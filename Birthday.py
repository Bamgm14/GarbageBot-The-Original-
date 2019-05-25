def Newbirthday(message,calender):
    binfo=message.split(' ')[1]
    binfo=binfo.split('\n')[0]
    blis=binfo.split(':')
    fix=blis[0]+':'+blis[1]
    bdate=blis[1].split('-')
    assert blis[0].isalpha(),'I need a name, not Numbers'
    assert blis[0] not in list(calender.keys()),'Name Already Exists,if this try adding the second name with "_"'
    assert int(bdate[0]) in [1,2,3,4,5,6,7,8,9,10,11,12] and int(bdate[1]) in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],'Not a date'
    b=open('Birthdays.txt','a')
    b.write('\n'+fix)
    b.close()
def Refresh():
    calender={}
    a=open('Birthdays.txt','r+')
    birthday=a.read()
    cal=birthday.split('\n')
    for x in cal:
        if x!='':
            calender[x.split(':')[0]]=x.split(':')[1]
    a.close()
    return calender
def FindBirthday(message,date,calender):
    bname=message.split(' ')[1]
    bname=bname.split('\n')[0]
    if bname in calender.keys():
        response=calender[bname]
        if date.split('T')[0][5:]==response:
            response+='\nHAPPY BIRTHDAY '+bname+'!!\n'
        return response
    else:
        response='No Name In Database\n'
        return response
def CheckBirthday(message,date,calender):
    response='Here Are '
    if '?' not in message:
        response+='Todays Birthdays:\n'
        for x in calender:
            if calender[x]==date:
                response+=x+'\n'
        if len(x.split('\n'))<=1:
            response+='No Birthdays In Database'
    else:
        check=(x.split('?')[1]).split('\n')[0]
        assert int(check.split('-')[0]) in [1,2,3,4,5,6,7,8,9,10,11,12] and int(check.split('-')[1]) in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],'Not a date'
        response+=check+' Brithdays:'
        for x in calender:
            if calender[x]==check:
                response+=x+'\n'
        if len(x.split('\n'))<=1:
            response+='No Birthdays In Database'
    return response
