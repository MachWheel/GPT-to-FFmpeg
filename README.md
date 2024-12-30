# How to use another OpenAI model:
In the `GPT-to-FFmpeg.exe` folder, create or edit a text file called `openai-model.cfg` with the model you want to use and nothing else. 

### A custom `openai-model.cfg` file:
```
gpt-4o-mini-2024-07-18
``` 
  - Result: will use the `gpt-4o-mini-2024-07-18` model to write the FFmpeg commands. 


# How to clone and run the project:

1. First, open the command-line and check your Python version. This app was made using **Python 3.12.0**:
```
py --version
```

2. Now, install virtualenv if you don't have it:
``` 
py -m pip install virtualenv
```

3. Clone the repository and change the directory to it:
```    
git clone https://github.com/MachWheel/GPT-to-FFmpeg.git
```

```
cd GPT-to-FFmpeg
```


4. Create a virtualenv for the project, then activate it:
```
py -m venv venv
```

```
.\venv\Scripts\activate
```


5. Install project dependencies:
```
py -m pip install -r requirements.txt
```

6. Done. Now you can run the app typing:
```
py main.py
```


# How to make the portable `.exe` file:
```
pyinstaller -w --onefile main.py --icon app.ico --name GPT-to-FFmpeg --splash splash.png
```
