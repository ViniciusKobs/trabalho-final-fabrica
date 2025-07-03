from re import match, search
from app.domains.user.dtos.user_dto import UserDTO
from app.exceptions.public_exception import PublicException
from app.http.request import Request

class UserRegisterRequest(Request):
    def __init__(self, req):
        super().__init__(req)
        self.username = self.body.getOrFail('username', 'error.user.usernameIsRequired')
        self.email    = self.body.getOrFail('email',    'error.user.emailIsRequired')
        self.password = self.body.getOrFail('password', 'error.user.passwordIsRequired')
        self.validate()

    def validate(self):
        if not match(r'^[a-zA-Z0-9_]{3,20}$', self.username):
            raise PublicException('error.user.invalidUsername')

        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not match(email_pattern, self.email):
            raise PublicException('error.user.invalidEmail')

        if not (
            len(self.password) >= 5                and
            search(r'[A-Z]', self.password) and
            search(r'[a-z]', self.password) and
            search(r'[0-9]', self.password)
        ):
            raise PublicException('error.user.invalidPassword')

    def toDTO(self):
        return UserDTO(
            username = self.username,
            email    = self.email,
            password = self.password
        )