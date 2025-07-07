from ..database.db import DB

class BrandsModel(DB.db.Model):
    __tablename__ = 'brands'

    id = DB.db.Column(DB.db.Integer, primary_key=True, autoincrement=True)
    name = DB.db.Column(DB.db.String(255), nullable=False, unique=True)
    description = DB.db.Column(DB.db.Text)
    image = DB.db.Column(DB.db.Text)
