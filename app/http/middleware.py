import jwt
from flask import request, jsonify
from functools import wraps
from app.service.jwt_service import validateJwtAndGetId

def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        if not token:
            return jsonify({"error": "error.token.missing"}), 401

        try:
            user_id = validateJwtAndGetId(token)
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "error.token.expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "error.token.invalid"}), 401
        return f(*args, **kwargs)
    return decorated