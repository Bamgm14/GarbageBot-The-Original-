import datetime as d
import time as t
def ArriveUser(User,date):
    if '#' in User:
        User.replace('#','*')
    if ' ' in User:
        User.replace(' ','_')
    a=open('Users.txt','a')
    a.write('\n'+User+'#True[('+date.split('T')[0]+')('+date.split('T')[1]+')]\n')
    a.close()
def LeaveUser(User,date):
    a=open('Users.txt','r')
    c=''
    b=a.read().split('\n')
    a.close()
    while '' in b:
        b.remove('')
    for x in b:
        if x.split('#')[0]==User and 'True' in x.split('#')[1]:
            c=x.split('#')[1][4:]
            b.remove(x)
            b.append(User+'#False'+c+'[('+date.split('T')[0]+')('+date.split('T')[1]+')]')
    a=open('Users.txt','w')
    for x in b:
        a.write(x+'\n')
    a.close()
def Users():
    c={}
    a=open('Users.txt','r')
    b=a.read().split('\n')
    while '' in b:
        b.remove('')
    for x in b:
        c[x.split('#')[0]]=(x.split('#')[1]).split('[')[0]
    a.close()
    return c
