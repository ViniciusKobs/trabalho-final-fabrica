from sqlalchemy import func
from ..database.db import DB


class PricingModel(DB.db.Model):
    __tablename__ = 'pricing'

    id = DB.db.Column(DB.db.Integer, primary_key=True, autoincrement=True)
    product_id = DB.db.Column(DB.db.Integer, DB.db.ForeignKey('products.id'))
    market_id = DB.db.Column(DB.db.Integer, DB.db.ForeignKey('markets.id'))
    price = DB.db.Column(DB.db.Float)
    created_at = DB.db.Column(DB.db.DateTime, server_default=DB.db.text('CURRENT_TIMESTAMP'))
    updated_at = DB.db.Column(DB.db.DateTime, server_default=DB.db.text('CURRENT_TIMESTAMP'), server_onupdate=DB.db.text('CURRENT_TIMESTAMP'))

    @staticmethod
    def getBestMarketId(products):
        market = (
            PricingModel.query.with_entities(
                PricingModel.market_id,
                func.sum(PricingModel.price).label('total')
            )
            .filter(PricingModel.product_id.in_(products))
            .group_by(PricingModel.market_id)
            .order_by('total')
            .first().market_id
        )

        return market