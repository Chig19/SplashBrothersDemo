import random

def guessr():
    emptypot=[]
    for x in range (0,10): 
        emptypot.append(raw_input())
    print emptypot
    myfav=random.choice(emptypot)
    print myfav
    
    