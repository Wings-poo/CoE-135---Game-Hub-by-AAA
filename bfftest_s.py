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
        self.conn = names.copy()            # List of players' connections (client variable)
        self.conntoname = usernames.copy()  # Dict of conn:username of the players
        self.pnum = len(self)               # Number of players in room
        self.currpnum = self.pnum
        self.state = "notyet"	    		# If playing or not, what stage the game is in

        # Addl variables
        self.deadz = {}
        self.players = []                   # List of players' usernames
        self.idx = {}                       # Dict of username:idx
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

        self.deadz[name] = False
        self.players.append(username)
        self.idx[username] = self.pnum

        self.ans.append("")
        self.head.append(self.pnum)
        self.famsize.append(1)
        self.scores.append(0)

        self.pnum = self.pnum + 1
        self.currpnum = self.currpnum + 1

    def __len__(self):
         return len(self.conntoname)

def randq(questions, qnum, questioned): 
    randnum = random.randint(0, qnum - 1)
    while (questioned[randnum] == True):
        randnum = random.randint(0, qnum-1)
    questioned[randnum] = True
    return randnum, questioned

def broadcast(rnum,msg):
    msg = msg + '\n'
    for i in berk[rnum].conn:
        if berk[rnum].deadz[i] == False:
            i.send(msg.encode())

def singlecast(conn,msg): 
    if berk[clientroom[conn]].deadz[conn] == False:
        conn.send(msg.encode())

def parse_input(rnum,conn,msg):
    global berk
    
    if msg.startswith('%%') and msg.endswith('%%'): ###$$
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
        elif ((cmd == 'grant') and (len(nmsg) == 1) and (berk[rnum].judging == True)):
            if (berk[rnum].player < 0):
                singlecast(conn, "Invalid command")
            elif ((nmsg[0] in berk[rnum].idx) and (berk[rnum].conntoname[conn] == berk[rnum].players[berk[rnum].player]) and (nmsg[0] != berk[rnum].players[berk[rnum].player])):
                if (berk[rnum].grantedpts.count(nmsg[0]) == 0):
                    berk[rnum].grantedpts.append(nmsg[0])
            else:
                singlecast(conn, "Invalid command")
        elif ((cmd == 'ungrant') and (len(nmsg) == 1) and (berk[rnum].judging == True)):
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
            berk[rnum].currpnum = berk[rnum].currpnum - 1
            if berk[rnum].player >= 0 and conn == berk[rnum].conn[berk[rnum].player]:
                mess = "Player highlighted gone. Skipping round."
                broadcast(rnum,mess)
        elif cmd == "kick" and len(nmsg) == 1 and (nmsg[0] in berk[rnum].idx):
            if nmsg[0] == berk[rnum].conntoname[conn]:
                singlecast(conn, "Invalid command")
            else:
                mess = berk[rnum].conntoname[conn] + " has kicked " + nmsg[0]
                broadcast(rnum,mess)
                connkick = berk[rnum].conn[berk[rnum].idx[nmsg[0]]]
                berk[rnum].deadz[connkick] = True
                berk[rnum].currpnum = berk[rnum].currpnum - 1
                singlecast(connkick, "Send your last words...")
                if berk[rnum].player >= 0 and connkick == berk[rnum].conn[berk[rnum].player]:
                    mess = "Player highlighted gone. Skipping round."
                    broadcast(rnum,mess)
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
    while ((tend - tstart < timelimit) and (berk[rnum].answered < berk[rnum].currpnum or isext)):
        tend = time.time()
        if berk[rnum].player >= 0 and berk[rnum].deadz[berk[rnum].conn[berk[rnum].player]] == True:
            break
        if berk[rnum].currpnum == 1:
            break
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
        if berk[rnum].deadz[berk[rnum].conn[berk[rnum].player]] == True:
            break
        if berk[rnum].currpnum == 1:
            break
    if (tend - tstart > 30.0):
        broadcast(rnum,"Time's up.")
    berk[rnum].judging = False

def waitforplayers(rnum):
    global berk
    berk[rnum].readying  = True
    berk[rnum].ready = [False] * berk[rnum].pnum

    broadcast(rnum,"\nWaiting for players all players to ready...")
    broadcast(rnum,"To ready, type \"$$ready$$\". To unready, \"$$unready$$\"")
    while (berk[rnum].readied < berk[rnum].currpnum):
        if berk[rnum].currpnum == 1:
            break
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
    for k in range(0,berk[rnum].pnum):
        broadcast(rnum,berk[rnum].players[k] + ":" + str(berk[rnum].scores[k]))

def printanswers(rnum):
    broadcast(rnum,"\nHere are the players' answers:")
    for k in range(0,berk[rnum].pnum):
        broadcast(rnum,berk[rnum].players[k] + ": " + berk[rnum].ans[k])
