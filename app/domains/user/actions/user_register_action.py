from app.database.db import DB
from app.models.user_model import UserModel
from app.service.hash import hash_password


def userRegisterAction(user):
    user.password = hash_password(user.password)
    UserModel.register(user)
    DB.commit()