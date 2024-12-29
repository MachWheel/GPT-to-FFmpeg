import base64

import PySimpleGUI as sg  # noqa
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from ui import popup
from . import storage


def _derive_key(password, salt):
    password = password.encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key


def encrypt_api_key(api_key: str, password: str):
    salt = storage.write_salt_file()
    derived_key = _derive_key(password, salt)
    fernet = Fernet(derived_key)
    encrypted_data = fernet.encrypt(api_key.encode())
    storage.write_key_file(encrypted_data)


def decrypt_api_key() -> str | None:
    attempts = 0
    while attempts < 3:
        password = popup.ENTER_PASSWORD()
        if not password:
            return None
        salt = storage.read_salt_file()
        derived_key = _derive_key(password, salt)
        try:
            data = storage.read_key_file()
            fernet = Fernet(derived_key)
            decrypted_data = fernet.decrypt(data)
            api_key = decrypted_data.decode()
            ask_remember_password(password)
            return api_key
        except InvalidToken:
            popup.INCORRECT_PASSWORD_ERROR()
            attempts += 1
    popup.PASSWORD_LIMIT_ERROR()
    storage.clear_stored_keys()
    return None


def ask_remember_password(password: str):
    if sg.user_settings_get_entry('-APP_PASSWORD-') is None:
        if popup.REMEMBER_PASSWORD() == 'Yes':
            sg.user_settings_set_entry('-APP_PASSWORD-', password)
