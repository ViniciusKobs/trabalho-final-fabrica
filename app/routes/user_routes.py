from flask import Blueprint, request
from ..controllers.user_controller import UserController
from ..http.dispatcher import dispatch

user_route = Blueprint('user_route', __name__)

@user_route.route('/user', methods=["POST"])
def __user():
    # if request.method == "GET": return dispatch(UserController.register)
    if request.method == "POST": return dispatch(UserController.register)


@user_route.route('/login', methods=["POST"])
def __login():
    if request.method == "POST": return dispatch(UserController.login)