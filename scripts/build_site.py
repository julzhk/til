"""Build a static TIL site from the top-level markdown files in this repo.

Each *.md file in the repo root (excluding README.md) becomes a post.
Posts are ordered newest-first by the date of their first git commit,
and the index is paginated at POSTS_PER_PAGE posts per page.

Usage: python scripts/build_site.py [output_dir]
"""

import html
import math
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "_site"
POSTS_PER_PAGE = 25
SITE_TITLE = "TIL — Today I Learned"
SITE_URL = "https://julzhk.github.io"
REPO_URL = "https://github.com/julzhk/til"
EXCLUDE = {"README.md"}

MD_EXTENSIONS = ["fenced_code", "tables", "sane_lists", "toc", "smarty"]


@dataclass
class Post:
    slug: str
    title: str
    date: datetime
    body_html: str
    summary: str
    source: str


def git_date(path: Path) -> datetime:
    """Date the file was first committed; falls back to mtime for uncommitted files."""
    out = subprocess.run(
        ["git", "log", "--follow", "--diff-filter=A", "--format=%aI", "--", path.name],
        cwd=ROOT, capture_output=True, text=True,
    ).stdout.split()
    if out:
        return datetime.fromisoformat(out[-1])
    return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)


LEADING_HEADING = re.compile(r"^\s*<h[1-3][^>]*>(.*?)</h[1-3]>", re.S)


def split_title(body_html: str, fallback: str) -> tuple[str, str]:
    """Use a leading heading as the title (removing it from the body), else the fallback."""
    match = LEADING_HEADING.match(body_html)
    if not match:
        return fallback, body_html
    title = html.unescape(re.sub(r"<[^>]+>", "", match.group(1))).strip()
    return title or fallback, body_html[match.end():]


def summarize(body_html: str, length: int = 280) -> str:
    text = re.sub(r"<pre.*?</pre>", " ", body_html, flags=re.S)
    text = html.unescape(re.sub(r"<[^>]+>", " ", text))
    text = " ".join(text.split())
    return text if len(text) <= length else text[:length].rsplit(" ", 1)[0] + "…"


def load_posts() -> list[Post]:
    posts = []
    for path in sorted(ROOT.glob("*.md")):
        if path.name in EXCLUDE:
            continue
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            continue
        body = markdown.markdown(text, extensions=MD_EXTENSIONS)
        fallback = path.stem.replace("-", " ").replace("_", " ").capitalize()
        title, body = split_title(body, fallback)
        slug = re.sub(r"[^a-z0-9]+", "-", path.stem.lower()).strip("-")
        posts.append(Post(slug, title, git_date(path), body, summarize(body), path.name))
    posts.sort(key=lambda p: p.date, reverse=True)
    return posts


def layout(title: str, content: str, root: str) -> str:
    """root is the relative path back to the site root ('' or '../')."""
    return f"""<!doctype html>
<html lang="en" class="h-full">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <script src="https://cdn.tailwindcss.com?plugins=typography"></script>
  <script>tailwind.config = {{ darkMode: 'media' }}</script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
  <script>document.addEventListener('DOMContentLoaded', () => hljs.highlightAll());</script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
    body {{ font-family: 'Inter', system-ui, sans-serif; }}
    .font-mono, code, pre {{ font-family: 'JetBrains Mono', ui-monospace, monospace; }}
    .prose pre {{ padding: 0; }}
    .prose pre code.hljs {{ border-radius: 0.5rem; }}
  </style>
</head>
<body class="min-h-full bg-slate-50 text-slate-800 dark:bg-slate-950 dark:text-slate-200 antialiased">
  <header class="border-b border-slate-200 dark:border-slate-800 bg-white/80 dark:bg-slate-900/80 backdrop-blur sticky top-0 z-10">
    <div class="max-w-3xl mx-auto px-4 h-14 flex items-center justify-between">
      <a href="{root}index.html" class="font-mono font-semibold text-slate-900 dark:text-white">
        <span class="text-emerald-500">~/</span>til<span class="animate-pulse text-emerald-500">_</span>
      </a>
      <nav class="flex gap-5 text-sm text-slate-500 dark:text-slate-400">
        <a href="{root}index.html" class="hover:text-emerald-500">Posts</a>
        <a href="{REPO_URL}" class="hover:text-emerald-500">GitHub</a>
      </nav>
    </div>
  </header>
  <main class="max-w-3xl mx-auto px-4 py-10">
{content}
  </main>
  <footer class="border-t border-slate-200 dark:border-slate-800 py-8 text-center text-xs font-mono text-slate-400">
    Built from <a class="underline hover:text-emerald-500" href="{REPO_URL}">julzhk/til</a> · {datetime.now(timezone.utc):%Y-%m-%d}
  </footer>
</body>
</html>
"""


