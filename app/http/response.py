class Response:
    def __init__(self, body, status = 200):
        self.status = status
        self.body = body

    @staticmethod
    def message(msg, status = 200):
        return Response({
            "message": msg,
        }, status)
