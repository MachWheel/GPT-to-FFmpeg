import PySimpleGUI as sg  # noqa

from config import params, txt

sg.theme(params.SG_THEME)


def create_history_combo():
    try:
        with open(params.PROMPT_HISTORY_FILE, 'r', encoding='utf-8') as file:
            log_lines = file.readlines()
        listbox_entries = list({line.strip() for line in log_lines})
        return [
            sg.Combo(
                values=listbox_entries,
                default_value=txt.VIEW_HISTORY,
                size=55,
                k="-HISTORY-",
                background_color=sg.theme_background_color(),
                enable_events=True,
                readonly=True
            )
        ]
    except FileNotFoundError:
        return []


def update_history_combo(window: sg.Window):
    try:
        with open(params.PROMPT_HISTORY_FILE, 'r', encoding='utf-8') as file:
            log_lines = file.readlines()
        listbox_entries = list({line.strip() for line in log_lines})
        window['-HISTORY-'].update(value=txt.VIEW_HISTORY, values=listbox_entries)
    except FileNotFoundError:
        return


def layout(openai_model: str):
    return [
        [sg.P(), sg.Text(txt.APP_NAME, font="Default 15 bold", p=((5, 5), (5, 0))), sg.P()],
        [sg.HSep(p=((5, 5), (5, 25)))],
        [
            sg.Text(txt.FILE_BROWSE_TEXT, font="Default 10 bold"),
            sg.P(),
            sg.FileBrowse(txt.FILE_BROWSE_BUTTON, k="-BROWSE-", s=14, target="-FILEPATH-", p=(7, 3))
        ],
        [sg.Input(s=57, k="-FILEPATH-", enable_events=True)],
        [sg.P(), sg.Text(txt.NO_SELECTED_FILE, font="Default 10 bold", k='-SELECTED-', text_color="khaki"), sg.P()],
        [sg.HSep(p=(5, 10))],
        [
            sg.Text(txt.CONVERT_PROMPT_TEXT, font="Default 10 bold", p=((5, 5), (15, 5))),
            sg.P(),
        ],
        [create_history_combo()],
        [sg.Multiline(size=(50, 4), no_scrollbar=True, font="Arial 11 bold",
                      k="-PROMPT-", background_color='khaki', text_color='black')],
        [sg.P(), sg.Button(txt.VOICE_COMMAND, s=49, k="-VOICE-"), sg.P()],
        [sg.HSep(p=(5, 10))],
        [sg.P(), sg.Text(txt.FOOTER_NOTE, font="Default 10 italic", text_color='khaki'), sg.P()],
        [sg.HSep(p=(5, 10))],
        [
            sg.P(),
            sg.Button(f"{txt.EXECUTE_TEXT} {openai_model}", s=49, font="Default 10 bold", k="-RUN-",
                      button_color=("white", "SeaGreen4"),
                      p=((5, 5), (5, 10))),
            sg.P(),
        ],
        [sg.ProgressBar(100, orientation='h', size=(31, 15), bar_color=("MediumSpringGreen", "gray"), key='-PROGRESS-')]
    ]
