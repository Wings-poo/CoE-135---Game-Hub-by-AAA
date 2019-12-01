from bfftest_g import *
from bfftest_obo import *
from bfftest_s import *

def hostrecv():
    while (berk[rnum].state != "end"):
        msg = client.recv(1024).decode("utf8")
        parse_input(rnum,client,msg)
    return

def controller(rnum):
    global berk
    print(berk[rnum].pnum)
    #waitforplayers(rnum)
    berk[rnum].state = "allready"

    broadcast(rnum,"\nAll ready. Game start!") 
    printscores(rnum,"start")

    berk[rnum].state = "bygroup"
    bygroup(rnum)

    berk[rnum].state = "obo"
    #onebyone(rnum)

    broadcast(rnum,"Game end")

    berk[rnum].state = "end"
    printscores(rnum,"end") 

    broadcast(rnum,"\nCongratulations to the highest scorer/s!")
    broadcast(rnum,"And of course, congratulations to the group who stayed, you have well kept your friendship! Until next time!") 
    return

def play(room, client):
    if (room in roomnum): # (check which room to change to room.password in roomnum) addplayer
        rnum = roomnum[room]
        clientroom[client] = rnum
        berk[rnum].addplayer(client,room.user[client])#(room.names, room.user)
    else: # move room class to sleepover class
        newroom = sleepover(room.names, room.user)#(room.names, room.user)
        roomnum[room] = len(berk)
        rnum = roomnum[room]
        clientroom[client] = rnum
        berk.append(newroom)

    broadcast(rnum,"A new player appeared! Please welcome " + berk[rnum].conntoname[client] + "!\n")
    singlecast(client,rules)
    
    if (room.names[0] == client): # assume host will not leave before game starts
        controller(rnum)
        """
        ctrlr_thread = Thread(target = controller,args=(rnum,))
        host_thread = Thread(target = hostrecv)
        host_thread.daemon = True
        host_thread.start()
        ctrlr_thread.start()
        ctrlr_thread.join()
        """

    else:
        if (berk[rnum].state == "bygroup"):
            singlecast(client,"You have entered in the middle of the game. No time to prepare. Good luck deciphering what's happening.")
            singlecast(client,"\n" + grules)
        elif (berk[rnum].state == "obo"):
            singlecast(client,"You have entered in the middle of the game. No time to prepare. Good luck deciphering what's happening.")
            singlecast(client,"\n" + oborules)
        elif (berk[rnum].state == "end"):
            singlecast(client,"\n Too late.")

        while (berk[rnum].state != "end"):
            print(berk[rnum].state)
            msg = client.recv(1024).decode("utf8")
            parse_input(rnum,client,msg)

    return
