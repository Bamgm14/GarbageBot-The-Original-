import datetime as d
from selenium import webdriver
from bs4 import BeautifulSoup
import time as t
import urllib3
import User as u
import Birthday as b
import Internet as i
import Send as s
import BnT
flag=1
driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')
driver.maximize_window()
print('Please Scan the QR Code and press enter')
t.sleep(10)
while True:
    user=u.Users()
    if flag==1:
        calender=b.Refresh()
        flag=0
    register=driver.find_elements_by_class_name("OUeyt")
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
            name = driver.find_element_by_class_name("_16vzP").text
            message = driver.find_elements_by_class_name("vW7d1")[-1].text.lower()
            if 'garbage.exe' in message.lower():
                if name not in user:
                    u.ArriveUser(name,date)
                    textbox = driver.find_element_by_class_name("_2S1VP")
                    response='Hello, This Is Garbage, Thank You For Calling Me, '+name+'. If you need help, Say !help, If you want me to leave say bye garb and please no enter keys(\\n)\n'
                    textbox.send_keys(response)
                    pass
                elif name in user and 'false' in user[name].lower():
                    u.ArriveUser(name,date)
                    textbox = driver.find_element_by_class_name("_2S1VP")
                    response='Hello, This Is Garbage, Thank You For Calling Me Again, '+name+'. If you need help, Say !help, If you want me to leave say bye garb and please no enter keys(\\n)\n'
                    textbox.send_keys(response)
                    pass
                else:
                    textbox = driver.find_element_by_class_name("_2S1VP")
                    response='I am already here\n'
                    textbox.send_keys(response)
                    pass
            if name in user:
                assert '\n' in message, 'Please No \\n(Enter Key)'
                textbox = driver.find_element_by_class_name("_2S1VP")
                if '!help' in message.lower():
                    response='Commands:!yt <Item To Be Searched>,!Birthday <Name>,!AddBirthday <Name>:<Month>(mm)-<Day>(dd)(SideNote:for names with space, use "_"),!checkbirthday <optinal{(mm)-(dd)}[default is current date]>,!memes <optional[?top,?new,?contro,?rising,?hot]> <*Yes/*No(Defualt is No){Image Downloader}>,!pun <optional[?top,?new,?contro,?rising,?hot,?written]> <*Yes/*No(Defualt is No){Image Downloader}>,!showerthou <optional[?top,?new,?contro,?rising,?hot]>\n'
                    textbox.send_keys(response)
                    pass
                if '!birthday' in message.lower():#Need To Update
                    response=b.FindBirthday(message,date,calender)
                    textbox.send_keys(str(response+'\n'))
                    pass
                if '!addbirthday' in message.lower():#Need To Update
                    b.Newbirthday(message)
                    flag=1
                    response='Successful\n'
                    textbox.send_keys(response)
                    pass
                if '!checkbrithday' in message.lower():#Need To Update
                    b.CheckBirthday(message,date,calender)
                    pass
                if '!memes' in message:
                    response='One Minute\n'
                    textbox.send_keys(response)
                    if '*yes' in message:
                        image,title=i.rmemes(message)
                        s.send(driver,image,title)
                    else:
                        response=i.rmemes(message)
                        textbox.send_keys(response)
                        t.sleep(5)
                        textbox.send_keys('\n')
                    pass
                if '!pun' in message:
                    response='One Minute\n'
                    textbox.send_keys(response)
                    if '*yes' in message:
                        image,title=i.rpun(message)
                        s.send(driver,image,title)
                    else:
                        response=i.rpun(message)
                        textbox.send_keys(response)
                        t.sleep(5)
                        textbox.send_keys('\n') 
                    pass
                if '!yt' in message:
                    response='One Minute\n'
                    textbox.send_keys(response)
                    response=i.youtube(message)
                    textbox.send_keys(response)
                    t.sleep(5)
                    textbox.send_keys('\n')
                if '!showerthou' in message:
                    response='One Minute\n'
                    textbox.send_keys(response)
                    response=i.rshowert(message)
                    textbox.send_keys(response)
                    t.sleep(5)
                    textbox.send_keys('\n')
                    pass
                if '!bnt' in message:
                    BnT.Builder(int(message.split(' ')[2].split('\n')[0]),message.split(' ')[1].split(','))
                    import SnL
                    SnL.Loop(textbox,driver)
                    del SnL
                    pass
                if 'bye garb' in message.lower():
                    response='Goodbye\n'
                    textbox.send_keys(response)
                    u.LeaveUser(name,date)
                    pass
                if 'killswitch' in message.lower():
                    break
        except Exception as e:
            print (e)
            textbox = driver.find_element_by_class_name("_2S1VP")
            response=str(e)[0].upper()+str(e)[1:]+'\n'
            textbox.send_keys(response)
        t.sleep(1)
