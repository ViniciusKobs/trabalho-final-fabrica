from re import match, search
from app.domains.user.dtos.user_dto import UserDTO
from app.exceptions.public_exception import PublicException
from app.http.request import Request

class UserLoginRequest(Request):
    def __init__(self, req):
        super().__init__(req)
        self.email    = self.body.getOrFail('email',    'error.user.emailIsRequired')
        self.password = self.body.getOrFail('password', 'error.user.passwordIsRequired')

    def toDTO(self):
        return UserDTO(
            email    = self.email,
            password = self.password
        )