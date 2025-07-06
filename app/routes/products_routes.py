from flask import Blueprint, request
from ..controllers.products_controller import ProductsController
from ..http.dispatcher import dispatch

products_route = Blueprint('products_route', __name__)

@products_route.route('/products', methods=["GET"])
def __products():
    if request.method == "GET": return dispatch(ProductsController.list)
