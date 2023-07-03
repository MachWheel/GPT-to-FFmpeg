APP_NAME = "GPT to FFmpeg"
INPUT_FILE_NEEDED_ERROR = "You need to select an input file first"
PROMPT_NEEDED_ERROR = 'Write how you want to convert or modify the file first\n\nExample:\n"I want only the audio from this video in .mp3 format"'
NO_MIC_ERROR = "It seems that there is no default microphone selected on your computer."
LISTENING_ERROR = 'I couldn\'t understand what you said.'
WAIT_TIMEOUT_ERROR = 'I didn\'t hear what you said.'
LISTENING_REQUEST_ERROR = 'Sorry, I am unable to recognize your voice at the moment.; {0}'
LISTENING_VOICE = 'Speak out what you need...'
DOWNLOADING_FFMPEG = 'Downloading ffmpeg...'
GPT_REQUEST_PROMPT = "You are part of a Python script that allows audio and video conversions using ffmpeg on Windows.\n\
Attention: Your response will be DIRECTLY executed as an ffmpeg command in a Windows terminal using Python's 'subprocess.Popen'.\n\
Therefore, regardless of what the user requests, your response should STRICTLY CONTAIN ONLY THE COMMAND AND NOTHING ELSE!\n\
With that in mind, this is the user's request:\n\n\
{prompt}\n\
The file that will be used is as follows:\n\
\"{input_file}\"\n\
The output file should be generated in the same directory as the input file, with the prefix \"gpt_\" in its name."
GPT_UNAVAILABLE_ERROR = "OpenAI service overloaded or unavailable at the moment"
GPT_AUTH_ERROR = "Authentication Error:\nThe saved API key is invalid and will be deleted.\nThe program will be terminated."
FILE_BROWSE_TEXT = "1. Select the input file:"
FILE_BROWSE_BUTTON = "Browse file..."
CONVERT_PROMPT_TEXT = "2. Write how you want to convert or modify the file:"
VIEW_HISTORY = "...or select from your history"
VOICE_COMMAND = "Write with my voice"
EXECUTE_TEXT = "Start"
NO_SELECTED_FILE = "No input file selected yet"
FOOTER_NOTE = 'The file is exported in the same directory as the input file,\nwith the prefix "gpt_" in its name'
EXPORTED_SUCCESS_MSG = '\nYour file has been successfully generated!\nThe folder with the generated file will be opened.\n'
EXPORTED_SUCCESS_BTN = 'Open folder'
ENTER_PASSWORD = f'Enter your password to open {APP_NAME}'
WELCOME = '\nWelcome\n'
INCORRECT_PASSWORD_ERROR = 'Incorrect password. Please try again.'
ENTER_NEW_PASSWORD = 'Enter a new password (at least 8 characters)'
CONFIRM_NEW_PASSWORD = 'Confirm your password'
PASSWORD_ERROR = 'Passwords do not match or are less than 8 characters. Please try again.'
API_DISCLAIMER = "\nAn OpenAI API key is required for this program to work\n\n\
You will set a password to protect access to your key\n\n\
This password will be required every time you open the program\n\n\
If you forget this password, you will need to:\n\
- Generate a new API key\n\
- Set a new password\n\n"
CONTINUE = 'Continue'
GO_TO_SITE = 'Go to "API keys" page on the OpenAI website'
ENTER_API_KEY = 'Enter your OpenAI API key'
REMEMBER_PASSWORD = "Do you want to remember your password for the next access?"
INVALID_API_KEY = 'Invalid API key format\nPlease enter your OpenAI API key'
PASSWORD_LIMIT_ERROR = 'Attempt limit exceeded.\n\
For security reasons, the saved API key will be deleted.\n\n\
Next time you open this program, you will need to:\n\
- Generate and save a new API key\n\
- Set a new password for the program'
CANCELLED_OPERATION = "Operation cancelled"


def CMD_WARNING(command: str):
    return (
        f"WARNING!\n"
        f"THIS COMMAND WILL BE EXECUTED IN YOUR TERMINAL:\n\n"
        f"{command}\n\n"
        f"Do you want to continue?"
    )
