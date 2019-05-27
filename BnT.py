import random as r
import os
def Builder(level,players):
    a=open('SnL.py','w+')
    a.write('''import random as r
import os
import Send as s
import time as t
import matplotlib.pyplot as plt
import numpy as np
def Set(n,c):
    global Ladders
    global Snakes
    global Players
    a={}
    plt.grid()
    plt.axis([-1,10,-1,10])
    plt.xticks(np.arange(-1, 10, step=1))
    plt.yticks(np.arange(-1, 10, step=1))
    for x in Ladders:
        Alg(x,'g*')
    for x in Snakes:
        Alg(x,'r*')
    for x in n:
        a[x],=Alg(sum(Players[x]),'bo')
    plt.savefig(os.getcwd()+'\\Bike\\image_'+str(c)+'.png')
    for x in n:
        a[x].remove()
def Alg(n,a):
    y=n//10
    x=n%10
    b=plt.plot(x,y,a)
    return b
def BikesAndTrucks(n,q):
    global Ladders
    global Snakes
    a=r.randrange(1,7)
    response=("Player "+str(q)+" Moved "+str(a)+'\\n')
    n.append(a)
    b=r.randrange(1,11)
    if sum(n) in Snakes:
        response+=("Oh No... A Truck Chased You... Move "+str(b)+" Backward!!\\n")
        n.append(-b)
    b=r.randrange(1,11)
    if sum(n) in Ladders:
        response+=("Yay... A Bike Helps You... Move "+str(b)+" Forward!!\\n")
        n.append(b)
    if sum(n)<0:
        n.append((-1)*sum(n))
    response+=("Current Position:"+str(sum(n))+'\\n')
    return response
def Standard(textbox,Player):
    flag=0
    response=BikesAndTrucks(Players[Player],Player)
    textbox.send_keys(response)
    if sum(Players[Player])>=100:
        response=Player+" Is Winner\\n"
        textbox.send_keys(response)
        t.sleep(5)
        flag=1
    t.sleep(5)
    return flag
def Loop(textbox=None,driver=None):
    global Players
    count=0
    while True:
        count+=1
        for x in list(Players.keys()):
            flag=Standard(textbox,x)
            if flag==1:
                break
        Set(Players,count)
        s.send(driver,os.getcwd()+'\\Bike\\image_'+str(count)+'.png')
        t.sleep(10)
        if flag==1:
            break\n''')
    Snakes=[]
    Ladders=[]
    while len(Snakes)!=(level*5) or len(Ladders)!=(level*5):
        e=r.randrange(1,100)
        if (e not in Snakes) and (len(Snakes)!=(level*5)):
            Snakes.append(e)
        if (e not in Snakes) or (e not in Ladders) and (len(Ladders)==(level*5)):
            Ladders.append(e)
    a.write('Snakes='+str(Snakes)+'\nLadders='+str(Ladders)+'\n')
    a.write('Players={')
    for x in players:
        a.write('"'+x+'":[],')
    a.write('}\n')
    a.close()
