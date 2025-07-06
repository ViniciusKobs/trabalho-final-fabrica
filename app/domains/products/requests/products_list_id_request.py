from app.http.request import Request


class ProductsListIdRequest(Request):

        def __init__(self, req):
            super().__init__(req)
            self.productId = self.url.getOrFail("productId", "error.products.missingProductId")


        def getProductId(self):
            return self.productId