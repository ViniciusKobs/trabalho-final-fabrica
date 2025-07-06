from uuid import uuid4
from ..database.db import DB

class UserModel(DB.db.Model):
    __tablename__ = 'users'

    id = DB.db.Column(DB.db.String(36), primary_key=True, autoincrement=False, default=lambda: str(uuid4()), server_default=DB.db.text('UUID()'))
    username = DB.db.Column(DB.db.String(255), nullable=False, unique=True)
    password = DB.db.Column(DB.db.String(255), nullable=False)
    email = DB.db.Column(DB.db.String(255), nullable=False, unique=True)
    created_at = DB.db.Column(DB.db.DateTime, server_default=DB.db.text('CURRENT_TIMESTAMP'))
    updated_at = DB.db.Column(DB.db.DateTime, server_default=DB.db.text('CURRENT_TIMESTAMP'), server_onupdate=DB.db.text('CURRENT_TIMESTAMP'))

    @staticmethod
    def register(user):
        new_user = UserModel(
            username = user.username,
            password = user.password,
            email    = user.email
        )
        DB.add(new_user)


    def find_by_email(email):
        if UserModel.query.filter_by(email=email).exists():
            return UserModel.query.filter_by(email=email).first()
        else:
            return False
