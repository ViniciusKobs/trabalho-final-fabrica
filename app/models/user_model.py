from ..database.db import DB

class UserModel(DB.db.Model):
    __tablename__ = 'usuarios'

    id       = DB.db.Column(DB.db.String(36), primary_key=True)
    username = DB.db.Column(DB.db.String(255), nullable=False, unique=True)
    password = DB.db.Column(DB.db.String(255), nullable=False)
    email    = DB.db.Column(DB.db.String(255), nullable=False, unique=True)

    @staticmethod
    def register(user):
        new_user = UserModel(
            id       = user.id,
            username = user.username,
            password = user.password,
            email    = user.email
        )
        DB.add(new_user)