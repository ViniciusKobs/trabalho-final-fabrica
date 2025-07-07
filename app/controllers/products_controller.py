from ..domains.products.actions.products_list_action import productsListAction
from ..domains.products.actions.products_list_by_id_action import productsListByIdAction
from ..domains.products.requests.products_list_id_request import ProductsListByIdRequest
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
        listIdRequest = ProductsListByIdRequest(request)

        product = productsListByIdAction(listIdRequest)

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
