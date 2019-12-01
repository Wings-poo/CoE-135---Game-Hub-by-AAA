from bfftest_s import *

def onebyone(players,pnum,scores):
    broadcast("\n\n" + oborules)
    printscores(players,pnum,scores,"ingame")
    
    played = [False] * pnum
    questioned = [False] * len(initq(""))
    ans = [""] * pnum

    for i in range(0,pnum):
        player,played = randp(players, pnum, played)
        questions = initq(players[player])
        broadcast("Round " +  str(i + 1) + ". Highlight is: " + players[player] + ".")

        for j in range(0,5):
            broadcast("\nQuestion " + str(j + 1) + ".")
            question,questioned = randq(questions, len(questions), questioned)
            broadcast(questions[question])
            
            ans = getanswer(pnum,30.0)
            
            print("All answers are in. Last 10 seconds to change your answer.")

            ans = getanswer(pnum,10.0)
                
            printanswers(players,pnum,ans)

            grantedpts = []
            print(players[player] + " please grant scores. Specify if player has an acceptable answer: Y/N")
            for k in range(0,pnum):
                if (k == player):
                    continue
                else:
                    print(players[k] + ": " + ans[k])
                    correct = input()
                    if (correct.lower() == 'y'):
                        scores[k] = scores[k] + 1
                        grantedpts.append(k)

            printgranted(players,grantedpts,scores)
            printscores(players,pnum,scores,"ingame")

    return scores