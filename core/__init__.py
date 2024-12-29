import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

import PySimpleGUI as sg  # noqa
import openai
import speech_recognition as sr

from config import txt
from security.storage import clear_stored_keys
from ui import popup
from . import voice


def get_voice_input(window: sg.Window):
    try:
        with ThreadPoolExecutor() as executor:
            listening_task = executor.submit(voice.listen)
            voice.show_listening(listening_task)
            heard = listening_task.result()
            if heard:
                window["-PROMPT-"].update(listening_task.result())
    except OSError:
        popup.NO_MIC_ERROR()
    except sr.exceptions.WaitTimeoutError:
        popup.WAIT_TIMEOUT_ERROR()
    except sr.UnknownValueError:
        popup.LISTENING_ERROR()
    except sr.RequestError as e:
        popup.LISTENING_REQUEST_ERROR(e)


def request_gpt_cmd(prompt, input_file) -> str:
    model = _get_openai_model_cfg()
    try:
        chat_completion = openai.ChatCompletion.create(
            model=model,
            messages=[{
                "role": "user",
                "content": txt.GPT_REQUEST_PROMPT.format(
                    prompt=prompt,
                    input_file=input_file
                )
            }]
        )
        return chat_completion.choices[0].message['content'].strip()
    except openai.error.ServiceUnavailableError:
        popup.GPT_UNAVAILABLE_ERROR()
    except openai.error.AuthenticationError:
        popup.GPT_AUTH_ERROR()
        clear_stored_keys()
        exit()


def run_ffmpeg(command, window):
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        encoding='ISO-8859-1'
    )
    duration = None
    while True:
        line = process.stdout.readline().strip()
        if line == '' and process.poll() is not None:
            break
        if "Duration" in line:
            h, m, s = line.split("Duration:")[1].split(",")[0].strip().split(':')
            duration = int(h) * 3600 + int(m) * 60 + float(s)
        if "time=" in line and duration is not None:
            h, m, s = line.split("time=")[1].split(" ")[0].split(':')
            elapsed_time = int(h) * 3600 + int(m) * 60 + float(s)
            window.write_event_value('-THREAD-', elapsed_time * 100 / duration)
    if process.returncode == 0 and duration is not None:
        window.write_event_value('-DONE-', '')


def _get_openai_model_cfg():
    """
    Returns the contents of the 'openai-model.cfg' file.
    If the file doesn't exist, creates it with the line 'o1-mini' and returns that line.
    """
    filename = "openai-model.cfg"
    default_model = "o1-mini"
    if not os.path.exists(filename):
        with open(filename, "wt") as file:
            file.write(default_model)
        return default_model

    with open(filename, "rt") as file:
        return file.read().strip()
