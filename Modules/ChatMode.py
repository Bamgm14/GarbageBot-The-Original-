from names_dataset import NameDataset
m = NameDataset()
Chatmde=[]
def Chatmode(chatbot,var,word):
    word=word.split('\n')[0].replace('(',' ').replace(')',' ')
    lst=word.split(' ')
    for x in lst:
        if m.search_first_name(x) or m.search_last_name(x):
            word=word.replace(x,'{}')
    if '!' not in word:
        response = chatbot.get_response(word)
        try:
            return (str(response).format(var))
        except:
            return (response)
