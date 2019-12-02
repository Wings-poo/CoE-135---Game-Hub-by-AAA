rules = "Welcome to The BFF Test!\n"
rules += "What is the BFF Test?\n"
rules += "    1. The BFF Test has two stages: group stage and one-by-one stage. The stages will be explained correspondingly when they start.\n"
rules += "    2. In each stage, there will be multiple questions. You will all be given 30 seconds to answer.\n" 
rules += "    3. When all answers are in, or if it's already the time limit, you will all be given an extra 10 seconds to change your answer.\n"
rules += "    4. Do take note that you are free to change your answer anytime within the time limit, and your last answer will be your final answer.\n" 
rules += "    5. The different stages will have different point-granting rules which will be explained accordingly when they start.\n"
rules += "    6. The player with the highest points will win.\n"
rules += "How to play:\n"
rules += "    1. Chat with normal text\n"
rules += "    2. Commands are sent with an opening and closing \'$$\'. The available commands are:\n"
rules += "       a. answer <answer> - to give an answer, duh\n"
rules += "       b. kick <username> - kick ya friend. byez\n"
rules += "       c. quit - feel free to walkout beshie\n"
rules += "    3. Have fun!\n"

grules = "Let's start with a warm up session.\n"
grules += "In this stage, there will be multiple questions, each pertaining to your group.\n"
grules += "All players will answer the question shown.\n"
grules += "Majority rules here and those whose answers are part of the majority gains a point.\n"
grules += "In the case of a tie, all included in the tie gets a point.\n"
grules += "Good luck~\n"

oborules = "Now, let's move on to the next stage.\n"
oborules += "In this stage, there will be multiple rounds, each highlighting one of the players.\n"
oborules += "All players will answer the question shown.\n"
oborules += "Once the round ends, the highlighted player will be the one to judge whether a player will get a point or not.\n"
oborules += "Good luck~\n"

def initq(pname):
    return [
        # Basic Info: 7
        "How old is " + pname + "?",
        "What is the middle initial of " + pname,
        "Number of siblings of " + pname + ".",
        "What is " + pname + "\'s childhood nickname?",
        "When was " + pname + " born?",
        "In what order was " + pname + " born among their siblings?",
        "Where is the province of " + pname + "?",

        # OR questions: 10
        "Does " + pname + " prefer calling or texting?",
        "Would " + pname + " dare to hug a stranger?",
        "What does " + pname + " prefer in YYH? If you don't know what YYH is, you're an angel.",
        "Asking the real questions. Is " + pname + " S or M?",
        "What would " + pname + " choose between meat and veggies?",
        "What does " + pname + " prefer? Social sciences or Natural sciences?",
        "Orange or Blue?",
        "Does " + pname + " prefer manga, anime, or live action?",
        "If the boat you're riding is sinking, who will " + pname + " choose to save?",
        "Can you trust " + pname + " with your secret/s?",

        # Favorites/Likes/Dislikes: 20
        "What is " + pname + "\'s favorite animal?",
        "What is the favorite cuisine of " + pname + "?",
        "Favorite color of " + pname + ".",
        "What is " + pname + "\'s favorite game?",
        "What is the favorite music genre of " + pname + "?",
        "Favorite Disney movie of " + pname + ".",
        "Who is " + pname + "\'s favorite Kpop artist/group?",
        "Who is the favorite vocaloid/vocaloid producer of " + pname + "?",
        "Favorite programming language of " + pname + ".",
        "Who is " + pname + "\'s favorite singer/band/idol?",
        "What’s a sound that " + pname + " hates?",
        "What’s the worst place " + pname + " have ever been to?",
        "What is the number one food that " + pname + " hates?",
        "Who is " + pname + "\'s idol crush?",
        "Favorite place that " + pname + " has traveled to.",
        "Favorite meme template of " + pname + ".",
        "Favorite number of " + pname + ".",
        "Most used emoji of " + pname + ".",
        "Name one thing that " + pname + " collects. (For " + pname + " list down all you can think of).",
        "Most used mobile app of " + pname + " aside from social media apps.",
        
        # UP rele: 18
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
        "What is " + pname + "\'s favorite pancit canton flavor?",
        "Favorite UP Diliman streetfood of " + pname + ".",
        "Where does " + pname + " usually tambay/stay within UP Diliman?",

        # Random: 25
        "What is the first thing " + pname + " will do if they win one million dollars?",
        "What is the first thing " + pname + " would buy if they win one million dollars?",
        "What accessory does " + pname + " usually wear?",
        "Name of " + pname + "\'s blog.",
        "What is the biggest \"what if \" of " + pname + "?",
        "Name something that will make " + pname + " to leave the house on a holiday.",
        "How can you best describe " + pname + "?",
        "Where was " + pname + " 3 hours ago?",
        "Name at least one hobby of " + pname + ". (For " + pname + " list down all you can think of).",
        "What would " + pname + " say if you asked them to loan you a million dollars (assuming they have a million dollars)?",
        "What is " + pname + "\'s guilty pleasure?",
        "What is " + pname + "\'s kink/fetish? ( ͡° ͜ʖ ͡°)",
        "What is the wallpaper of " + pname + "\'s phone currently?",
        "What would " + pname + " name their first child?",
        "What is the deepest fear of " + pname + "?",
        "What business would " + pname + " want to own/already owns?",
        "What is " + pname + "\'s strangest talent?",
        "Pet peeve of " + pname + ".",
        "Most recent song addiction of " + pname + ".",
        "Annie are you ok? Are you ok, Annie? What is the most criminal act that " + pname + " has ever done?",
        "How many shoes does " + pname + " have?",
        "What is " + pname + "\'s dream job?",
        "Dream destination of " + pname + ".",
        "What sports is " + pname + " most confident at?",
        "What is one thing that " + pname + " draws the most?"
    ]

