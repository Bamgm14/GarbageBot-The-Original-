import time as t
def makeadmin(message,driver,textbox,name):
    botadmin=open('Special.txt','r+').read().split('\n')
    if message.split('!')[0].replace('\n','') in botadmin and message.split('!')[0].replace('\n','')!='':
        message=message.split('!')[1].split('\n')[0][9:].split(' ')[1]
        if message not in HB(message,driver,textbox,name):
            textbox.send_keys("Person Not Here\n")
        else:
            click_menu = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[2]")
            click_menu.click()
            prt=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[5]/div[1]/div/div/div[1]/span')
            driver.execute_script("arguments[0].scrollIntoView();", prt)
            prt.click()
            t.sleep(3) 
            send=driver.find_element_by_xpath('/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/label/input') 
            send.send_keys(message+'\n')
            t.sleep(3)
            if driver.find_element_by_class_name('FPZFa').is_displayed():
                textbox.send_keys("You Are Admin Already\n")
            else:
                driver.find_element_by_class_name('_3NWy8').click()
                driver.find_element_by_xpath('/html/body/div[1]/div/span[4]/div/ul/li[1]/div').click()
                t.sleep(2)
            driver.find_element_by_class_name('qfKkX').click()
            t.sleep(3)
            driver.find_element_by_class_name('qfKkX').click()
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
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/input').send_keys(message.split('!')[1][4:]+'\n')
    t.sleep(3)
    click_menu = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[2]")
    click_menu.click()
    prt=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[5]/div[2]/div[2]/div/div')
    driver.execute_script("arguments[0].scrollIntoView();", prt)
    prt.click()
    t.sleep(2)
    send=driver.find_element_by_xpath('/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/label/input')
    send.send_keys(name+'\n')
    t.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div/span/span').click()
    t.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/span[2]/div/div/div/span').click()
    t.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div[2]').click()
def linkmeback(message,driver,textbox,name):
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/input').send_keys(message.split('!')[1][4:]+'\n')
    t.sleep(3)
    click_menu = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[2]")
    click_menu.click()
    prt=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[5]/div[3]/div[2]/div/div')
    driver.execute_script("arguments[0].scrollIntoView();", prt)
    prt.click()
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div/div[3]/div[2]/div/span").click()
    t.sleep(1)
    send=driver.find_element_by_xpath('/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/label/input')
    send.send_keys(name+'\n')
    driver.find_element_by_xpath('/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/span/div/div/div/span').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/header/div/div[1]/button/span').click()
def HB(message,browser,textbox,name):
    try:
        click_menu = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header/div[2]/div[2]/span').text.lower()
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
