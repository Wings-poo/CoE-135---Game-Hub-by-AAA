from bfftest_g import *
from bfftest_obo import *
from bfftest_s import *

def hostrecv(rnum,client):
    while (berk[rnum].state != "end" and berk[rnum].deadz[client] == False):
        msg = client.recv(1024).decode("utf8")
        parse_input(rnum,client,msg)
    return

def controller(rnum):
    global berk
    waitforplayers(rnum)
    berk[rnum].state = "allready"

    broadcast(rnum,"\nAll ready. Game start!") 
    printscores(rnum,"start")

    berk[rnum].state = "bygroup"
    bygroup(rnum)

    berk[rnum].state = "obo"
    onebyone(rnum)

    broadcast(rnum,"Game end")

    printscores(rnum,"end") 

    broadcast(rnum,"\nCongratulations to the highest scorer/s!")
    broadcast(rnum,"And of course, congratulations to the group who stayed, you have well kept your friendship! Until next time!") 

    time.sleep(5.0)
    berk[rnum].state = "end"
    return

def play(room, client):
    if (room.names[0] == client): # assume host will not leave before game starts...
        singlecast(client,rules)
        newroom = sleepover(room.names, room.user)#(room.names, room.user)
        roomnum[room.password] = len(berk)
        rnum = roomnum[room.password]
        clientroom[client] = rnum
        berk.append(newroom)
        
        ctrlr_thread = Thread(target = controller,args=(rnum,))
        host_thread = Thread(target = hostrecv,args=(rnum,client,))
        host_thread.daemon = True
        host_thread.start()
        ctrlr_thread.start()
        ctrlr_thread.join()

    else:
        while (not (room.password in roomnum)):
            pass
        rnum = roomnum[room.password]
        clientroom[client] = rnum
        if (not (client in berk[rnum].conntoname)):
            berk[rnum].addplayer(client,room.user[client])

        broadcast(rnum,"A new player appeared! Please welcome " + berk[rnum].conntoname[client] + "!\n")
        singlecast(client,rules)

        if (berk[rnum].state == "bygroup"):
            singlecast(client,"You have entered in the middle of the game. No time to prepare. Good luck deciphering what's happening.")
            singlecast(client,"\n" + grules)
        elif (berk[rnum].state == "obo"):
            singlecast(client,"You have entered in the middle of the game. No time to prepare. Good luck deciphering what's happening.")
            singlecast(client,"\n" + oborules)
        elif (berk[rnum].state == "end"):
            singlecast(client,"\n Too late.")

        while (berk[rnum].state != "end" and berk[rnum].deadz[client] == False):
            msg = client.recv(1024).decode("utf8")
            parse_input(rnum,client,msg)

    return
