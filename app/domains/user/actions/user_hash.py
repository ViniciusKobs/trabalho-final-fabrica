import hashlib
import hmac

def hash_pass(key: str, password: str) -> str:
    hashed = hmac.new(key.encode(), password.encode(), hashlib.sha256)
    return hashed.hexdigest()

def validate_pass(key: str, hashed_pass: str, password: str) -> bool:
    return hashed_pass == hash_pass(key, password)