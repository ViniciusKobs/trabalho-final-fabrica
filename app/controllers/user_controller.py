from ..domains.user.actions.user_login_action import userLoginAction
from ..domains.user.actions.user_register_action import userRegisterAction
from ..domains.user.requests.user_register_request import UserRegisterRequest
from ..http.response import Response
from ..domains.user.requests.user_login_request import UserLoginRequest
from ..service.jwt_service import createJwtToken


class UserController:
    @staticmethod
    def register(request):
        registerRequest = UserRegisterRequest(request)

        userRegisterAction(registerRequest.toDTO())

        return Response.message("success.user.register")

    @staticmethod
    def login(request):
        loginRequest = UserLoginRequest(request)

        userId = userLoginAction(loginRequest.toDTO())

        jwt = createJwtToken(userId)

        response = {
            "jwt": jwt,
            "message": "success.user.login"
        }

        return Response(response)