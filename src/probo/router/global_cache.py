from probo.router.cache import ProboCache 
import os, hashlib
from typing import Optional

global_cache = ProboCache()

def file_hash(filepath: str) -> str:
    """Generates an MD5 hash of a file's contents to detect changes."""
    if not os.path.exists(filepath):
        return ""
    with open(filepath, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def get_or_render(filepath: str, render_func=None, ttl: int = 86400) -> Optional[str]:
    """
    Checks the global cache for a file's rendered output.
    If the file hasn't changed (based on hash), returns the cached HTML.
    Otherwise, calls render_func(), caches the new HTML, and returns it.
    """
    key = f"file:{filepath}"
    current_hash = file_hash(filepath)
    global global_cache
    cached = global_cache.get(key)

    # Cache Hit: File hasn't been modified
    if cached and cached.get("hash") == current_hash:
        return cached["html"]

    # Cache Miss: File was modified or not cached yet
    if render_func:
        html = render_func() if callable(render_func) else str(render_func)
        global_cache.set_cache(key, {"hash": current_hash, "html": html}, ttl=ttl)
        return html

    return None
