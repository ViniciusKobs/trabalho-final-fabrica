from app.models.pricing_model import PricingModel
from app.models.products_model import ProductsModel

def productsSearchAction(request):
    products = request.getProducts()
    market = PricingModel.getBestMarketId(products)
    return ProductsModel.getPricesInMarket(products, market)