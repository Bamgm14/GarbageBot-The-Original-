import Bank as bk
import datetime as d
def Spliter(message):
    if '!rtrans' in message:
        Pass=message.split('!')[1].split('#')[1]
        money=message.split('!')[1].split('#')[2]
        name=message.split('!')[1].split('#')[3].split('\n')[0]
        return JCInterfaceR(Pas,name,money)
    if '!strans' in message:
        if message.split('!')[0]!='':
            return 'Error:Name Not Found'
        else:
            name=message.split('!')[0]
            money=message.split('!')[1].split('#')[1]
            return JCInterfaceS(name,money)
    if '!bankbal' in message:
        if message.split('!')[0]!='':
            return 'Error:Name Not Found'
        else:
            name=message.split('!')[0]
            return bk.Bal(name)
    if '!roulette' in message:
        if message.split('!')[0]!='':
            return 'Error:Name Not Found'
        else:
            name=message.split('!')[0]
            number=message.split('!')[1].split('#')[1].split('\n')[0]
            return 'InProgress'
def JCInterfaceS(name,money):
    Pass=[]
    for x in str(d.datetime.now().isoformat().split('T')[1].split('.')[0].split(':')[0]+d.datetime.now().isoformat().split('T')[1].split('.')[0].split(':')[1]):
        Pass.append(str(hex(ord(str(x)))))
    response=bk.WithdrawMoney(name,money)
    if response=='Successful':
        return 'jc!banktransfer #'+('.'.join(Pass))+' #'+str(money)+' #'+str(name)
    else:
        return response
def JCInterfaceR(Pas,name,money):
    Pass=[]
    for x in str(d.datetime.now().isoformat().split('T')[1].split('.')[0].split(':')[0]+d.datetime.now().isoformat().split('T')[1].split('.')[0].split(':')[1]):
        Pass.append(hex(ord(str(x))))
    P=Pas.split('.')
    for x in range(len(P)):
        assert P[x]==Pass[x],'Password Incorrect'
    response=bk.DepositMoney(name,money)
    return response
