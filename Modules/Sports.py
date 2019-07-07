from pycricbuzz import Cricbuzz
import datetime as d
c=Cricbuzz()
Matches=c.matches()
def teammatch(team1,team2):
    team1=team1[0].upper()+team1[1:].lower()
    team2=team2[0].upper()+team2[1:].lower()
    flag=0
    for x in Matches:
        tlist=[x['team1']['name'],x['team2']['name']]
        if team1 in tlist and team2 in tlist:
            flag=1
            return False,x
    if flag==0:
        return True,'No Match Recently Between '+team1+' And '+team2
def status(team1,team2):
    lst=teammatch(team1,team2)
    if lst[0]:
        return lst[1]
    else:
        return 'Status:'+str(lst[1]['status'])
def live(team1,team2):
    lst=teammatch(team1,team2)
    info=''
    info+='As Of '+d.datetime.now().isoformat().split('T')[1]+'\n'
    if lst[0]:
        return lst[1]
    else:
        checklive=status(team1,team2)
        if 'won' in checklive:
            return 'Game Is Over'
        elif 'Starts' in checklive:
            return 'Game Has Not Started'
        else:
            match=c.livescore(lst[1]['id'])
            for x in match.keys():
                info+=x.upper()[0]+x.lower()[1:]+'\n'
                for y in match[x].keys():
                    if isinstance(match[x][y], str):
                        info+=y.upper()[0]+y.lower()[1:]+':'+match[x][y]+'\n'
                    else:
                        for z in match[x][y]:
                            if len(z)>0:
                                if len(z)>1:
                                    info+='Player '+str(int(match[x][y].index(z))+1)+':\n'
                                for a in z.keys():
                                    if z[a]:
                                        info+=a.upper()[0]+a.lower()[1:]+':'+z[a]+'\n'
                                    else:
                                        info+=a.upper()[0]+a.lower()[1:]+':None\n'
        return info
def matchoverview(team1,team2):
    lst=teammatch(team1,team2)
    info=''
    info+='As Of '+d.datetime.now().isoformat().split('T')[1]+'\n'
    if lst[0]:
        return lst[1]
    else:
        checklive=status(team1,team2)
        if 'Starts' in checklive:
            return 'Game Has Not Started'
        else:
            match=c.scorecard(lst[1]['id'])
            
