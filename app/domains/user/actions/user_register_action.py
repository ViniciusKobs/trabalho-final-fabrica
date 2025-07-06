from app.database.db import DB
from app.exceptions.public_exception import PublicException
from app.models.user_model import UserModel
from app.service.hash import hash_password

def userRegisterAction(user):
    if UserModel.existsByEmail(user.email):
        raise PublicException('error.user.emailAlreadyRegistered')

    if UserModel.existsByUsername(user.username):
        raise PublicException('error.user.usernameAlreadyRegistered')

    user.password = hash_password(user.password)

    UserModel.register(user)

    DB.commit()