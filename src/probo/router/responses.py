import gzip

def gzip_response(body: str,response) -> bytes:
    compressed = gzip.compress(body.encode("utf-8"))
    response.set_header("Content-Encoding", "gzip")
    response.set_header("Content-Length", str(len(compressed)))
    return compressed