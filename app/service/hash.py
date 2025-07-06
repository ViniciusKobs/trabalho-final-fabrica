from hashlib import sha256
from hmac import new
from os import getenv

HASH_KEY = getenv('HASH_KEY')

def hash_password(password):
    hashed = new(HASH_KEY.encode(), password.encode(), sha256)
    return hashed.hexdigest()

def validate_password_hash(hashed_pass, password):
    return hashed_pass == hash_password(password)