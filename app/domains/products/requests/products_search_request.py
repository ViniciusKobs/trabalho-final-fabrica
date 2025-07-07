from app.http.request import Request

class ProductsSearchRequest(Request):
    def __init__(self, req):
        super().__init__(req)
        self.products = self.body.getOrFail('products', 'error.products.productsIsRequired')

    def getProducts(self):
        for product in self.products:
            print(product)
        return [products['id'] for products in self.products]