import hashlib
import base64
import os

def add_user(data, name, password):
    if name in data:
        return False
    data[name] = hash_password(password)
    return True

def hash_password(password: str) -> str:
    salt = os.urandom(16)

    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100_000
    )

    return base64.b64encode(salt + key).decode('utf-8')


def check_password(stored_hash: str, entered: str) -> bool:
    raw = base64.b64decode(stored_hash.encode('utf-8'))
    salt = raw[:16]
    old_key = raw[16:]

    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        entered.encode('utf-8'),
        salt,
        100_000
    )

    return new_key == old_key