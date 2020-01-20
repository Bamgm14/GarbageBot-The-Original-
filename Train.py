import Commands as c
import ast
import nltk
import numpy as np
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer,UbuntuCorpusTrainer
def Train(file,var='y'):
    var=var.lower()
    print(file)
    lst=open(file,'r').read().split('\n')
    if len(lst)>=100 and var=='y':
        var=[]
        for x in list(np.random.randint(low=0, high=len(lst), size=1000)):
            var.append(lst[x])
        lst=var
    for x in lst:
        try:
            conversation=ast.literal_eval(x)
            print(conversation)
            trainer = ListTrainer(c.chatbot)
            trainer.train(conversation)
        except Exception as e:
            print(str(e))
            pass
def Test():
    word=''
    while word!='bye':
        word=input('>')
        print(c.chatbot.get_response(word))

def DefTrain():
    trainer = ChatterBotCorpusTrainer(c.chatbot)
    trainer.train("chatterbot.corpus.english.ai",
              "chatterbot.corpus.english.conversations",
              "chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.emotion")
    UbuntuCorpusTrainer(c.chatbot)
def Chatter():
    b='Hi'
    while True:
        a=nltk.chat.iesha.iesha_chatbot.respond(b)
        print(a)
        b=c.chatbot.get_response(a)
        print(b)

