import os

from config import params


def read_salt_file() -> bytes:
    with open(params.SALT_FILE, 'rb') as f:
        return f.read()


def write_salt_file() -> bytes:
    salt = os.urandom(16)
    with open(params.SALT_FILE, 'wb') as f:
        f.write(salt)
    return salt


def read_key_file() -> bytes:
    with open(params.KEY_FILE, 'rb') as f:
        return f.read()


def write_key_file(encrypted_data: bytes) -> None:
    with open(params.KEY_FILE, 'wb') as f:
        f.write(encrypted_data)


def clear_stored_keys():
    os.remove(params.KEY_FILE)
    os.remove(params.SALT_FILE)
