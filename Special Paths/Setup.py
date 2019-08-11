import os
lib=['pycricbuzz','selenium','bs4','urllib3','matplotlib','numpy','requests','gtts','matplotlib','numpy','chatterbot','chatterbot-corpus']
Execute=['https://youtube-dl.org/downloads/latest/youtube-dl.exe','https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_win32.zip','https://www.7-zip.org/a/7zr.exe','https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-win32.zip',]
for x in lib:
    os.system('python3 -m pip install '+str(x)+' --user|| python -m pip install '+str(x)+' --user')
import requests as r
WExcutable=r.get('https://eternallybored.org/misc/wget/1.20.3/32/wget.exe')
a=open('wget.exe','wb')
a.write(WExcutable.content)
a.close()
for x in Execute:
    os.system('wget "'+x+'"')
os.system('setx path "%path%";'+os.getcwd()+'')
for x in os.listdir():
    if '.zip' in x:
        os.system('7zr x '+x)
