from ..domains.products.actions.products_list_action import productsListAction
from ..domains.products.requests.products_list_id_request import ProductsListIdRequest
from ..domains.products.actions.products_search_action import productsSearchAction
from ..domains.products.requests.products_list_request import ProductsListRequest
from ..domains.products.requests.products_search_request import ProductsSearchRequest
from ..http.response import Response

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

    @staticmethod
    def search(request):
        searchRequest = ProductsSearchRequest(request)

        response = productsSearchAction(searchRequest)

        return Response({
            "message": "success.products.list",
            "data": response
        })
