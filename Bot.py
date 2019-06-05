import datetime as d
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from bs4 import BeautifulSoup
import time as t
import urllib3
import Blind as bd
import User as u
import Birthday as b
import Internet as i
import Send as s
import BnT
import MA as m
nor={'!help':'Commands:\n!yt <Item To Be Searched>\n!Birthday <Name>\n!AddBirthday <Name>:<Year>(yyyy)-<Month>(mm)-<Day>(dd)(SideNote:for names with space, use "_")\n!checkbirthday ?<optinal{(mm)-(dd)}[default is current date]>\n!memes <optional[?top,?new,?contro,?rising,?hot]> <*Yes/*No(Defualt is No){Image Downloader}>\n!pun <optional[?top,?new,?contro,?rising,?hot,?written]> <*Yes/*No(Defualt is No){Image Downloader}>\n!showerthou <optional[?top,?new,?contro,?rising,?hot]>\n!anattempt <optional[?top,?new,?contro,?rising,?hot,?written]> <*Yes/*No(Defualt is No){Image Downloader}>\n!bnt <Name1,Name2,etc> <Level>','!birthday':b.FindBirthday,'!addbirthday':b.Newbirthday,'!checkbirthday':b.CheckBirthday}
net={'!memes':i.rmemes,'!anattempt':i.ranattempt,'!pun':i.rpun,'!yt':i.youtube,'!showerthou':i.rshowert}
driver = webdriver.Firefox()
driver.maximize_window()
blist=[]
driver.get('http://web.whatsapp.com')
print('Please Scan the QR Code')
t.sleep(10)
while True:
    user=u.Users()
    calender=b.Refresh()
    register=driver.find_elements_by_class_name("P6z4j")
    date=d.datetime.now().isoformat()
    if len(register) > 0:
        ele = register[-1]
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(ele, 0, -20)
        try:
            action.click()
            action.perform()
            action.click()
            action.perform()
        except Exception as e:
            pass
        try:
            name = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[2]/div[1]/div/span").text
            message = driver.find_elements_by_class_name("-N6Gq")[-1].text.lower()
            textbox = driver.find_element_by_xpath("/html/body/div/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
            if 'garbage.exe' in message.lower():
                if name not in user:
                    u.ArriveUser(name,date)
                    response='Hello, This Is Garbage, Thank You For Calling Me, '+name+'. If you need help, Say !help, If you want me to leave say bye garb and please no enter keys(\\n)\n'
                    textbox.send_keys(response)
                    pass
                elif name in user and 'false' in user[name].lower():
                    u.ArriveUser(name,date)
                    response='Hello, This Is Garbage, Thank You For Calling Me Again, '+name+'. If you need help, Say !help, If you want me to leave say bye garb and please no enter keys(\\n)\n'
                    textbox.send_keys(response)
                    pass
                else:
                    response='I am already here\n'
                    if name in blist:
                        bd.blindmode(driver,response)
                    textbox.send_keys(response)
                    pass
            if name in user:
                assert '\n' in message, 'Please No \\n(Enter Key)'
                for x in list(nor.keys()):
                    if x in message:
                        try:
                            res=nor[x](message,calender,date)
                        except:
                            res=nor[x]
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
                            response=listing[x](message)
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
                    res=b.g_check(b.HB(date,driver,name,textbox),calender)
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
                            blist.append(name)
                            bd.blindmode(driver,'Blindmode Online')
                    elif '*deactive' in message:
                        blist.remove(name)
                        bd.blindmode(driver,'Blindmode Offline')
                if '!makeadmin' in message:
                    m.makeadmin(driver,textbox,message,open('special.txt','r+').read().split('\n'),b.HB(date,driver,name,textbox))
                    pass
                if '*iam!special' in message:
                    m.special(name,message,textbox)
                    pass
                if 'bye garb' in message.lower():
                    response='Goodbye\n'
                    if name in blist:
                        bd.blindmode(driver,response)
                    textbox.send_keys(response)
                    u.LeaveUser(name,date)
                    pass
                if 'killswitch' in message.lower():
                    break
        except Exception as e:
            print (e)
            textbox = driver.find_element_by_xpath("/html/body/div/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
            response=str(e)[0].upper()+str(e)[1:]+'\n'
            if name in blist:
                bd.blindmode(driver,response)
            textbox.send_keys(response)
        t.sleep(1)
