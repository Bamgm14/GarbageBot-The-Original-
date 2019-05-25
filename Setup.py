import os
import platform
Frame=platform.architecture()[0]
lib=['selenium','bs4','urllib3','matplotlib','numpy','requests']
for x in lib:
    os.system('python3 -m pip install '+str(x)+' || python -m pip install '+str(x))
import requests as r
if '64' in Frame:
    Excutable=r.get('https://eternallybored.org/misc/wget/1.20.3/64/wget.exe')
    a=open('wget.exe','wb')
    a.write(Excutable.content)
    a.close()
else:
    Excutable=r.get('https://eternallybored.org/misc/wget/1.20.3/32/wget.exe')
    a=open('wget.exe','wb')
    a.write(Excutable.content)
    a.close()
