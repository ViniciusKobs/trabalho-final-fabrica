from app.exceptions.public_exception import PublicException
from app.models.user_model import UserModel
from app.service.hash import hash_password


def userLoginAction(user):
    user_model = UserModel.find_by_email(user.email)

    if  not user_model:
        raise PublicException('failure.login.userNotFound')

    if user_model.password != hash_password(user.password):
        raise PublicException('failure.login.userPasswordIncorrect')

    return user_model.id