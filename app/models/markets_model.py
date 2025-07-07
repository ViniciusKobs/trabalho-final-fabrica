from ..database.db import DB

class MarketsModel(DB.db.Model):
    __tablename__ = 'markets'

    id = DB.db.Column(DB.db.Integer, primary_key=True, autoincrement=True)
    name = DB.db.Column(DB.db.String(255), nullable=False, unique=True)
    created_at = DB.db.Column(DB.db.DateTime, server_default=DB.db.text('CURRENT_TIMESTAMP'))
    updated_at = DB.db.Column(DB.db.DateTime, server_default=DB.db.text('CURRENT_TIMESTAMP'), server_onupdate=DB.db.text('CURRENT_TIMESTAMP'))
