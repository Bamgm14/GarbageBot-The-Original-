Chatmde=[]
def Chatmode(chatbot,var,word):
    word=word.split('\n')[0]
    if '!' not in word:
        response = chatbot.get_response(word)
        try:
            return (str(response).format(var))
        except:
            return (response)
