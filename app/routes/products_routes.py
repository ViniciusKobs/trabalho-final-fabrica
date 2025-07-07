from flask import Blueprint, request
from ..controllers.products_controller import ProductsController
from ..http.dispatcher import dispatch
from app.http.middleware import jwt_required
products_route = Blueprint('products_route', __name__)

@products_route.route('/products', methods=["GET", "POST"])
@jwt_required
def __products():
    if request.method == "GET": return dispatch(ProductsController.list)
    if request.method == "POST": return dispatch(ProductsController.search)


@products_route.route('/products/{id}', methods=["GET"])
@jwt_required
def __product_id(_id):
    if request.method == "GET": return dispatch(ProductsController.listById)