def page_href(n: int, root: str = "") -> str:
    return f"{root}index.html" if n == 1 else f"{root}page/{n}.html"


def render_index(posts: list[Post], page: int, total_pages: int, intro: str) -> str:
    root = "" if page == 1 else "../"
    items = "\n".join(
        f"""      <li class="py-5 group">
        <a href="{root}posts/{p.slug}.html" class="block">
          <time class="font-mono text-xs text-emerald-600 dark:text-emerald-400">{p.date:%Y-%m-%d}</time>
          <h2 class="mt-1 text-lg font-semibold text-slate-900 dark:text-white group-hover:text-emerald-500 transition-colors">{html.escape(p.title)}</h2>
          <p class="mt-1 text-sm text-slate-500 dark:text-slate-400">{html.escape(p.summary)}</p>
        </a>
      </li>"""
        for p in posts
    )
    hero = intro if page == 1 else ""
    content = f"""    {hero}
    <ul class="divide-y divide-slate-200 dark:divide-slate-800">
{items}
    </ul>
{render_pager(page, total_pages, root)}"""
    title = SITE_TITLE if page == 1 else f"{SITE_TITLE} — page {page}"
    return layout(title, content, root)


def render_pager(page: int, total_pages: int, root: str) -> str:
    if total_pages <= 1:
        return ""
    btn = "px-3 py-1.5 rounded-md border border-slate-200 dark:border-slate-800 font-mono text-sm"
    prev = (f'<a class="{btn} hover:border-emerald-500 hover:text-emerald-500" href="{page_href(page - 1, root)}">← newer</a>'
            if page > 1 else f'<span class="{btn} opacity-40">← newer</span>')
    nxt = (f'<a class="{btn} hover:border-emerald-500 hover:text-emerald-500" href="{page_href(page + 1, root)}">older →</a>'
           if page < total_pages else f'<span class="{btn} opacity-40">older →</span>')
    numbers = " ".join(
        f'<span class="{btn} bg-emerald-500 border-emerald-500 text-white">{n}</span>' if n == page
        else f'<a class="{btn} hover:border-emerald-500 hover:text-emerald-500" href="{page_href(n, root)}">{n}</a>'
        for n in range(1, total_pages + 1)
    )
    return f"""    <nav class="mt-10 flex flex-wrap items-center justify-between gap-3" aria-label="Pagination">
      {prev}
      <div class="flex flex-wrap gap-2">{numbers}</div>
      {nxt}
    </nav>"""


def render_post(post: Post) -> str:
    content = f"""    <article>
      <header class="mb-8">
        <a href="../index.html" class="font-mono text-sm text-slate-400 hover:text-emerald-500">← all posts</a>
        <h1 class="mt-4 text-3xl sm:text-4xl font-extrabold tracking-tight text-slate-900 dark:text-white">{html.escape(post.title)}</h1>
        <div class="mt-3 font-mono text-xs text-slate-500 flex gap-4">
          <time>{post.date:%B %-d, %Y}</time>
          <a class="hover:text-emerald-500" href="{REPO_URL}/blob/master/{post.source}">view source</a>
        </div>
      </header>
      <div class="prose prose-slate dark:prose-invert max-w-none prose-a:text-emerald-600 dark:prose-a:text-emerald-400 prose-code:before:content-none prose-code:after:content-none">
{post.body_html}
      </div>
    </article>"""
    return layout(f"{post.title} · TIL", content, "../")


def render_intro(count: int) -> str:
    return f"""<section class="mb-10">
      <h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight text-slate-900 dark:text-white">Today I Learned</h1>
      <p class="mt-3 text-slate-500 dark:text-slate-400">Concise write-ups on small things I learn day to day across languages and technologies.
        <span class="font-mono text-emerald-600 dark:text-emerald-400">{count} posts</span></p>
    </section>"""


def main() -> None:
    posts = load_posts()
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "posts").mkdir(parents=True)
    (OUT / "page").mkdir()

    for post in posts:
        (OUT / "posts" / f"{post.slug}.html").write_text(render_post(post), encoding="utf-8")

    total_pages = max(1, math.ceil(len(posts) / POSTS_PER_PAGE))
    intro = render_intro(len(posts))
    for page in range(1, total_pages + 1):
        chunk = posts[(page - 1) * POSTS_PER_PAGE: page * POSTS_PER_PAGE]
        target = OUT / ("index.html" if page == 1 else f"page/{page}.html")
        target.write_text(render_index(chunk, page, total_pages, intro), encoding="utf-8")

    # Keep any static images referenced relatively by posts.
    if (ROOT / "images").is_dir():
        shutil.copytree(ROOT / "images", OUT / "images")
    (OUT / ".nojekyll").touch()
    print(f"Built {len(posts)} posts across {total_pages} page(s) into {OUT}")


if __name__ == "__main__":
    main()
