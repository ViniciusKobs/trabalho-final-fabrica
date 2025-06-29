from flask import Blueprint
from ..controllers.test_controller import TestController
from ..http.dispatcher import dispatch

test_route = Blueprint('test_route', __name__)

@test_route.route('/test', methods=["GET", "POST"])
def __test():
    return dispatch(TestController.index)
