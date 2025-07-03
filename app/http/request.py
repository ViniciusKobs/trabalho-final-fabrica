from flask import request
from ..exceptions.public_exception import PublicException

class Request:
    def __init__(
        self,
        req = None
    ):
        if req is None:
            dynamic_routes = dict(request.view_args)
            url_params     = dict(request.args)
            self.url       = RequestDataSource(dynamic_routes | url_params)
            self.headers   = RequestDataSource(request.headers)
            if request.is_json:
                self.body = RequestDataSource(request.get_json())
            else:
                self.body = RequestDataSource({})
        else:
            self.url       = req.url
            self.headers   = req.headers
            self.body      = req.body

class RequestDataSource:
    def __init__(self, data):
        self.data = data

    def get(self, key):
        if key in self.data:
            return self.data[key]
        return None

    def getOrFail(self, key, msg = None):
        if key in self.data:
            return self.data[key]
        if msg is not None:
            raise PublicException(msg, 400)
        raise Exception

    def exists(self, key):
        return key in self.data