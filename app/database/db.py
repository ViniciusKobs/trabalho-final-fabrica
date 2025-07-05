from os import getenv

from flask_sqlalchemy import SQLAlchemy

DB_USER = getenv("DB_USER")
DB_PASSWORD = getenv("DB_PASSWORD")
DB_HOST = getenv("DB_HOST")
DB_PORT = getenv("DB_PORT")
DB_NAME = getenv("DB_NAME")

class DB:
    db = SQLAlchemy()

    @staticmethod
    def init(app):
        app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        DB.db.init_app(app)

    @staticmethod
    def add(row):
        DB.db.session.add(row)

    @staticmethod
    def addAll(rows):
        DB.db.session.add_all(rows)

    @staticmethod
    def commit():
        DB.db.session.commit()

    @staticmethod
    def rollback():
        DB.db.session.rollback()
