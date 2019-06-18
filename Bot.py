import datetime as d
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time as t
import User as u
import Commands as cmd
hlp=open('Help.txt','r').read()
driver = webdriver.Firefox()
driver.maximize_window()
blist=[]
driver.get('http://web.whatsapp.com')
print('Please Scan the QR Code')
t.sleep(1)
msgstoragemode=input('Do You Want To Store All Incoming Messages?[Y/N](Only If You Have Good Storage):')
gd,nme,msg,tbx,qt,down=("P6z4j","/html/body/div[1]/div/div/div[4]/div/header/div[2]/div[1]/div/span","-N6Gq","/html/body/div/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]",'qfKkX','/html/body/div[1]/div/div/div[4]/div/div[3]/div/span[2]/div/span[2]')
while True:
    try:
        user=u.Users()
        calender=b.Refresh()
        register=driver.find_elements_by_class_name(gd)
        date=d.datetime.now().isoformat()
        try:
            driver.find_element_by_xpath(down).click()
        except:
            pass
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
                name = driver.find_element_by_xpath(nme).text
                message = driver.find_elements_by_class_name(msg)[-1].text.lower()
                if msgstoragemode.lower()=='y':
                    a=open('MessageHistory','a')
                    a.write(name+':'+message+'\n')
                    a.close()
                textbox = driver.find_element_by_xpath(tbx)
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
                if (name in user) and ('true' in user[name].lower()):
                    assert '\n' in message, 'Please No \\n(Enter Key)'
                    if '!help' in message:
                        res=hlp
                        if name in blist:
                            bd.blindmode(driver,res)
                        for x in res.split('\n'):
                            textbox.send_keys(x)
                            textbox.send_keys(Keys.SHIFT+Keys.ENTER)
                        textbox.send_keys('\n')
                    cmd.Birth(driver,textbox,date,message,name)
                    cmd.Net(driver,textbox,message,name)
                    cmd.Group(message,driver,textbox,name)
                    cmd.Cri(message,driver,textbox,name)
                    cmd.Blindmode(driver,message,name)
                    cmd.BnTAndGbc(message,textbox,driver,name,date)
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
                try:
                    driver.find_element_by_class_name(qt).click()
                except:
                    pass
                textbox = driver.find_element_by_xpath(tbx)
                response=str(e)[0].upper()+str(e)[1:]+'\n'
                if name in blist:
                    bd.blindmode(driver,response)
                textbox.send_keys(response)
            t.sleep(1)
    except Exception as e:
        print(e)
