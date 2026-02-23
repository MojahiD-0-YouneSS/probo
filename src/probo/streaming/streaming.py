import gzip
import io
from typing import Any, Iterator, Union, Iterable, Callable


class GzipStreamer:
    """
    Real-time Gzip Compressor.
    Compresses fragments on-the-fly as they are yielded.
    """

    def __init__(self, generator: Iterator[str], compress_level: int = 6):
        self.generator = generator
        self.compress_level = compress_level

    def __iter__(self) -> Iterator[bytes]:
        buffer = io.BytesIO()
        # Use the with block to manage the gzip object
        with gzip.GzipFile(fileobj=buffer, mode='wb', compresslevel=self.compress_level) as f:
            for fragment in self.generator:
                f.write(fragment.encode('utf-8'))
                f.flush()
                chunk = buffer.getvalue()
                if chunk:
                    yield chunk
                    buffer.seek(0)
                    buffer.truncate()

        # IMPORTANT: After the 'with' block closes, the Gzip footer is written.
        # We must yield this final chunk to make the stream valid.
        remainder = buffer.getvalue()
        if remainder:
            yield remainder

def stream_render(elements: Iterable[Callable]) -> Iterator[str]:
    """
    Memory-Efficient Recursive Streamer.
    Walks the tree and yields fragments without ever concatenating them
    into a single massive string in Python memory.
    """
    for el in elements:
        if callable(el):
            content=el()
            if hasattr(content,'render'):
                yield content.render()
            else:
                yield content
        else:
            yield str(el)

def to_django_response(node: Any, compress: bool = True):
    """
    Django Integration Utility.
    Returns a StreamingHttpResponse that keeps RAM usage flat.
    """
    from django.http import StreamingHttpResponse

    stream = node.render_stream()
    if compress:
        response = StreamingHttpResponse(GzipStreamer(stream))
        response['Content-Encoding'] = 'gzip'
    else:
        response = StreamingHttpResponse(stream)

    response['Content-Type'] = 'text/html; charset=utf-8'
    return response
