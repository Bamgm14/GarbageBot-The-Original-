import Blind as bd
import User as u
import Birthday as b
import Internet as i
import Interface as In
import Send as s
import BnT
import Group as g
#open('Help.txt','r').read()
from selenium.webdriver.common.keys import Keys
import time as t
blist=[]
grp={'!makeadmin':g.makeadmin,'*iam!special':g.special,'!amb':g.Addmeback,'!lmb':g.linkmeback}
bir={'!birthday':b.FindBirthday,'!addbirthday':b.Newbirthday,'!checkbirthday':b.CheckBirthday}
net={'!meme':i.rmemes,'!anattempt':i.ranattempt,'!pun':i.rpun,'!yt':i.youtube,'!showerthou':i.rshowert,'!physmeme':i.rphysmeme,'!chemmeme':i.rchemmeme,'!mathmeme':i.rmathmeme,'!compmeme':i.rcompmeme}
def Birth(driver,textbox,date,message,name):
    for x in list(bir.keys()):
        if x in message:
            res=bir[x](message,b.Refresh(),date)
            if name in blist:
                bd.blindmode(driver,res)
            for x in res.split('\n'):
                textbox.send_keys(x)
                textbox.send_keys(Keys.SHIFT+Keys.ENTER)
            textbox.send_keys('\n')
            pass
def Net(driver,textbox,message,name):
    for x in list(net.keys()):
        if x in message:
            response='One Minute\n'
            if name in blist:
                bd.blindmode(driver,response)
            textbox.send_keys(response)
            if ('*yes' in message):
                image,title=net[x](message)
                if image==None:
                    response="Image Doesn't Exist\n"
                    if name in blist:
                        bd.blindmode(driver,response)
                    textbox.send_keys(response)
                    if name in blist:
                        bd.blindmode(driver,title)
                    textbox.send_keys(title)
                    t.sleep(5)
                    textbox.send_keys('\n')
                    pass
                else:
                    s.send(driver,image,name,blist,title)
                    pass
            else:
                response=net[x](message)
                if name in blist:
                    bd.blindmode(driver,response)
                textbox.send_keys(response)
                t.sleep(5)
                textbox.send_keys('\n')
                pass
def BnTAndGbc(message,textbox,driver,name,date):
    if '!bnt' in message:
        assert int(message.split(' ')[2].split('\n')[0]) in [1,2,3,4],'Not Possible Level'
        BnT.Builder(int(message.split(' ')[2].split('\n')[0]),message.split(' ')[1].split(','))
        import SnL
        SnL.Loop(textbox,driver)
        del SnL
        pass
    if '!gbc' in message:
        res=b.g_check(g.HB(date,driver,name,textbox),b.Refresh())
        if name in blist:
            bd.blindmode(driver,res)
        for x in res.split('\n'):
            textbox.send_keys(x)
            textbox.send_keys(Keys.SHIFT+Keys.ENTER)
        textbox.send_keys('\n')
def Blindmode(driver,message,name):
    global blist
    if '!blindmode' in message:#Unstable
        if '*active' in message:
            if name in blist:
                bd.blindmode(driver,'I am already online')
            else:
                file=open('Blindindex.txt','a')
                file.write(name+'\n')
                file.close()
                bd.blindmode(driver,'Blindmode Online')
        elif '*deactive' in message:
            file=open('Blindindex.txt','r')
            blist=file.read().split('\n')
            file.close()
            while '' in blist:
                blist.remove('')
            if name in blist:
                blist.remove(name)
            file=open('Blindindex.txt','w')
            for x in blist:
                file.write(x+'\n')
            bd.blindmode(driver,'Blindmode Offline')
def Group(message,driver,textbox,name):
    for x in grp.keys():
        if x in message:
            grp[x](message,driver,textbox,name)
def Cri(message,driver,textbox,name):
    if '!cricket' in message:
        res=In.SInterface(message)
        if name in blist:
            bd.blindmode(driver,res)
        for x in res.split('\n'):
            textbox.send_keys(x)
            textbox.send_keys(Keys.SHIFT+Keys.ENTER)
        textbox.send_keys('\n')
