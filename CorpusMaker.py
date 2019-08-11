import ast
import pickle as p
file=open('MessageHistory.txt','r')
lst=file.read().split('\n====\n')
nlst=[]
dic={}
for x in lst:
    try:
        l=[]
        l.append(ast.literal_eval(x)[list(ast.literal_eval(x).keys())[0]][1])
        print(ast.literal_eval(x))
        if list(ast.literal_eval(x).keys())[0] not in nlst:
            nlst.append(list(ast.literal_eval(x).keys())[0])
            dic[list(ast.literal_eval(x).keys())[0]]=l
        else:
            if ast.literal_eval(x)[list(ast.literal_eval(x).keys())[0]][1] not in dic.values():
                dic[list(ast.literal_eval(x).keys())[0]]+=l
    except Exception as e:
        print(str(e))
print(nlst,dic)
f1=open('Message.bin','wb')
p.dump(dic,f1)
f1.close()
f1=open('Message.bin','rb')
print(p.load(f1))
f1.close()
