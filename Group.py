import time as t
import Constant as c
def makeadmin(message,driver,textbox,name):
    botadmin=open('Special.txt','r+').read().split('\n')
    if message.split('!')[0].replace('\n','') in botadmin and message.split('!')[0].replace('\n','')!='':
        message=message.split('!')[1].split('\n')[0][9:].split(' ')[1]
        if message not in HB(message,driver,textbox,name):
            textbox.send_keys("Person Not Here\n")
        else:
            click_menu = driver.find_element_by_xpath(c.Menu)
            click_menu.click()
            prt=driver.find_element_by_xpath(c.Parti)
            driver.execute_script(c.Scroll, prt)
            prt.click()
            t.sleep(3) 
            send=driver.find_element_by_xpath(c.Search_parti) 
            send.send_keys(message+'\n')
            t.sleep(3)
            if driver.find_element_by_class_name(c.Adm).is_displayed():
                textbox.send_keys("You Are Admin Already\n")
            else:
                driver.find_element_by_class_name(c.Madm).click()
                driver.find_element_by_xpath(c.BMadm).click()
                t.sleep(2)
            driver.find_element_by_class_name(c.Qt).click()
            t.sleep(3)
            driver.find_element_by_class_name(c.Qt).click()
    else:
        textbox.send_keys("You Aren't Special\n")
def special(message,driver,textbox,name):
    try:
        a=open('Special.txt','a')
    except:
        a=open('Special.txt','w+')
    a.write(name.lower()+'\n')
    a.close()
    textbox.send_keys('You Are Special\n')
def Addmeback(message,driver,textbox,name):
    driver.find_element_by_xpath(c.GrpSrch).send_keys(message.split('!')[1][4:]+'\n')
    t.sleep(3)
    click_menu = driver.find_element_by_xpath(c.Menu)
    click_menu.click()
    prt=driver.find_element_by_xpath(c.AddPrt)
    driver.execute_script(c.Scroll, prt)
    prt.click()
    t.sleep(2)
    send=driver.find_element_by_xpath(c.Search_add)
    send.send_keys(name+'\n')
    t.sleep(2)
    driver.find_element_by_xpath(c.Add).click()
    t.sleep(2)
    driver.find_element_by_xpath(c.Tick).click()
    t.sleep(2)
    driver.find_element_by_xpath(c.AddPt).click()
def linkmeback(message,driver,textbox,name):
    driver.find_element_by_xpath(c.GrpSrch).send_keys(message.split('!')[1][4:]+'\n')
    t.sleep(3)
    click_menu = driver.find_element_by_xpath(c.Menu)
    click_menu.click()
    prt=driver.find_element_by_xpath(c.Invite)
    driver.execute_script(c.Scroll, prt)
    prt.click()
    driver.find_element_by_xpath(c.Snd_invite1).click()
    t.sleep(1)
    send=driver.find_element_by_xpath(c.Search_add)
    send.send_keys(name+'\n')
    driver.find_element_by_xpath(c.Snd_invite2).click()
    driver.find_element_by_xpath(c.Back).click()
def HB(message,browser,textbox,name):
    try:
        click_menu = browser.find_element_by_xpath(c.Menu).text.lower()
        assert 'last' and 'online' not in click_menu,'Second Path'
        assert 'typing' not in click_menu,'Please Stop Typing\n'
        participate=click_menu.replace(' ','').split(',')
        return participate
    except Exception as e:
        if str(e)=='Please Stop Typing\n':
            textbox.send_keys(e)
            return HB(message,browser,textbox,name)
        else:
            lst=[]
            lst.append(name.lower())
            return lst
