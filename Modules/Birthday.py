import datetime as d
import time as t
from bs4 import BeautifulSoup
import urllib3
import random as r
import os
def Newbirthday(message,calender,Random=None):
    binfo=message.split(' ')[1]
    binfo=binfo.split('\n')[0]
    blis=binfo.split(':')
    fix=blis[0]+':'+blis[1]
    bdate=blis[1].split('-')
    assert blis[0].isalpha(),'I need a name, not Numbers'
    assert blis[0] not in list(calender.keys()),'Name Already Exists,if this try adding the second name with "_"'
    d.date(int(bdate[0]),int(bdate[1]),int(bdate[2]))
    b=open('Birthdays.txt','a')
    b.write('\n'+fix)
    b.close()
    return 'Successful'
def Refresh():
    calender={}
    a=open('Birthdays.txt','r+')
    birthday=a.read().split('\n')
    for x in birthday:
        if x!='':
            calender[x.split(':')[0]]=x.split(':')[1]
    a.close()
    return calender
def FindBirthday(message,calender,date=d.datetime.now().isoformat()):
    bname=message.split(' ')[1]
    bname=bname.split('\n')[0]
    if bname in calender.keys():
        response=calender[bname]
        if date.split('T')[0][5:]==response[5:]:
            response+='\nHAPPY BIRTHDAY '+bname+'!!\n'
        return response
    else:
        response='No Name In Database\n'
        return response
def CheckBirthday(message,calender,date=d.datetime.now().isoformat()):
    response='Here Are '
    if '?' not in message:
        response+='Todays Birthdays:\n'
        for x in calender:
            if calender[x][5:]==date.split('T')[0][5:]:
                response+=x+'\n'
        if len(response.split('\n'))<=2:
            response+='\nNo Birthdays In Database'
    else:
        check=(message.split('?')[1]).split('\n')[0]
        assert d.date(2000,int(check.split('-')[0]),int(check.split('-')[1])),'Not a date'
        response+=check+' Brithdays:\n'
        for x in calender:
            if calender[x][5:]==check:
                response+=x+'\n'
        if len(response.split('\n'))<=2:
            response+='\nNo Birthdays In Database'
    return response
def g_check(lst,calender):
    response='Here You Go:\n'
    for x in lst:
        if 'you' not in x.replace(' ',''):
            response+=x.replace(' ','').lower()+':'+FindBirthday(' '+x.replace(' ','').lower(),calender,d.datetime.now().isoformat())+'\n'
    return response
