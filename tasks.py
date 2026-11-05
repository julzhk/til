"""Site tasks. Run `inv --list` to see them.

    inv build     # render the site into _site/ and open it
    inv watch     # rebuild whenever posts, pages, templates or static files change
    inv serve     # build, then preview at http://localhost:8000
    inv deploy    # build, then deploy to Fly.io
"""

import sys
import threading
import time
from pathlib import Path

from invoke import task
from invoke.exceptions import UnexpectedExit

SITE_DIR = "_site"
ROOT = Path(__file__).resolve().parent
# What counts as "content": anything here triggers a rebuild.
WATCH_PATHS = ["posts", "pages", "templates", "static", "scripts/build_site.py"]


@task(help={"open": "Open the built site in a browser (default: on)."})
def build(c, open=True):
    """Render the site into _site/."""
    c.run(f"{sys.executable} scripts/build_site.py {SITE_DIR}")
    if open:
        c.run(f"open {SITE_DIR}/index.html")


@task(help={"delay": "Seconds to wait for more changes before rebuilding."})
def watch(c, delay=0.5):
    """Rebuild the site whenever content changes (Ctrl-C to stop)."""
    from watchdog.events import FileSystemEventHandler
    from watchdog.observers import Observer

    pending = threading.Event()

    class OnChange(FileSystemEventHandler):
        def on_any_event(self, event):
            if event.event_type in ("opened", "closed_no_write"):
                return  # reads, not changes
            path = Path(event.src_path)
            if path.name.startswith(".") or path.name.endswith("~"):
                return  # editor swap/backup files
            print(f"changed: {path.relative_to(ROOT)}")
            pending.set()

    observer = Observer()
    handler = OnChange()
    for rel in WATCH_PATHS:
        target = ROOT / rel
        if target.is_dir():
            observer.schedule(handler, str(target), recursive=True)
        elif target.exists():
            observer.schedule(handler, str(target.parent), recursive=False)
    observer.start()

    build(c)  # initial build, opens the browser once
    print(f"Watching {', '.join(WATCH_PATHS)} (Ctrl-C to stop)")
    try:
        while True:
            pending.wait()
            time.sleep(delay)  # let a burst of saves settle into one rebuild
            pending.clear()
            try:
                build(c, open=False)
            except UnexpectedExit:
                print("Build failed; waiting for the next change.")
    except KeyboardInterrupt:
        pass
    finally:
        observer.stop()
        observer.join()


@task(pre=[build])
def serve(c, port=8000):
    """Build, then serve the site locally."""
    print(f"Serving http://localhost:{port}  (Ctrl-C to stop)")
    c.run(f"{sys.executable} -m http.server {port} --directory {SITE_DIR}", pty=True)


@task(pre=[build])
def deploy(c):
    """Build, then deploy to Fly.io (app and region are set in fly.toml)."""
    c.run("flyctl deploy", pty=True)
