from gtts import gTTS as g
import Send as s
import os
import time as t
def blindmode(driver,info):
    a=g(info)
    a.save(os.getcwd()+'\\Blind\\'+info[:5]+'.mp3')
    t.sleep(1.5)
    s.send(driver,os.getcwd()+'\\Blind\\'+info[:5]+'.mp3')
    
