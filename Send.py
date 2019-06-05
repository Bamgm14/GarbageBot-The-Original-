import time as t
import Blind as b
def send(driver,direct,name=None,lst=None,caption=None):
    attach_xpath = '//*[@id="main"]/header/div[3]/div/div[2]/div'
    send_file_xpath = '/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div/span'
    attach_type_xpath = '/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input'
    # open attach menu
    attach_btn = driver.find_element_by_xpath(attach_xpath)
    attach_btn.click()
    # Find attach file btn and send screenshot path to input
    t.sleep(1)
    attach_img_btn = driver.find_element_by_xpath(attach_type_xpath)
    # TODO - might need to click on transportation mode if url doesn't work
    attach_img_btn.send_keys(direct)
    t.sleep(1)
    if caption!=None:
        caption_xpath = "/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/span/div/div[2]/div/div[3]/div[1]/div[2]"
        send_caption = driver.find_element_by_xpath(caption_xpath)
        send_caption.send_keys(caption)
        if name in lst:
            b.blindmode(driver,caption)
    send_btn = driver.find_element_by_xpath(send_file_xpath)
    send_btn.click()
