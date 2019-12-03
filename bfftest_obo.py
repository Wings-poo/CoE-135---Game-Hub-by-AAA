from bfftest_s import *

def randp(players, pnum, played):
    randnum = random.randint(0, pnum - 1)
    while (played[randnum] == True):
        randnum = random.randint(0, pnum - 1)
    played[randnum] = True
    return randnum, played

def onebyone(rnum):
    global berk
    broadcast(rnum,"\n" + oborules)
    printscores(rnum,"ingame")
    
    played = [False] * berk[rnum].pnum
    questioned = [False] * len(initq(""))

    for i in range(0,berk[rnum].pnum):
        if (len(played) < berk[rnum].pnum):
            played.append(False)
        berk[rnum].player,played = randp(berk[rnum].players, berk[rnum].pnum, played)
        questions = initq(berk[rnum].players[berk[rnum].player])
        broadcast(rnum,"\nRound " +  str(i + 1) + ". Highlight is: " + berk[rnum].players[berk[rnum].player] + ".")
        if berk[rnum].deadz[berk[rnum].conn[berk[rnum].player]] == True:
            continue

        for j in range(0,3):
            question,questioned = randq(questions, len(questions), questioned)
            broadcast(rnum,"\nQuestion " + str(j + 1) + ". " + questions[question])
            
            getanswer(rnum,30.0,False)
            broadcast(rnum,"\nAll answers are in. Last 10 seconds to change your answer.")
            getanswer(rnum,10.0,True)
                
            printanswers(rnum)

            if berk[rnum].deadz[berk[rnum].conn[berk[rnum].player]] == True:
                break
            broadcast(rnum,"\nNow, 30 seconds to convince " + berk[rnum].players[berk[rnum].player] + " to grant you a point!")
            grantpts(rnum)
            
            printgranted(rnum)
            printscores(rnum,"ingame")

            if berk[rnum].currpnum == 1:
                break

            time.sleep(5.0)

        if berk[rnum].currpnum == 1:
            break
