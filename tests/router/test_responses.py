import pytest
import json
import gzip
from probo.router.responses import (
    gzip_response,
    json_response,
    html_response,
    plain_text_response,
    download_response,
    no_content_response,
    sse_response,
)

# ==========================================
# FIXTURES & MOCKS
# ==========================================


class MockResponse:
    """
    Mocks the Bottle response object.
    Since Probo response helpers accept the response object directly,
    we can easily inject this mock without needing monkeypatch!
    """

    def __init__(self):
        self.headers = {}
        self.status = 200

    def set_header(self, key, value):
        self.headers[key] = value


@pytest.fixture
def mock_res():
    return MockResponse()


# ==========================================
# TESTS
# ==========================================


def test_gzip_response(mock_res):
    """Tests that GZIP compression works and sets correct headers."""
    body = "Hello Probo! " * 100
    compressed_bytes = gzip_response(body, mock_res)

    # Verify Headers
    assert mock_res.headers["Content-Encoding"] == "gzip"
    assert mock_res.headers["Content-Length"] == str(len(compressed_bytes))

    # Verify Data (Decompressing the result should perfectly match the original string)
    decompressed_body = gzip.decompress(compressed_bytes).decode("utf-8")
    assert decompressed_body == body
    assert isinstance(compressed_bytes, bytes)


def test_json_response(mock_res):
    """Tests JSON serialization and Content-Type."""
    data = {"status": "success", "items": [1, 2, 3]}
    result = json_response(data, mock_res)

    assert mock_res.headers["Content-Type"] == "application/json"
    assert json.loads(result) == data
    assert isinstance(result, str)


def test_html_response(mock_res):
    """Tests explicit HTML headers (crucial for HTMX chunk responses)."""
    html_content = "<div id='test'>UI Chunk</div>"
    result = html_response(html_content, mock_res)

    assert mock_res.headers["Content-Type"] == "text/html; charset=utf-8"
    assert result == html_content


def test_plain_text_response(mock_res):
    """Tests raw text returns."""
    text_content = "Just some standard logs."
    result = plain_text_response(text_content, mock_res)

    assert mock_res.headers["Content-Type"] == "text/plain; charset=utf-8"
    assert result == text_content


def test_download_response(mock_res):
    """Tests the force-download headers for files like PDFs and CSVs."""
    file_data = b"fake_binary_data_010101"
    filename = "report.csv"

    result = download_response(file_data, filename, mock_res)

    # File downloads require 3 specific headers
    assert mock_res.headers["Content-Type"] == "application/octet-stream"
    assert (
        mock_res.headers["Content-Disposition"] == 'attachment; filename="report.csv"'
    )
    assert mock_res.headers["Content-Length"] == str(len(file_data))

    assert result == file_data
    assert isinstance(result, bytes)


def test_no_content_response(mock_res):
    """Tests the HTTP 204 No Content status update."""
    result = no_content_response(mock_res)

    # Status code must be 204, and body must be totally empty
    assert mock_res.status == 204
    assert result == ""


def test_sse_response(mock_res):
    """Tests Server-Sent Events header preparation and generator passthrough."""

    def fake_stream():
        yield "data: one\n\n"
        yield "data: two\n\n"

    gen = fake_stream()
    result_gen = sse_response(gen, mock_res)

    # SSE requires these exact 3 headers to keep the connection open
    assert mock_res.headers["Content-Type"] == "text/event-stream"
    assert mock_res.headers["Cache-Control"] == "no-cache"
    assert mock_res.headers["Connection"] == "keep-alive"

    # Ensure it passes the generator through untouched so Bottle/FastAPI can consume it
    chunks = list(result_gen)
    assert chunks == ["data: one\n\n", "data: two\n\n"]
