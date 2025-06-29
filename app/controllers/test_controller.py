from ..http.response import Response

class TestController:
    @staticmethod
    def index(request):
        return Response.message("Hello World")