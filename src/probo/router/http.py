from bottle import request as _request
from bottle import response as _response
from bottle import redirect, abort, static_file


request = _request
response = _response

def get_wsgi_environ():
    """
    FIXED: Must be a function to avoid evaluating .environ
    before a request context actually exists!
    """
    return request.environ

class RouterRequestdata:
    
    def __init__(self,) -> None:
        self.request=request
        self.response=response

    def get_params(self,):
        return self.request.params


    def get_query(self,):
        return self.request.query


    def get_forms(self,):
        return self.request.forms


    def get_json(self,):
        return self.request.json


    def get_files(self,):
        return self.request.files


def set_cookie(
    name: str, value: str, secret: str = None, max_age: int = 31536000, **kwargs
):
    response.set_cookie(name, value, secret=secret, max_age=max_age, path="/", **kwargs)


def get_cookie(name: str, default: str = None, secret: str = None) -> str:
    return request.get_cookie(name, default=default, secret=secret)


def hx_redirect(url: str):
    response.set_header("HX-Redirect", url)
    return ""


def get_upload(key: str):
    """
    Retrieves a file upload from the request.
    Returns a Bottle FileUpload object.
    """
    return request.files.get(key)


def save_upload(key: str, save_path: str, overwrite: bool = False):
    """
    Shortcut to save an uploaded file to disk.
    """
    upload = get_upload(key)
    if upload:
        upload.save(save_path, overwrite=overwrite)
        return True
    return False
