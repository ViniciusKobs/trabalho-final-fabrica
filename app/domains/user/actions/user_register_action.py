from app.database.db import DB
from app.models.user_model import UserModel

def userRegisterAction(user):
    UserModel.register(user)
    DB.commit()