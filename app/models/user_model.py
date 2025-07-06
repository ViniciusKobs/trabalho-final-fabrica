from uuid import uuid4
from ..database.db import DB
from ..exceptions.public_exception import PublicException


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

    @staticmethod
    def login(email, password):
        user = UserModel.query.filter(
            UserModel.email == email,
            UserModel.password == password
        ).first()

        if user is None: raise PublicException('error.user.invalidCredentials')

        return user.id

    @staticmethod
    def existsByEmail(email):
        return UserModel.query.filter(
            UserModel.email == email,
        ).first() is not None

    @staticmethod
    def existsByUsername(username):
        return UserModel.query.filter(
            UserModel.username == username,
        ).first() is not None
