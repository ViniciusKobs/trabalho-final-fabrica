import jwt
import time

SECRET = os.getenv('HASH_KEY')

def create_jwt_token(uid: int) -> dict:
    issued_at = int(time.time())
    expires_at = issued_at + (2 * 60 * 60)
    payload = {
        "uid": uid,
        "iat": issued_at,
        "exp": expires_at,
    }
    return jwt.encode(payload, SECRET, algorithm='HS256')

def validate_jwt_and_get_id(jwt_token: str) -> int:
    decoded = jwt.decode(jwt_token, SECRET,verify=True, algorithms=['HS256'])
    return int(decoded['uid'])