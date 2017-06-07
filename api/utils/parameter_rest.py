import requests

class Parameter:

    params = None
    body = None
    headers = {"Content-type": "application/json"}
    retry = 3
    timeout = 1

    def __init__(self, params=None, body=None, headers=None, retry=None, timeout=None):
        self.params = params
        self.body = body
        if headers is not None:
            self.headers = headers
        if retry is not None:
            self.retry = retry
        if timeout is not None:
            self.timeout = timeout
