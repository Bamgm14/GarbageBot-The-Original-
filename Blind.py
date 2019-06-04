from gtts import gTTS as g
import Send as s
import os
def blindmode(driver,info):
    a=g(info)
    a.save(os.getcwd()+'\\Blind\\'+info[:5]+'.mp3')
    s.send(driver,os.getcwd()+'\\Blind\\'+info[:5]+'.mp3')
    
