"""Build a static personal site from the markdown in this repo.

- posts/*.md   -> blog posts (newest first, dated by their first git commit)
- pages/*.md   -> standalone pages (about, projects, now, uses, contact)
- templates/   -> Jinja templates; shared pieces live in templates/macros.html.
                  A page uses templates/pages/<name>.html if present, else templates/page.html.
- static/      -> copied as-is into the site root (put resume.pdf here)

Usage: python scripts/build_site.py [output_dir]
"""

import html
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "_site"
POSTS_DIR = ROOT / "posts"
PAGES_DIR = ROOT / "pages"
STATIC_DIR = ROOT / "static"
TEMPLATES_DIR = ROOT / "templates"

# --- Site details: edit these -------------------------------------------------
SITE = {
    "author": "Julian Harley",
    "tagline": "Software developer. I build things. and think about things. and maybe write about them.",
    "url": "https://julzhk.fly.dev",
    "repo_url": "https://github.com/julzhk/til",
    "github_url": "https://github.com/julzhk",
    "email": "vinegar_mica.0d@icloud.com",
    "linkedin_url": "https://www.linkedin.com/in/julian-h-b82b171/",
    "resume_path": "julian_harley_resume.pdf",
    "location": "somewhere with decent tea",
    "quips": [
        "No dinosaurs were harmed in the making of this website.",
        "This page weighs less than a cookie banner.",
        "Written by a human. So typos are a feature.",
        "Best viewed with curiosity and a hot drink.",
        "How hard could it be?",
        "Contains no trackers, cookies, or newsletter pop-ups.",
        "Works on my machine.",
        "That's a good problem to have.",
    ],
}

# projects, shown on the home page (first two) and the projects page.
PROJECTS = [
    {"name": "TIL", "year": "2025",
     "desc": "This site: a Markdown notebook turned into a static site by Python.",
     "url": SITE["repo_url"], "tags": ["Python", "Markdown"]},
    {"name": "Screen Dream", "year": "2026",
     "desc": "Music, rendered as worlds: an audio-reactive visualizer for macOS",
     "url": "https://github.com/julzhk/screendream#screendream", "tags": ["App", "Rust"]},
    {"name": "Code Health Analysis", "year": "2024",
     "desc": "Uses git logs to measure code hotspots (eg:churn); changes in cyclometric complexity; maintainability",
     "url": "https://github.com/julzhk/git-analysis#git-analysis", "tags": ["Git", "Python"]},
    {"name": "Dino maze escape", "year": "2025",
     "desc": "3D maze escape. Watch out for T.Rexes. And the Pterosaurs want to eat you too!",
     "url": "https://dino-seth.itch.io/dino-maze", "tags": ["Godot", "Game","Fun"]},
]

# (key, label, href) for the tab bar; a page's key marks its tab as active.
NAV = [("home", "Home", "index.html"), ("blog", "Blog", "blog/index.html"),
       ("projects", "Projects", "projects.html"), ("about", "About", "about.html"),
       ("now", "Now", "now.html"), ("contact", "Contact", "contact.html")]
# -------------------------------------------------------------------------------

MD_EXTENSIONS = ["fenced_code", "tables", "sane_lists", "toc", "smarty"]


@dataclass
class Post:
    slug: str
    title: str
    date: datetime
    body_html: str
    summary: str
    source: str


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True).stdout.strip()


def git_date(path: Path) -> datetime:
    """Date the file was first committed (following renames); mtime for uncommitted files."""
    rel = path.relative_to(ROOT).as_posix()
    out = git("log", "--follow", "--diff-filter=A", "--format=%aI", "--", rel).split()
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


def summarize(body_html: str, length: int = 200) -> str:
    text = re.sub(r"<pre.*?</pre>", " ", body_html, flags=re.S)
    text = html.unescape(re.sub(r"<[^>]+>", " ", text))
    text = " ".join(text.split())
    return text if len(text) <= length else text[:length].rsplit(" ", 1)[0] + "…"


def render_md(path: Path) -> tuple[str, str]:
    body = markdown.markdown(path.read_text(encoding="utf-8"), extensions=MD_EXTENSIONS)
    fallback = path.stem.replace("-", " ").replace("_", " ").capitalize()
    return split_title(body, fallback)


def load_posts() -> list[Post]:
    posts = []
    for path in sorted(POSTS_DIR.glob("*.md")):
        if not path.read_text(encoding="utf-8").strip():
            continue
        title, body = render_md(path)
        slug = re.sub(r"[^a-z0-9]+", "-", path.stem.lower()).strip("-")
        posts.append(Post(slug, title, git_date(path), body, summarize(body),
                          path.relative_to(ROOT).as_posix()))
    posts.sort(key=lambda p: p.date, reverse=True)
    return posts


def make_env(posts: list[Post]) -> Environment:
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(["html", "xml"]),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["rfc822"] = format_datetime
    env.globals.update(
        site=SITE,
        nav=NAV,
        projects=PROJECTS,
        posts=posts,
        post_count=len(posts),
        build={"time": datetime.now(timezone.utc), "sha": git("rev-parse", "--short", "HEAD") or "unknown"},
        active="",
    )
    return env


def main() -> None:
    posts = load_posts()
    env = make_env(posts)

    if OUT.exists():
        shutil.rmtree(OUT)

    def render(template: str, dest: str, **context) -> None:
        target = OUT / dest
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(env.get_template(template).render(**context), encoding="utf-8")

    render("home.html", "index.html", root="", active="home")
    render("blog.html", "blog/index.html", root="../", active="blog", title="Blog")
    for post in posts:
        render("post.html", f"posts/{post.slug}.html", root="../", active="blog", post=post)

    pages = sorted(p.stem for p in PAGES_DIR.glob("*.md"))
    for name in pages:
        title, body_html = render_md(PAGES_DIR / f"{name}.md")
        template = f"pages/{name}.html" if (TEMPLATES_DIR / "pages" / f"{name}.html").exists() else "page.html"
        render(template, f"{name}.html", root="", active=name, title=title, body_html=body_html)

    render("404.html", "404.html", root="/")
    render("feed.xml", "feed.xml")

    if STATIC_DIR.is_dir():
        shutil.copytree(STATIC_DIR, OUT, dirs_exist_ok=True)
    (OUT / ".nojekyll").touch()
    print(f"Built {len(posts)} posts and {len(pages)} pages into {OUT}")


if __name__ == "__main__":
    main()
