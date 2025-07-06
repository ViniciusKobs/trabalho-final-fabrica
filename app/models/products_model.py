from ..database.db import DB
from sqlalchemy import or_

from ..exceptions.public_exception import PublicException


class ProductsModel(DB.db.Model):
    __tablename__ = 'products'

    id = DB.db.Column(DB.db.Integer, primary_key=True, autoincrement=True)
    brand_id = DB.db.Column(DB.db.Integer, DB.db.ForeignKey('brands.id'))
    name = DB.db.Column(DB.db.String(255), nullable=False, unique=True)
    description = DB.db.Column(DB.db.Text)
    image = DB.db.Column(DB.db.Text)
    weight = DB.db.Column(DB.db.Integer)
    volume = DB.db.Column(DB.db.Integer)
    units = DB.db.Column(DB.db.Integer)
    length = DB.db.Column(DB.db.Integer)
    created_at = DB.db.Column(DB.db.DateTime, server_default=DB.db.text('CURRENT_TIMESTAMP'))
    updated_at = DB.db.Column(DB.db.DateTime, server_default=DB.db.text('CURRENT_TIMESTAMP'), server_onupdate=DB.db.text('CURRENT_TIMESTAMP'))

    @staticmethod
    def list(request):
        dsc = request.getDsc()
        qtd = request.getQtd()
        order = request.getOrd()

        query = ProductsModel.query

        if dsc is not None:
            query = query.filter(or_(
                ProductsModel.name.like(f'%{dsc}%'),
                ProductsModel.description.like(f'%{dsc}%')
            ))

        if qtd is not None:
            query = query.filter(or_(
                ProductsModel.weight == qtd,
                ProductsModel.volume == qtd,
                ProductsModel.units  == qtd,
                ProductsModel.length == qtd,
            ))

        if order is not None:
            if order.startswith('-'):
                query = query.order_by(getattr(ProductsModel, order[1:]).desc())
            else:
                query = query.order_by(getattr(ProductsModel, order).asc())

        return query.all()

    @staticmethod
    def list_id(product_id):
        query = ProductsModel.query
        query = query.filter(ProductsModel.id == product_id).first()
        if query is None:
            raise PublicException("error.products.invalidProductId")
        return query
