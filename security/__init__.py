import os
import webbrowser

import PySimpleGUI as sg

from config import params
from ui import popup
from . import encryption


def get_api_key():
    if os.path.exists(params.KEY_FILE):
        return encryption.decrypt_api_key()
    else:
        _show_api_disclaimer()
        try:
            api_key = _get_new_api_key()
            password = _get_new_password()
            encryption.encrypt_api_key(api_key, password)
        except ValueError:
            popup.CANCELLED_OPERATION()
            return None
        else:
            popup.WELCOME()
            return api_key


def _get_new_password():
    while True:
        password = popup.ENTER_NEW_PASSWORD()
        if password is None:
            raise ValueError
        confirm_password = popup.CONFIRM_NEW_PASSWORD()
        if confirm_password is None:
            raise ValueError
        typed = (password and confirm_password)
        matches = (password == confirm_password)
        valid = (len(password) >= 8)
        if typed and matches and valid:
            return password
        popup.PASSWORD_ERROR()


def _show_api_disclaimer():
    window = popup.API_DISCLAIMER()
    while True:
        event, values = window.read()
        if event in ['-CONTINUE-', sg.WIN_CLOSED]:
            window.close()
            break
        elif event == '-SITE-':
            webbrowser.open(params.OPENAI_API_SITE)


def _get_new_api_key():
    api_key = popup.ENTER_API_KEY()
    if api_key is None:
        raise ValueError
    while len(api_key) < 40:
        api_key = popup.INVALID_API_KEY()
        if api_key is None:
            raise ValueError
    return api_key
