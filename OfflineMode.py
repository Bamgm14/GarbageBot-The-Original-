#Offline Command Mode
import os
from Commands import *
import datetime as d
class Node:
    def send_keys(x):
        print(x)
        if os.path.isfile(x):
            os.system('"'+x+'"')
        return None
    def click():
        return None
class Nod(Node):
    def find_element_by_xpath(var=None):
        return Node
def cmd(msg):
    Commands(Nod,Node,d.datetime.now().isoformat(),msg)
msg=''
while msg!='bye garb':
    try:
        msg=input("Input Message:")
        cmd(msg)
    except Exception as e:
        print(str(e))
