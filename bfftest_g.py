from bfftest_s import *

def init_uf(rnum):
    global berk
    berk[rnum].head = [0] * berk[rnum].pnum
    for i in range(0,berk[rnum].pnum):
        berk[rnum].head[i] = i
    berk[rnum].famsize = [1] * berk[rnum].pnum
    berk[rnum].bigfam = 1

def union(A,B,rnum):
    global berk
    headA = find(A,rnum)
    berk[rnum].head[B] = headA
    berk[rnum].famsize[headA] = berk[rnum].famsize[headA] + 1
    if (berk[rnum].bigfam < berk[rnum].famsize[headA]):
        berk[rnum].bigfam = berk[rnum].famsize[headA]

def find(A,rnum):
    global berk
    if (berk[rnum].head[A] == A):
        return A
    return find(berk[rnum].head[A],rnum)

def comp_ans(ansA,ansB):
    ansA = ansA.lower()
    ansB = ansB.lower()

    if (ansA == ansB):
        return True
    elif ((len(ansA) + 1) == len(ansB)):
        # missing chara
        for i in range(0,len(ansB)):
            newB = ansB[:i] + ansB[i+1:]
            if (ansA == newB):
                return True
    elif (len(ansA) == (len(ansB) + 1)):
        # extra chara
        for i in range(0,len(ansA)):
            newA = ansA[:i] + ansA[i+1:]
            if (newA == ansB):
                return True
    elif (len(ansA) == len(ansB)):
        # swapped chara
        for i in range(0,len(ansB)-2):
            newB = ansB[:i] + ansB[i+1] + ansB[i] + ansB[i+2:]
            if (ansA == newB):
                return True
        # keyboard mismatch - only one direction?
        # for i in range(0,len(ansB)):  
        #    for j in   
        #    newB = ansB[:i] + ansB[i+1:]
    else:
        return False
    
def bygroup(rnum):
    global berk
    broadcast(rnum,"\n" + grules)
    
    gquestioned = [0] * len(gq)
    for j in range(0,5):
        broadcast(rnum,"\nQuestion " + str(j + 1) + ".")
        question,questioned = randq(gq, len(gq), gquestioned)
        broadcast(rnum,gq[question])

        getanswer(rnum,30.0,False)
        broadcast(rnum,"\nAll answers are in. Last 10 seconds to change your answer.")
        getanswer(rnum,10.0,True)

        printanswers(rnum)

        # granting of pts
        init_uf(rnum)
        for i in range(0,berk[rnum].pnum):
            for j in range(0,berk[rnum].pnum):
                if (comp_ans(berk[rnum].ans[i],berk[rnum].players[j])):
                    for k in range(0,berk[rnum].pnum):
                        if (find(i,rnum) == find(k,rnum)):
                            continue
                        if (comp_ans(berk[rnum].ans[i],berk[rnum].ans[k]) or (comp_ans(berk[rnum].ans[i],berk[rnum].players[j]) and comp_ans(berk[rnum].ans[k],berk[rnum].players[j]))):
                            union(i,k,rnum)

        for i in range(0,berk[rnum].pnum):
            foundone = False
            for j in range(0,berk[rnum].pnum):
                if (comp_ans(berk[rnum].ans[i],berk[rnum].players[j])):
                    foundone = True
            if (foundone == False and berk[rnum].famsize[find(i,rnum)] == 1):
                berk[rnum].ans[i] = ""

        berk[rnum].grantedpts = []
        for i in range(0,berk[rnum].pnum):
            if (berk[rnum].ans[i] == ""):
                continue
            if (berk[rnum].famsize[find(i,rnum)] == berk[rnum].bigfam):
                berk[rnum].grantedpts.append(berk[rnum].players[i])

        printgranted(rnum)
        printscores(rnum,"ingame")

        time.sleep(5)
