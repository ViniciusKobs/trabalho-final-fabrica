from ..domains.user.actions.user_login_action import userLoginAction
from ..domains.user.actions.user_register_action import userRegisterAction
from ..domains.user.requests.user_register_request import UserRegisterRequest
from ..exceptions.public_exception import PublicException
from ..http.response import Response
from ..domains.user.requests.user_login_request import UserLoginRequest
from ..service.jwt import create_jwt_token


class UserController:
    @staticmethod
    def register(request):
        registerRequest = UserRegisterRequest(request)

        userRegisterAction(registerRequest.toDTO())

        return Response.message("success.user.register")

    @staticmethod
    def login(request):
        loginRequest = UserLoginRequest(request)

        try:
            userId = userLoginAction(loginRequest.toDTO())
        except PublicException as e:
            return Response.message(str(e))

        jwt = create_jwt_token(userId)

        response = {
            "jwt": jwt,
            "message": "success.user.login"
        }

        return Response(response)