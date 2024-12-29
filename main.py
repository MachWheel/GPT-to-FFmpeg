import importlib.util
import os
import sys
import threading

import PySimpleGUI as sg  # noqa
import openai

import config
import core
import security
import ui
from ui import popup


def main(api_key: str):
    openai.api_key = api_key
    window = sg.Window(config.txt.APP_NAME, ui.layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        elif event == "-RUN-":
            input_file = values["-FILEPATH-"]
            if not input_file:
                popup.INPUT_FILE_NEEDED_ERROR()
                continue
            prompt = values["-PROMPT-"]
            if not prompt:
                popup.PROMPT_NEEDED_ERROR()
                continue
            ffmpeg_command = core.request_gpt_cmd(prompt, input_file)
            if not ffmpeg_command:
                continue
            config.update_prompt_history(prompt)
            config.update_ffmpeg_history(ffmpeg_command)
            if values.get('-HISTORY-'):
                ui.update_history_combo(window)
            if popup.CMD_WARNING(ffmpeg_command) == "Yes":
                threading.Thread(
                    target=core.run_ffmpeg,
                    args=(ffmpeg_command, window),
                    daemon=True
                ).start()

        elif event == "-VOICE-":
            core.get_voice_input(window)

        elif event == "-HISTORY-":
            window['-PROMPT-'].update(values['-HISTORY-'])

        elif event == "-FILEPATH-":
            filename = values['-FILEPATH-'].split('/')[-1]
            if filename:
                window['-SELECTED-'].update(filename)

        elif event == '-THREAD-':
            window['-PROGRESS-'].UpdateBar(values['-THREAD-'])

        elif event == '-DONE-':
            popup.EXPORTED_SUCCESS()
            os.startfile(os.path.dirname(values["-FILEPATH-"]))
            window['-PROGRESS-'].update_bar(0)

    window.close()


def close_splash():
    """
    Closes the application loading splash screen.
    """
    if '_PYIBoot_SPLASH' in os.environ:
        if not importlib.util.find_spec("pyi_splash"):
            return
        import pyi_splash
        pyi_splash.close()


if __name__ == "__main__":
    close_splash()
    if not config.existing_ffmpeg_binary():
        config.get_ffmpeg_binary()
    openai_key = security.get_environment_api_key()
    if not openai_key:
        openai_key = security.get_api_key()
    if not openai_key:
        sys.exit(0)
    main(openai_key)
