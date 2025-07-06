from os import getenv
from time import time
import jwt

SECRET = getenv('HASH_KEY')

def createJwtToken(uid):
    issued_at = int(time())
    expires_at = issued_at + (24 * 60 * 60)
    payload = {
        "uid": uid,
        "iat": issued_at,
        "exp": expires_at,
    }
    return jwt.encode(payload, SECRET, algorithm='HS256')

def validateJwtAndGetId(jwt_token):
    return jwt.decode(jwt_token, SECRET, verify=True, algorithms=['HS256'])