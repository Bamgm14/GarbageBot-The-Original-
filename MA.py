import time as t
def makeadmin(driver,textbox,message,botadmin,lst):
    if message.split('!')[0].replace('\n','') in botadmin and message.split('!')[0].replace('\n','')!='':
        message=message.split('!')[1].split('\n')[0][9:].split(' ')[1]
        if message not in lst:
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
            driver.find_element_by_class_name('_3NWy8').click()
            driver.find_element_by_xpath('/html/body/div[1]/div/span[4]/div/ul/li[1]/div').click()
            t.sleep(2)
            driver.find_element_by_class_name('qfKkX').click()
            t.sleep(3)
            driver.find_element_by_class_name('qfKkX').click()
    else:
        textbox.send_keys("You Aren't Special\n")
def special(name,message,textbox):
    try:
        a=open('special.txt','a')
    except:
        a=open('special.txt','w+')
    a.write(name.lower()+'\n')
    a.close()
    textbox.send_keys('You Are Special\n')
        
