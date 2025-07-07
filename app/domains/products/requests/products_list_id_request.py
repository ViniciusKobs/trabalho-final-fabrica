from app.http.request import Request

class ProductsListByIdRequest(Request):
        def __init__(self, req):
            super().__init__(req)
            self.id = self.url.getOrFail("id", "error.products.missingProductId")
