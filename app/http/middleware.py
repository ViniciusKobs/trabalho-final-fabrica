import jwt
from flask import request, jsonify
from functools import wraps
from app.service.jwt import validate_jwt_and_get_id
from os import getenv
SECRET_KEY = getenv('HASH_KEY')
def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return jsonify({"error": "Token ausente"}), 401
        try:
            user_id = validate_jwt_and_get_id(token, SECRET_KEY)
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Token inválido"}), 401
        return f(*args, **kwargs)
    return decorated