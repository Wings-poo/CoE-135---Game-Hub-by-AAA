import random 
from threading import Thread
import time
from bfftestq import *

berk = []
roomnum = {}
clientroom = {}

class sleepover:
    def __init__(self, names, usernames):
        # copy variables from Room // makes a new class para lang less gulo?
        self.conn = names               # List of players' connections (client variable)
        self.conntoname = usernames     # Dict of conn:username of the players
        self.pnum = len(self)           # Number of players in room
        self.state = "notyet"			# If playing or not, what stage the game is in

        # Addl variables
        self.deadz = {}
        self.players = []               # List of players' usernames
        self.idx = {}                   # Dict of username:idx
        for i in range(0,self.pnum):
            self.players.append(self.conntoname[self.conn[i]])
            self.deadz[self.conn[i]] = False
        for i in range(0,self.pnum):
            self.idx[self.players[i]] = i
        self.scores = [0] * self.pnum

        self.player = -5
        self.readying = False
        self.ready = []
        self.readied = 0

        self.answering = False
        self.answered = 0
        self.ans = [""] * self.pnum

        self.judging = False
        self.grantedpts = []

        self.head = [0]
        self.famsize = [1]
        self.bigfam = 1

    # When new player arrives   
    def addplayer(self, name, username):
        self.conn.append(name)
        self.conntoname[name] = username
        self.players.append(username)
        self.idx[username] = self.pnum
        self.ans.append("")
        self.head.append(self.pnum)
        self.famsize.append(1)
        self.deadz[name] = False
        self.pnum = self.pnum + 1

    def __len__(self):
         return len(self.conntoname)

def randq(questions, qnum, questioned): 
    randnum = random.randint(0, qnum - 1)
    while (questioned[randnum] == True):
        randnum = random.randint(0, qnum-1)
    questioned[randnum] = True
    return randnum, questioned

def broadcast(rnum,msg):
    msg += '\n'
    for i in berk[rnum].conn:
        i.send(msg.encode())

def singlecast(conn,msg): 
    conn.send(msg.encode())

def parse_input(rnum,conn,msg):
    global berk
    
    if msg.startswith('%%') and msg.endswith('%%'):
        nmsg = msg[len('%%'):len(msg)-len('%%')].split(',')
        cmd = nmsg[0]
        nmsg = nmsg[1:]

        # before game start
        if cmd == 'ready' and len(nmsg) == 0 and berk[rnum].readying == True:
            if (berk[rnum].ready[berk[rnum].idx[berk[rnum].conntoname[conn]]] == False):
                berk[rnum].readied = berk[rnum].readied + 1
                berk[rnum].ready[berk[rnum].idx[berk[rnum].conntoname[conn]]] = True
        elif cmd == 'unready' and len(nmsg) == 0 and berk[rnum].readying == True:
            if (berk[rnum].ready[berk[rnum].idx[berk[rnum].conntoname[conn]]] == True):
                berk[rnum].readied = berk[rnum].readied - 1
                berk[rnum].ready[berk[rnum].idx[berk[rnum].conntoname[conn]]] = False

        # in game
        elif cmd == 'ans' and len(nmsg) >= 1 and berk[rnum].answering == True:
            mess = nmsg[0]
            if (len(nmsg) > 1):
                for i in range(1,len(nmsg)):
                    mess += "," + nmsg[i]
            if (berk[rnum].ans[berk[rnum].idx[berk[rnum].conntoname[conn]]] == ""):
                berk[rnum].answered = berk[rnum].answered + 1
            berk[rnum].ans[berk[rnum].idx[berk[rnum].conntoname[conn]]] = mess

        # after game question round
        elif ((cmd == 'grant') and (len(nmsg) == 1)):
            if (berk[rnum].player < 0):
                singlecast(conn, "Invalid command")
            elif ((berk[rnum].judging == True) and (nmsg[0] in berk[rnum].idx) and (berk[rnum].conntoname[conn] == berk[rnum].players[berk[rnum].player]) and (nmsg[0] != berk[rnum].players[berk[rnum].player])):
                if (berk[rnum].grantedpts.count(nmsg[0]) == 0):
                    berk[rnum].grantedpts.append(nmsg[0])
            else:
                singlecast(conn, "Invalid command")
        elif ((cmd == 'ungrant') and (len(nmsg) == 1)):
            if (berk[rnum].player < 0):
                singlecast(conn, "Invalid command")
            elif ((berk[rnum].judging == True) and (nmsg[0] in berk[rnum].idx) and (berk[rnum].conntoname[conn] == berk[rnum].players[berk[rnum].player]) and (nmsg[0] != berk[rnum].players[berk[rnum].player])):
                if (berk[rnum].grantedpts.count(nmsg[0]) != 0):
                    berk[rnum].grantedpts.remove(nmsg[0])
            else:
                singlecast(conn, "Invalid command")

        # default
        elif cmd == 'quit' and len(nmsg) == 0:
            mess = berk[rnum].conntoname[conn] + " is quitting"
            broadcast(rnum,mess)
            berk[rnum].deadz[conn] = True
            conn.send(bytes("$$quit$$", "utf8"))
            conn.close()
            print("%s:%s has disconnected" % addresses[conn])
        elif cmd == "kick" and len(nmsg) == 1 and (nmsg[0] in berk[rnum].idx):
            mess = berk[rnum].conntoname[conn] + " has kicked " + nmsg[0]
            broadcast(rnum,mess)
            connkick = ""
            for i in berk[rnum].conntoname:
                if berk[rnum].conntoname[i] == nmsg[0]:
                    connkick = i
            berk[rnum].deadz[connkick] = True
            connkick.send(bytes("$$quit$$", "utf8"))
            connkick.close()
            print("%s:%s has disconnected" % addresses[connkick])
        else:
            singlecast(conn, "Invalid command")
    else:
        broadcast(rnum,berk[rnum].conntoname[conn] + ": " + msg)

