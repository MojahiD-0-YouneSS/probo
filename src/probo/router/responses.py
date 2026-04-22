import gzip
import json
from typing import Any, Dict, Generator


def gzip_response(body: str, response) -> bytes:
    """Compresses a string body using GZIP and sets appropriate headers."""
    compressed = gzip.compress(body.encode("utf-8"))
    response.set_header("Content-Encoding", "gzip")
    response.set_header("Content-Length", str(len(compressed)))
    return compressed


def json_response(data: Any, response) -> str:
    """Returns a JSON formatted string and sets the application/json header."""
    response.set_header("Content-Type", "application/json")
    return json.dumps(data)


def html_response(html: str, response) -> str:
    """Explicitly sets the text/html content type (useful for APIs returning UI chunks)."""
    response.set_header("Content-Type", "text/html; charset=utf-8")
    return html


def plain_text_response(text: str, response) -> str:
    """Returns raw text with the text/plain header."""
    response.set_header("Content-Type", "text/plain; charset=utf-8")
    return text


def download_response(file_bytes: bytes, filename: str, response) -> bytes:
    """Forces the browser to download the content as a file."""
    response.set_header("Content-Type", "application/octet-stream")
    response.set_header("Content-Disposition", f'attachment; filename="{filename}"')
    response.set_header("Content-Length", str(len(file_bytes)))
    return file_bytes


def no_content_response(response) -> str:
    """
    Returns an empty 204 No Content response.
    Crucial for HTMX: A 204 response tells HTMX to leave the target alone
    or safely remove it (if hx-swap="delete" is used).
    """
    response.status = 204
    return ""


def sse_response(stream_gen: Generator, response) -> Generator:
    """
    Prepares headers for Server-Sent Events (SSE).
    Expects a generator that yields formatted SSE strings: f"data: {chunk}\\n\\n"
    """
    response.set_header("Content-Type", "text/event-stream")
    response.set_header("Cache-Control", "no-cache")
    response.set_header("Connection", "keep-alive")
    return stream_gen
