from concurrent.futures import Future

import PySimpleGUI as sg
import speech_recognition as sr

from config import params
from ui import popup


def listen() -> str | None:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, timeout=3, phrase_time_limit=5)
        return r.recognize_google(audio, language='pt-BR')


def show_listening(task: Future[str]):
    sg.theme(params.LIGHT_SG_THEME)
    window = popup.LISTENING_VOICE()
    i = 0
    while task.running():
        window.read(timeout=10)
        window['-LISTENING-'].update(current_count=i)
        i += 1
    window.close()
    sg.theme(params.SG_THEME)