def getanswer(rnum,timelimit,isext):
    global berk
    if (not isext):
        berk[rnum].ans = [""] * berk[rnum].pnum
    berk[rnum].answering = True
    berk[rnum].answered = 0

    tstart = time.time()
    tend = time.time()
    while ((tend - tstart < timelimit) and (berk[rnum].answered < berk[rnum].pnum or isext)):
        tend = time.time()
    if (tend - tstart > timelimit):
        broadcast(rnum,"Time's up.")
    berk[rnum].answering = False

def grantpts(rnum):
    global berk
    berk[rnum].grantedpts = []
    berk[rnum].judging = True

    singlecast(berk[rnum].conn[berk[rnum].player], berk[rnum].players[berk[rnum].player] + " please grant scores.")
    singlecast(berk[rnum].conn[berk[rnum].player], "To grant scores, type \"$$grant,<username>$$\". To ungrant scores, \"$$ungrant,<username>$$\"")

    tstart = time.time()
    tend = time.time()
    while (tend - tstart < 30.0):
        tend = time.time()
    if (tend - tstart > 30.0):
        broadcast(rnum,"Time's up.")
    judging = False

def waitforplayers(rnum):
    global berk
    berk[rnum].readying  = True
    berk[rnum].ready = [False] * berk[rnum].pnum

    broadcast(rnum,"\nWaiting for players all players to ready... Minimum of 3 players to play...")
    broadcast(rnum,"To ready, type \"$$ready$$\". To unready, \"$$unready$$\"")
    while ((berk[rnum].readied < berk[rnum].pnum) or (berk[rnum].pnum < 3)):
        print(berk[rnum].pnum, berk[rnum].readied)
    berk[rnum].readying = False

def printgranted(rnum):
    global berk
    broadcast(rnum,"\nHere are the players granted scores to:")
    for i in range(0,len(berk[rnum].grantedpts)):
        broadcast(rnum,berk[rnum].grantedpts[i])
        berk[rnum].scores[berk[rnum].idx[berk[rnum].grantedpts[i]]] = berk[rnum].scores[berk[rnum].idx[berk[rnum].grantedpts[i]]] + 1

def printscores(rnum,stage):
    if (stage == "start"):
        broadcast(rnum,"\nInitial scores are:")
    if (stage == "ingame"):
        broadcast(rnum,"\nCurrent scores are:")
    if (stage == "end"):
        broadcast(rnum,"\n*drum rolls*\n*drum rolls*\n*drum rolls*\n\nFinal scores are:")
    print(berk[rnum].pnum,berk[rnum].players)
    for k in range(0,berk[rnum].pnum):
        print(k)
        broadcast(rnum,berk[rnum].players[k] + ":" + str(berk[rnum].scores[k]))

def printanswers(rnum):
