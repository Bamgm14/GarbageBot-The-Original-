import Commands as c
import ast
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer
def Train(file):
    print(file)
    for x in open(file,'r').read().split('\n'):
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
