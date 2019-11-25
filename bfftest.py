import random 
import threading 
import time
from bfftestvar import *

print(rules)

def randp():
    global played
    randnum = random.randint(0, numplayers - 1)
    while (played[randnum] == True):
        randnum = random.randint(0, numplayers - 1)
    played[randnum] = True
    return players[randnum]

def q(): 
    global questioned
    randnum = random.randint(0, qnum - 1)
    while (questioned[randnum] == True):
        randnum = random.randint(0, qnum-1)
    questioned[randnum] = True
    print(questions[randnum])

def comp_input(ansA,ansB):
    if (ansA == ansB):
        return True
    """ things to include:
        double chara
        swapped chara
        keyboard mismatch
        missing chara
    """
    return False

def donothing():
    print("idle\n")

for i in range(0,numplayers):
    playername = randp()
    questions = initq(playername)
    for j in range(0,5):
        """q()
        timer = threading.Timer(10.0, a) 
        timer.start() 
        time.sleep(5.0) 
        
        """
        """ wait for ten seconds after last dude has answered; max of thirty seconds"""
        q()
        """send"""
        #time.sleep(10.0)
        ansA = input()
        ansB = input()
        print(comp_input(ansA,ansB))
        """recv"""
        #time.sleep(5.0) 

print("Exit\n")   
