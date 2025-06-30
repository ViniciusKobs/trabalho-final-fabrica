from flask_sqlalchemy import SQLAlchemy

DB_USER = 'user'
DB_PASSWORD = 'pass'
DB_HOST = 'db'
DB_PORT = 3306
DB_NAME = 'market'

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
