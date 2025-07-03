from ..domains.user.actions.user_register_action import userRegisterAction
from ..domains.user.requests.user_register_request import UserRegisterRequest
from ..http.response import Response

class UserController:
    @staticmethod
    def register(request):
        registerRequest = UserRegisterRequest(request)

        userRegisterAction(registerRequest.toDTO())

        return Response.message("success.user.register")
