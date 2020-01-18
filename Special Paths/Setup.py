import os
import zipfile as z
lib=['pycricbuzz','selenium','bs4','urllib3','matplotlib','numpy','requests','gtts','matplotlib','chatterbot','chatterbot-corpus','names_dataset']
Execute=['https://eternallybored.org/misc/wget/1.20.3/32/wget.exe','https://youtube-dl.org/downloads/latest/youtube-dl.exe','https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_win32.zip','https://www.7-zip.org/a/7zr.exe','https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-win32.zip',]
for x in lib:
    os.system('python3 -m pip install '+str(x)+' --user || python -m pip install '+str(x)+' --user')
import requests as r

for x in Execute:
    WExcutable=r.get(x)
    with open(x.split('/')[x.split('/')-1],'wb') as a:
        a.write(WExcutable.content)
#os.system('setx path "%path%";'+os.getcwd()+'')
for x in os.listdir():
    if os.path.endswith(".zip"):
        with z.ZipFile(os.getcwd()+"\\"+str(x), 'r') as zip_ref:
            zip_ref.extractall(os.getcwd())
