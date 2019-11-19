import random 
import threading 
import time

players = ["Aidee","Angie","Amanda"]
playername = players[random.randint(0, len(players)-1)]
questions = [
    "What is the favorite cuisine of " + playername + "?",
    "How old is " + playername + "?",
    "What is the middle initial of " + playername,
    playername + "\'s most recent song addiction",
    "Number of siblings of " + playername]

def q(): 
    r1 = random.randint(0, len(questions)-1) 
    print(questions[r1])

def a():
    ans = input()

def donothing():
    print("idle\n")

for i in range(0,2):
    q()
    timer = threading.Timer(10.0, a) 
    timer.start() 
    time.sleep(5.0) 
    
    """q()
    time.sleep(10.0)
    a() 
    time.sleep(5.0) """

print("Exit\n")   