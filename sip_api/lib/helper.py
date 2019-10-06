import secrets

import bcrypt


def hash_password(pw):
    pw_hash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
    return pw_hash.decode('utf8')


def generate_token():
    return secrets.token_hex(32)
