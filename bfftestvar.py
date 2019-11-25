rules = 'Welcome to The BFF Test. How to play:\n'
rules += '    1. Chat with normal text\n'
rules += '    2. Commands are sent with an opening and closing \'$$\'. The available commands are:\n'
rules += '       a. answer <answer> - to give an answer, duh\n'
rules += '       b. kick <username> - kick ya friend. byez\n'
rules += '       c. quit - feel free to walkout beshie\n'
rules += '    3. Have fun!\n'

players = ["Aidee","Angie","Amanda","Ella","Panda"]
numplayers = len(players)
played = [False] * numplayers
playername = ""

def initq(pname):
    return [
        # Basic Info:
        "How old is " + pname + "?",
        "What is the middle initial of " + pname,
        "Number of siblings of " + pname + ".",
        "What is " + pname + "\'s childhood nickname?",
        "When was " + pname + " born?",

        # Favorites:
        "What is " + pname + "\'s favorite animal?",
        "What is the favorite cuisine of " + pname + "?",
        "Favorite color of " + pname + ".",
        "What is " + pname + "\'s favorite mobile game?",
        "What is the favorite music genre of " + pname + "?",
        "Favorite Disney movie of " + pname + ".",
        "Who is " + pname + "\'s favorite Kpop artist/group?",
        "Who is the favorite vocaloid of " + pname + "?",
        "Favorite programming language of " + pname + ".",
        "Who is " + pname + "\'s favorite singer/band/idol?",
        
        # UP rele:
        "How many UP Diliman orgs does " + pname + " have?",
        "How many orgs (not restricted to UPD) does " + pname + " have?",
        "How many MST subjects has " + pname + " taken?",
        "How many SSP subjects has " + pname + " taken?",
        "How many AH subjects has " + pname + " taken?",
        "How many GEs has " + pname + " taken?",
        "How many PEs has " + pname + " taken?",
        "What is " + pname + "\'s favorite major subject?",
        "What is " + pname + "\'s favorite GE subject?",
        "What is " + pname + "\'s favorite PE subject?",
        "Where is " + pname + "\'s favorite spot in UP Diliman?",
        "How long has " + pname + " been in UP Diliman?",
        "What is the student number of " + pname + "?",
        "What is the degree/course of " + pname + "?",
        "Within UP Diliman area, where does " + pname + " usually eat out?",
        ]

qnum = len(initq(""))
questioned = [False] * qnum