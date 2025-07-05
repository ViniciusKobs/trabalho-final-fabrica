import hashlib
import hmac
import os

HASH_KEY = os.getenv('HASH_KEY')

def hash_password(password):
    hashed = hmac.new(HASH_KEY.encode(), password.encode(), hashlib.sha256)
    return hashed.hexdigest()

def validate_password_hash(hashed_pass, password):
    return hashed_pass == hash_password(password)