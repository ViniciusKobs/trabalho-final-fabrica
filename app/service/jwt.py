import jwt
import time

def create_jwt_token(uid: int, secret: str) -> dict:
    issued_at = int(time.time())
    expires_at = issued_at + (2 * 60 * 60)
    payload = {
        "uid": uid,
        "iat": issued_at,
        "exp": expires_at,
    }
    return jwt.encode(payload, secret, algorithm='HS256')

def validate_jwt_and_get_id(jwt_token: str, secret: str) -> int:
    decoded = jwt.decode(jwt_token, secret,verify=True, algorithms=['HS256'])
    return int(decoded['uid'])