gq = [
    # Sa inyong lahat: 20
    "Amongst you, who is most likely to sleep past 11 AM? (yes, AM)",
    "Which among your group is the laziest?", 
    "Mirror, mirror, on the wall, who's the sketchiest of them all?",
    "Who is the mother figure of the group?",
    "\"Anime\". Which among your group do you think of when you hear this word?", 
    "Which among your group is the most addicted to Kpop?",
    "There's a sale on anything and everything! Which among you would impulsively buy the most number of items?",
    "\"Sweet Princess, if through this wicked witch’s trick, a spindle should your finger prick. A ray of hope there still may be in this, the gift I give to thee.\" - Maleficent. Which among your group sleeps the most?",
    "Spicy. Who is the most tolerant to spicy food?",
    "It's the middle of the night, and you're feeling under the weather. Who would you contact first?",
    "Person who says the cheesiest lines.",
    "Bang! You have just pulled the trigger, which among you did you kill?",
    "Blah-blah-blah. Who's the most talkative in your group?",
    "Who is most likely to embarass themselves in front of their crush?",
    "Which among your group do you consider the most attractive?",
    "Who eats the most? Om nom nom",
    "Who is the flirtiest?",
    "We're all talented in one way, or another... But who amongst you do you think is the most talented?",
    "Who is the friendliest?",
    "*crash* Someone just pushed you off the stairs, who did it?",
]

kybrd = {
    'q' : ['w','a'],
    'w' : ['e','s','q'],
    'e' : ['r','d','w'],
    'r' : ['t','f','e'],
    't' : ['y','g','r'],
    'y' : ['u','h','t'],
    'u' : ['i','j','y'],
    'i' : ['o','k','u'],
    'o' : ['p','l','i',],
    'p' : ['[',';','o'],
    '[' : [']','\'','p'],
    'a' : ['s','q','z'],
    's' : ['d','w','x','a'],
    'd' : ['f','e','c','s'],
    'f' : ['g','r','v','d'],
    'g' : ['h','t','b','f'],
    'h' : ['j','y','n','g'],
    'j' : ['k','u','m','h'],
    'k' : ['l','i',',','j'],
    'l' : [';','o','.','k'],
    ';' : ['\'','p','/','l'],
    'z' : ['x','a'],
    'x' : ['c','s','z'],
    'c' : ['v','d','x'],
    'v' : ['b','f','c'],
    'b' : ['n','g','v'],
    'n' : ['m','h','b'],
    'm' : [',','j','n'],
    ',' : ['.','k','m'],
    '.' : ['/','l',',']
}
