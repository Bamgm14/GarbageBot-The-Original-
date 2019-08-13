import Modules.Blind as bd
import Modules.Birthday as b
import Modules.Internet as i
import Modules.Interface as In
import Modules.Send as s
import Modules.BnT as BnT
import Modules.Group as g
import Modules.ChatMode as cm
import Modules.JCInterface as jc
from selenium.webdriver.common.keys import Keys
import time as t
import chatterbot
from chatterbot.comparisons import *
from chatterbot.response_selection import *
from chatterbot import ChatBot
chatbot=ChatBot('Garb',
    preprocessors=['chatterbot.preprocessors.clean_whitespace','chatterbot.preprocessors.convert_to_ascii'],
    logic_adapters=[{"import_path": "chatterbot.logic.BestMatch","statement_comparison_function": synset_distance,"response_selection_method": get_first_response,'default_response': 'I am sorry, but I do not understand.','maximum_similarity_threshold': 0.95},
                    {'import_path': 'chatterbot.logic.SpecificResponseAdapter','input_text': 'bye garb','output_text': ''},
                    {'import_path': 'chatterbot.logic.MathematicalEvaluation'}]
                )
blist=[]
JC=['!rtrans','!strans','!bankbal']
grp={'!makeadmin':g.makeadmin,'*iam!special':g.special,'!amb':g.Addmeback,'!lmb':g.linkmeback}
bir={'!birthday':b.FindBirthday,'!addbirthday':b.Newbirthday,'!checkbirthday':b.CheckBirthday}
net={'!meme':i.rmemes,'!anattempt':i.ranattempt,'!pun':i.rpun,'!yt':i.youtube,'!showerthou':i.rshowert,'!physmeme':i.rphysmeme,'!chemmeme':i.rchemmeme,'!mathmeme':i.rmathmeme,'!compmeme':i.rcompmeme}
def Commands(driver,textbox,date,message,name,UserName):
    global blist
    for x in JC:
        if x in message:
            res=jc.Spliter(message)
            if name in blist:
                bd.blindmode(driver,res)
            for x in res.split('\n'):
                textbox.send_keys(x)
                textbox.send_keys(Keys.SHIFT+Keys.ENTER)
            textbox.send_keys('\n')
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
    if '!blindmode' in message:
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
    for x in grp.keys():
        if x in message:
            grp[x](message,driver,textbox,name)
    if '!cricket' in message:
        res=In.SInterface(message)
        if name in blist:
            bd.blindmode(driver,res)
        for x in res.split('\n'):
            textbox.send_keys(x)
            textbox.send_keys(Keys.SHIFT+Keys.ENTER)
        textbox.send_keys('\n')
    if name in cm.Chatmde:
        response=cm.Chatmode(chatbot,UserName,message)
        if response:
            for x in response.split('\n'):
                textbox.send_keys(x)
                textbox.send_keys(Keys.SHIFT+Keys.ENTER)
            textbox.send_keys('\n')
    if '!chat' in message:
        if 'true' in message:
            cm.Chatmde.append(name)
        elif 'false' in message:
            try:
                while name in cm.Chatmde:
                    cm.Chatmde.remove(name)
            except:
                pass
