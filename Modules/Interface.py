import Modules.Sports as s
Scommand={'?live':s.live,'?status':s.status}
def SInterface(message):
    for x in Scommand.keys():
        if x in message:
            answer=Scommand[x](str(message.split('!')[1].split('(')[1].split(',')[0]),str(message.split('!')[1].split('(')[1].split(',')[1].split(')')[0]))
            break
    return answer
