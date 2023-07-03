from concurrent.futures import Future

import requests
import zipfile
import os
import shutil

from ui import popup


def ffmpeg_binary():
    url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
    local_filename = "ffmpeg-master-latest-win64-gpl.zip"

    response = requests.get(url, stream=True)

    with open(local_filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    zip_filename = local_filename
    extracted_file_path = "ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe"
    destination_folder = "."

    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extract(extracted_file_path, destination_folder)

    os.rename(os.path.join(destination_folder, extracted_file_path), os.path.join(destination_folder, 'ffmpeg.exe'))

    os.remove(zip_filename)
    shutil.rmtree(os.path.join(destination_folder, 'ffmpeg-master-latest-win64-gpl'))


def show_task(task: Future[str]):
    window = popup.DOWNLOADING_FILE()
    i = 0
    while task.running():
        window.read(timeout=10)
        window['-DOWNLOADING-'].update(current_count=i)
        if i < 1000:
            i += 10
        else:
            i = 0
    window.close()
