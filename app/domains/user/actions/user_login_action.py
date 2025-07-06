from app.models.user_model import UserModel
from app.service.hash import hash_password

def userLoginAction(user):
    return UserModel.login(
        user.email,
        hash_password(user.password)
    )