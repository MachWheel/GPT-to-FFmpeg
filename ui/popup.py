import PySimpleGUI as sg  # noqa

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
            [sg.ProgressBar(1500, s=(32, 20), key="-LISTENING-")]
        ],
        no_titlebar=True,
        keep_on_top=True
    )


def DOWNLOADING_FILE():
    return sg.Window(
        "",
        [
            [sg.P(), sg.T(txt.DOWNLOADING_FFMPEG, font="Default 14 bold"), sg.P()],
            [sg.ProgressBar(1000, s=(32, 20), key="-DOWNLOADING-")]
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
        default_text=sg.user_settings_get_entry('-APP_PASSWORD-', ''),
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
        [sg.P(), sg.B(txt.GO_TO_SITE, k="-SITE-"), sg.P()],
        [sg.P(), sg.B(txt.STORE_KEY_LOCALLY, k="-CONTINUE-", font="Default 12 bold"), sg.P()],
        [sg.P(), sg.B(txt.QUIT, k="-QUIT-"), sg.P()],
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


def REMEMBER_PASSWORD():
    return sg.popup_yes_no(
        txt.REMEMBER_PASSWORD,
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
