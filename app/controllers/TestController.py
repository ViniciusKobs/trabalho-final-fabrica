from ..http.Response import Response

class TestController:
    @staticmethod
    def index(request):
        return Response.message("Hello World")