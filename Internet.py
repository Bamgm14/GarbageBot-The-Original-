from bs4 import BeautifulSoup
import urllib3
import random as r
import os
urllib3.disable_warnings()
http = urllib3.PoolManager()
def youtube(message):
    url = 'https://www.youtube.com/results?search_query='
    url+=message[4:].replace(' ','+')
    res= http.request('GET', url)
    soup = BeautifulSoup(res.data,"html.parser")
    ytlist=[]
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        ytlist.append('https://www.youtube.com' + vid['href'])
    return ytlist[0]
def rshowert(message):
    url = 'https://www.reddit.com/r/Showerthoughts/'
    if '?new' in message:
        url+='new'
    elif '?hot' in message:
        url+='hot'
    elif '?rising' in message:
        url+='rising'
    elif '?contro' in message:
        url+='controversial'
    elif '?top' in message:
        url+='top'
    res= http.request('GET', url)
    soup = BeautifulSoup(res.data,"html.parser")
    stlist=[]
    for x in soup.find_all('a'):
        if "https://www.reddit.com/r/Showerthoughts/comments/" in x.get('href'):
            stlist.append(x.get('href'))
    response=str(r.choice(stlist))
def rmemes(message):
    url = 'https://www.reddit.com/r/memes/'
    if '?new' in message:
        url+='new'
    elif '?hot' in message:
        url+='hot'
    elif '?rising' in message:
        url+='rising'
    elif '?contro' in message:
        url+='controversial'
    elif '?top' in message:
        url+='top'
    res= http.request('GET', url)
    soup = BeautifulSoup(res.data,"html.parser")
    memelist=[]
    for x in soup.find_all('a'):
        if "https://www.reddit.com/r/memes/comments/" in x.get('href'):
            memelist.append(x.get('href'))
    response=str(r.choice(memelist))
    if '*yes' in message:
        response=yes(response)
    return response
def rpun(message):
    if '?written' not in message:
        url = 'https://www.reddit.com/r/puns/'
        if '?new' in message:
            url+='new'
        elif '?hot' in message:
            url+='hot'
        elif '?rising' in message:
            url+='rising'
        elif '?contro' in message:
            url+='controversial'
        elif '?top' in message:
            url+='top' 
        res= http.request('GET', url)
        soup = BeautifulSoup(res.data,"html.parser")
        pun=[]
        for x in soup.find_all('a'):
            if "https://www.reddit.com/r/puns/comments/" in x.get('href'):
                pun.append(x.get('href'))
        response=str(r.choice(pun))
        if '*yes' in message:
            response,title=yes(response)
            return response,title
    else:
        punlist=["A friend of mine tried to annoy me with bird puns, but I soon realized that toucan play at that game.", "Have you ever tried to eat a clock? It's very time consuming.", "Police were called to a daycare where a three-year-old was resisting a rest.", "I couldn't quite remember how to throw a boomerang, but eventually it came back to me.", "Simba was walking too slow, so I told him to Mufasa.", "Why is Peter Pan always flying? He neverlands! I love this joke because it never grows old.", "Jokes with punch lines can be painfully funny.", "A man died today when a pile of books fell on him. He only had his shelf to blame.", "What do you call a dinosaur with an extensive vocabulary? A Thesaurus.", "What happens when four children lock themselves in a wardrobe? That's narnia business..", "Why was Cinderella thrown off the basketball team? She ran away from the ball.", "My first job was working in an orange juice factory, but I got canned: couldn't concentrate.", "I wanna make a joke about sodium, but Na..", "Did you hear about the Italian chef with a terminal illness? He pastaway.", "An expensive laxative will give you a run for your money.", "I never understood odourless chemicals, they never make scents.", "Never trust an atom, they make up everything!", "When two vegetarians are arguing, is it still considered beef?", "I stayed up all night to see where the sun went. Then it dawned on me.", "When life gives you melons, you're probably dyslexic.", "I make apocalypse jokes like there's no tomorrow.", "No matter how hard you push the envelope it will still be stationery.", "What tea do hockey players drink? Penaltea!", "Did you hear about the guy who got hit in the head with a can of soda? He was lucky it was a soft drink.", "I was trying to make a pun about escaping quicksand but I'm stuck.", "The rotation of the earth really makes my day"]
        response=str(r.choice(punlist))
    return response
def yes(url):
    res= http.request('GET', url)
    soup = BeautifulSoup(res.data,"html.parser")
    image=[]
    for x in soup.find_all('a'):
        if "https://i.redd.it/" in x.get('href'):
            image.append(x.get('href'))
    os.system(r'wget -P '+os.getcwd()+'\PictureTemp '+str(image[0]))
    return os.getcwd()+'PictureTemp\\'+image[0][18:],soup.title.get_text().split(':')[0]
