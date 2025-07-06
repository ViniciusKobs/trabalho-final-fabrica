from ..domains.products.actions.products_list_action import productsListAction
from ..domains.products.requests.products_list_id_request import ProductsListIdRequest
from ..domains.products.requests.products_list_request import ProductsListRequest
from ..http.response import Response


def productsListIdAction(listIdRequest):
    pass


class ProductsController:
    @staticmethod
    def list(request):
        listRequest = ProductsListRequest(request)

        products = productsListAction(listRequest)

        return Response({
            "message": "success.products.list",
            "products": products.toArray()
        })

    @staticmethod
    def listById(request):
        listIdRequest = ProductsListIdRequest(request)

        product = productsListIdAction(listIdRequest)

        return Response({
            "message": "success.products.list",
            "product": product.toDict()
        })