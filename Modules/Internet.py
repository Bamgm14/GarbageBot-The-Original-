from bs4 import BeautifulSoup
import requests as rq
import random as r
import urllib3
import os
urllib3.disable_warnings()
http = urllib3.PoolManager()
def youtube(message,cyc):
    url = 'https://www.youtube.com/results?search_query='
    url+=message[4:].replace(' ','+')
    res= rq.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'})
    soup = BeautifulSoup(res.text,"html.parser")
    ytlist=[]
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        ytlist.append('https://www.youtube.com' + vid['href'])
    if len(ytlist)==0:
        return youtube(message)
    else:
        response=ytlist[0]
        if '*yes' in message:
            response=YesUtube(response)
        return response
def rshowert(message):
    url = 'https://www.reddit.com/r/Showerthoughts/'
    return Over(url,message)
def rmemes(message):
    urllist = ['https://www.reddit.com/r/memes/','https://www.reddit.com/r/meme/','https://www.reddit.com/r/dank_meme/']
    url=str(r.choice(urllist))
    return Over(url,message)
def rmathmeme(message):
    urllist=['https://www.reddit.com/r/MathJokes/','https://www.reddit.com/r/mathmemes/']
    url=str(r.choice(urllist))
    return Over(url,message)
def rpun(message):
    if '?written' not in message:
        urllist = ['https://www.reddit.com/r/puns/','https://www.reddit.com/r/Punny/']
        url=str(r.choice(urllist))
        return Over(url,message)
    else:
        pun=open('Pun.txt','r').read()
        punlist=pun.split('\n')#["A friend of mine tried to annoy me with bird puns, but I soon realized that toucan play at that game.", "Have you ever tried to eat a clock? It's very time consuming.", "Police were called to a daycare where a three-year-old was resisting a rest.", "I couldn't quite remember how to throw a boomerang, but eventually it came back to me.", "Simba was walking too slow, so I told him to Mufasa.", "Why is Peter Pan always flying? He neverlands! I love this joke because it never grows old.", "Jokes with punch lines can be painfully funny.", "A man died today when a pile of books fell on him. He only had his shelf to blame.", "What do you call a dinosaur with an extensive vocabulary? A Thesaurus.", "What happens when four children lock themselves in a wardrobe? That's narnia business..", "Why was Cinderella thrown off the basketball team? She ran away from the ball.", "My first job was working in an orange juice factory, but I got canned: couldn't concentrate.", "I wanna make a joke about sodium, but Na..", "Did you hear about the Italian chef with a terminal illness? He pastaway.", "An expensive laxative will give you a run for your money.", "I never understood odourless chemicals, they never make scents.", "Never trust an atom, they make up everything!", "When two vegetarians are arguing, is it still considered beef?", "I stayed up all night to see where the sun went. Then it dawned on me.", "When life gives you melons, you're probably dyslexic.", "I make apocalypse jokes like there's no tomorrow.", "No matter how hard you push the envelope it will still be stationery.", "What tea do hockey players drink? Penaltea!", "Did you hear about the guy who got hit in the head with a can of soda? He was lucky it was a soft drink.", "I was trying to make a pun about escaping quicksand but I'm stuck.", "The rotation of the earth really makes my day"]
        while '' in punlist:
            punlist.remove('')
        response=str(r.choice(punlist))
        return response
def ranattempt(message):
    url = 'https://www.reddit.com/r/therewasanattempt/'
    return Over(url,message)
def rphysmeme(message):
    urllist=['https://www.reddit.com/r/physicsmemes/','https://www.reddit.com/r/physicsjokes/']
    url=str(r.choice(urllist))
    return Over(url,message)
def rcompmeme(message):
    urllist=['https://www.reddit.com/r/programmingmemes/','https://www.reddit.com/r/ProgrammerHumor/']
    url=str(r.choice(urllist))
    return Over(url,message)
def rchemmeme(message):
    url = 'https://www.reddit.com/r/chemistrymemes/'
    return Over(url,message)
def Over(url,message,cyc=0):
    ur=url
    if cyc==0:
        if '?new' in message:
            url+='new/'
        elif '?hot' in message:
            url+='hot/'
        elif '?rising' in message:
            url+='rising/'
        elif '?contro' in message:
            url+='controversial/'
        elif '?top' in message:
            url+='top/'
    res= rq.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'})
    print(cyc,url)
    soup = BeautifulSoup(res.text,"html.parser")
    anlist=[]
    for x in soup.find_all('a'):
        if ur+'comments/' in x.get('href'):
            anlist.append(x.get('href'))
    if len(anlist)==0:
        if cyc<=40:
            return Over(url,message,cyc+1)
        else:
            return "An Error Has Occured, Try Again"
    else:
        response=str(r.choice(anlist))
        if '*yes' in message:
            response=yes(response)
        return response
def YesUtube(url,cyc=0):
    os.system("cd "+os.getcwd()+"\\PictureTemp\\"+"& youtube-dl -o"+str(len(os.listdir(os.getcwd()+"\\PictureTemp\\"))+1)+".mp4 "+url)
    if len(image)==0:
        if cyc==15:
            return None,url
        else:
            return yes(url,cyc+1)
    return os.getcwd()+'\\PictureTemp\\'+str(len(os.listdir(os.getcwd()+"\\PictureTemp\\")))+'.mp4',None
def yes(url,cyc=0):
    res= rq.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'})
    print(cyc)
    soup = BeautifulSoup(res.text,"html.parser")
    image=[]
    for x in soup.find_all('a'):
        if "https://i.redd.it/" in x.get('href') or "https://v.redd.it/" in x.get('href'):
            image.append(x.get('href'))
    if len(image)==0:
        if cyc==15:
            return None,url
        else:
            return yes(url,cyc+1)
    os.system(r'wget -P "'+os.getcwd()+'\PictureTemp" '+str(image[0]))
    return os.getcwd()+'\\PictureTemp\\'+image[0][18:],soup.title.get_text().split(':')[0]
