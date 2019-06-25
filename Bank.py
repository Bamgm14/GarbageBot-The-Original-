import pickle as p
import datetime as d
import random as r
def Read():
    try:
        file=open('Bank.bin','rb')
        bank=p.load(file)
        file.close()
        return bank
    except:
        file=open('Bank.bin','wb')
        p.dump({},file)
        file.close()
        return Read()
def Bal(name):
    bank=Read()
    if name in bank.keys():
        return 'Balance\n'+name+':'+str(bank[name])
    else:
        return 'You Have Not Registered In Bank'    
def Money(name,money):
    bank=Read()
    f=open('Bank.bin','wb')
    if name in bank.keys():
        bank[name]+=money
    else:
        bank[name]=money
    p.dump(bank,f)
    f.close()
def DepositMoney(name,money):
    if money<=0:
        return "You Can't Add Negative Money"
    else:
        Money(name,money)
        return 'Successful'
def WithdrawMoney(name,money):
    if money<=0:
        return "You Can't Withdraw Negative Money"
    else:
        Money(name,(-1)*(money))
        return 'Successful'
def Interest(date):
    try:
        f=open('Time.txt','r')
        Hour=f.read().split(':')[0]
        Minute=f.read().split(':')[1]
        f.close()
    except:
        Hour='0'
        Minute=(d.datetime.now().isoformat()).split('T')[1].split(':')[1]
    if int((d.datetime.now().isoformat()).split('T')[1].split(':')[0])-int(Hour)!=0 and int((d.datetime.now().isoformat()).split('T')[1].split(':')[1])-int(Minute)==0:
        f=open('Time.txt','w')
        Hour=(d.datetime.now().isoformat()).split('T')[1].split(':')[0]
        Minute=(d.datetime.now().isoformat()).split('T')[1].split(':')[1]
        f.write(Hour+':'+Minute)
        f.close()
        bank=Read()
        for x in bank.keys():
            Money(x,(bank[x]*0.1))
    else:
        pass
#def Roulette(name,number):
#    if 'e'==number:
#    comp=r.randrange(1,37)
