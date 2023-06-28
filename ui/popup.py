import PySimpleGUI as sg

from config import txt


def NO_MIC_ERROR():
    return sg.popup(
        txt.NO_MIC_ERROR,
        no_titlebar=True,
        keep_on_top=True,
        font="Default 12",
        background_color="black"
    )


def WAIT_TIMEOUT_ERROR():
    return sg.popup(
        txt.WAIT_TIMEOUT_ERROR,
        no_titlebar=True,
        keep_on_top=True,
        font="Default 12",
        background_color="black"
    )


def LISTENING_ERROR():
    return sg.popup(
        txt.LISTENING_ERROR,
        no_titlebar=True,
        keep_on_top=True,
        font="Default 12",
        background_color="black"
    )


def LISTENING_REQUEST_ERROR(error):
    return sg.popup(
        txt.LISTENING_REQUEST_ERROR.format(error),
        no_titlebar=True,
        keep_on_top=True,
        font="Default 12",
        background_color="black"
    )


def GPT_UNAVAILABLE_ERROR():
    return sg.popup(
        txt.GPT_UNAVAILABLE_ERROR,
        no_titlebar=True,
        keep_on_top=True,
        font="Default 12",
        background_color="black"
    )


def GPT_AUTH_ERROR():
    return sg.popup(
        txt.GPT_AUTH_ERROR,
        no_titlebar=True,
        keep_on_top=True,
        font="Default 12",
        background_color="black"
    )


def LISTENING_VOICE():
    return sg.Window(
        "",
        [
            [sg.P(), sg.T(txt.LISTENING_VOICE, font="Default 14 bold"), sg.P()],
            [sg.ProgressBar(700, s=(32, 20), key="-LISTENING-")]
        ],
        no_titlebar=True,
        keep_on_top=True
    )


def ENTER_NEW_PASSWORD():
    return sg.popup_get_text(
        txt.ENTER_NEW_PASSWORD,
        password_char='*',
        no_titlebar=True,
        keep_on_top=True,
        font="Default 12",
    )


def CONFIRM_NEW_PASSWORD():
    return sg.popup_get_text(
        txt.CONFIRM_NEW_PASSWORD,
        password_char='*',
        no_titlebar=True,
        keep_on_top=True,
        font="Default 12",
    )


def ENTER_PASSWORD():
    return sg.popup_get_text(
        txt.ENTER_PASSWORD,
        password_char='*',
        no_titlebar=True,
        keep_on_top=True,
        font="Default 12",
    )


def INCORRECT_PASSWORD_ERROR():
    return sg.popup(
        txt.INCORRECT_PASSWORD_ERROR,
        no_titlebar=True,
        keep_on_top=True,
        font="Default 12",
        background_color="black"
    )


def PASSWORD_LIMIT_ERROR():
    return sg.popup(
        txt.PASSWORD_LIMIT_ERROR,
        no_titlebar=True,
        keep_on_top=True,
        font="Default 12",
        background_color="black"
    )


def PASSWORD_ERROR():
    return sg.popup(
        txt.PASSWORD_ERROR,
        no_titlebar=True,
        keep_on_top=True,
        font="Default 12",
        background_color="black"
    )


def API_DISCLAIMER():
    layout = [
        [sg.T(txt.API_DISCLAIMER)],
        [
            sg.B(txt.CONTINUE, k="-CONTINUE-", font="Default 12 bold"),
            sg.B(txt.GO_TO_SITE, k="-SITE-")
        ]
    ]
    return sg.Window(txt.APP_NAME, layout, font="Default 12")


def ENTER_API_KEY():
    return sg.popup_get_text(
        txt.ENTER_API_KEY,
        txt.APP_NAME,
        font="Default 12"
    )


def INVALID_API_KEY():
    return sg.popup_get_text(
        txt.INVALID_API_KEY,
        txt.APP_NAME,
        font="Default 12",
    )


def CANCELLED_OPERATION():
    return sg.popup(
        txt.CANCELLED_OPERATION,
        no_titlebar=True,
        keep_on_top=True,
        font="Default 12",
        background_color="black"
    )


def WELCOME():
    return sg.popup(
        txt.WELCOME,
        no_titlebar=True,
        keep_on_top=True,
        font="Default 12"
    )


def INPUT_FILE_NEEDED_ERROR():
    return sg.popup(
        txt.INPUT_FILE_NEEDED_ERROR,
        no_titlebar=True,
        keep_on_top=True,
        font="Default 12",
        background_color="black"
    )


def PROMPT_NEEDED_ERROR():
    return sg.popup(
        txt.PROMPT_NEEDED_ERROR,
        no_titlebar=True,
        keep_on_top=True,
        font="Default 12",
        background_color="black"
    )


def CMD_WARNING(ffmpeg_command):
    return sg.popup_yes_no(
        txt.CMD_WARNING(ffmpeg_command),
        no_titlebar=True,
        keep_on_top=True,
        font="Default 12",
        background_color="black"
    )


def EXPORTED_SUCCESS():
    return sg.popup(
        "",
        txt.EXPORTED_SUCCESS_MSG,
        font="Default 12 bold",
        no_titlebar=True,
        background_color="lightgray",
        custom_text=txt.EXPORTED_SUCCESS_BTN,
        text_color="black"
    )
