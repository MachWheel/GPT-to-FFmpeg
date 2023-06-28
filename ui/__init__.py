import PySimpleGUI as sg

from config import params, txt

sg.theme(params.SG_THEME)

layout = [
    [sg.P(), sg.Text(txt.APP_NAME, font="Default 15 bold", p=((5, 5), (5, 15))), sg.P()],

    [
        sg.Text(txt.FILE_BROWSE_TEXT, font="Default 10 bold"),
        sg.P(),
        sg.FileBrowse(txt.FILE_BROWSE_BUTTON, k="-BROWSE-", s=12, target="-FILEPATH-", p=(7, 3))
    ],
    [sg.Input(s=57, k="-FILEPATH-")],

    [sg.Text(txt.CONVERT_PROMPT_TEXT, font="Default 10 bold", p=((5, 5), (15, 5)))],
    [sg.Multiline(size=(50, 6), no_scrollbar=True, font="Arial 11 bold", k="-PROMPT-")],
    [
        sg.Button(txt.VOICE_COMMAND, s=25, k="-VOICE-"),
        sg.P(),
        sg.Button(txt.EXECUTE_TEXT, s=15, font="Default 10 bold", k="-RUN-", button_color="darkgreen")
    ],

    [sg.P(), sg.Text(txt.FOOTER_NOTE, font="Default 10 italic"), sg.P()],
    [sg.ProgressBar(100, orientation='h', size=(31, 20), bar_color=("lightgreen", "gray"), key='-PROGRESS-')]
]
