from app.http.request import Request

class ProductsGetBestMarket(Request):
    def __init__(self, req):
        super().__init__(req)
        self.products = self.url.getOrFail('products', 'error.products.productsIsRequired')

    def getProducts(self):
        return self.products