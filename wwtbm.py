import random
import sys
import time
import threading
import signal
import os

def menu(player):
    while True:
        clear(player)
        player.send((bytes("WHO WANTS TO BE A MILLIONAIRE?\nPress spacebar to start\nPress ? for help\nPress other keys to exit\n", "utf8")))
        BUFSIZ = 1024;
        menu_press = player.recv(BUFSIZ).decode("utf8")
        if menu_press == '?':
            help_menu(player)
        elif menu_press == ' ':
            play(player)
        else:
            return

def help_menu(player):
    BUFSIZ = 1024
    clear(player)
    text = "__________\nHow to play?\n\nWho Wants to Be a Millionaire is a trivia game involving a series of trivia questions.\nWhat you have to do is answer each questions within the  time limit, which varies per round.\nThere is a total of three rounds with five questions per each round.\nYou will have 15 seconds to answer on the first round, 30 seconds on the second and 45 seconds on the third.\nYour score will be equivalent to the cash prize of the highest correct level that you answered.\n\nGOOD LUCK!\n___________\n"
    player.send((bytes(text, "utf8")))
    player.send((bytes("Press any key to continue", "utf8")))
    player.recv(BUFSIZ).decode("utf8")
    return

def get_ans(player, delay, cor_0, cor_1, fifty, call_friend, audience, score):
    BUFSIZ = 1024
    level_score = [0, 1000, 2000, 3000, 5000, 10000, 20000, 30000, 40000, 50000, 100000, 200000, 300000, 400000, 500000, 1000000]
    while(1):
        player.send((bytes("Answer: ", "utf8")))
        a = time.time()
        ans = player.recv(BUFSIZ).decode("utf8")
        b = time.time()
        c = int(b - a)
        if c > delay:
            text = "Time's up. Correct answer is " +  cor_0 + "\nGame over! Your total score is " + str(level_score[score - 1]) +"\n"
            player.send((bytes(text, "utf8")))
            time.sleep(3)
            score = -1
            return fifty, call_friend, audience, score
        if (ans == 'E')|(ans == 'e'):
            fifty, call_friend, audience = lifeline(player, cor_0, fifty, call_friend, audience)
        elif(ans == cor_0) | (ans == cor_1):
            text = "Correct! You got " + str(level_score[score]) + " php\n"
            player.send((bytes(text, "utf8")))
            time.sleep(2)
            return fifty, call_friend, audience, score
        else:
            text = "Incorrect. Correct answer is " +  cor_0 + "\nGame over! Your total score is " + str(level_score[score - 1]) +"\n"
            player.send((bytes(text, "utf8")))
            time.sleep(3)
            score = -1
            return fifty, call_friend, audience, score

def lifeline(player, cor_0, fifty, call_friend, audience):
    BUFSIZ = 1024
    choice = ["A", "B", "C", "D"]
    text(player,"Choose lifeline to use:")
    if(fifty):
        text(player,"Press 1 if \"50-50\". Reduce the choices into two.")
    if(call_friend):
        text(player,"Press 2 to call a friend.")
    if(audience):
        text(player,"Press 3 to ask the audience.")

    life_used = player.recv(BUFSIZ).decode("utf8")
    if(life_used == '1') & (fifty):
        fifty = False
        buf = cor_0
        while buf == cor_0:
            buf = choice[random.randint(0, 3)]
        text(player,"Result of 50-50: ")
        if(cor_0 < buf):
            text(player,cor_0 + " or " + buf)
        else:
            text(player,buf + " or " + cor_0)
    elif(life_used == '2') & (call_friend):
        call_friend = False
        text(player,"Friend: Just pick " + cor_0)
    elif(life_used == '3') & (audience):
        audience = False
        text(player,"Audience votes: \n")
        if(cor_0 == 'A'):
            text(player,"A: 55%\nB: 5%\nC: 20%\nD: 20%")
        elif(cor_0 == 'B'):
            text(player,"A: 36%\nB: 44%\nC: 17%\nD: 3%")
        elif(cor_0 == 'C'):
            text(player,"A: 3%\nB: 4%\nC: 69%\nD: 24%")
        else:
            text(player,"A: 12%\nB: 25%\nC: 23%\nD: 40%")
    else:
        text(player,"Failed to use a lifeline.\n")
    return fifty, call_friend, audience

def play(player):
    choice = ["A", "B", "C", "D"]
    choice_small = ["a", "b", "c", "d"]
    fifty = True
    call_friend = True
    audience = True

    #initialize levels
    level_1 = ["What is the first letter of the Alphabet?\nA. A\nB. B\nC. C\nD. D\n", "The female deer is known as?\nA. jill\nB. doe\nC. flyer\nD. hen\n", "Who among the following is a national hero of the Philippines?\nA. Marian Rivera\nB. James Reid\nC. Jose Rizal\nD. Sir Briones\n", "What is the currency of the Philippines?\nA. Dollar\nB. Yen\nC. Won\nD. Peso\n", "How many continents are in the world?\nA. 7\nB. 6\nC. 5\nD. 4\n","What is the formula for water?\nA. H3O\nB. H2O\nC. H3O2\nD. H2O2\n","How many sides a pentagon has?\nA. 3\nB. 4\nC. 5\nD. 6\n", "Up above the world so high, like a diamond in the sky. Which poem do the lyrics belong to?\nA. Old Macdonald\nB. Three Little Pigs\nC. Mary Had a Little Lamb\nD. Twinkle Twinkle Little Star\n", "What is the chemical Symbol for Oxygen?\nA. O\nB. C\nC. H\nD. He\n", "What is the largest planet?\nA. Earth\nB. Jupiter\nC. Sun\nD. Mars\n"]
    level_2 = ["Botany is the study of?\nA. Animal\nB. Population\nC. Plants\nD. Human Body\n", "How many elements are in a periodic table?\nA. 115\nB. 116\nC. 117\nD. 118\n", "Who built the pyramids?\nA. Egyptians\nB. Summerians\nC. Greeks\nD. Romans\n", "Who is the first Greek god of love?\nA. Zeus\nB. Aphrodite\nC. Hera\nD. Hermes\n", "How many keys are there on a piano?\nA. 66\nB. 77\nC. 88\nD. 99\n", "Which American singer is known as the King of Pop?\nA. Justin Bieber\nB. Miley Cyrus\nC. Ed Sheeran\nD. Michael Jackson\n", "Komodo dragon belongs to which animal family?\nA. Lizard\nB. Cats\nC. Dogs\nD. Bears\n", "In the bible, after the flood, what sign did God give that He would not destroy the earth with a flood again?\nA. Rain\nB. Rainbow\nC. Clouds\nD. Lightning", "In which game the word \"love\" is used?\nA. Basketball\nB. Soccer\nC. Tennis\nD. Volleyball\n", "In the movie \"Home Alone\", who was the child left at home in Christmas Holidays?\nA. John\nB. Peter\nC. James\nD. Kevin\n"]
    level_3 = ["\"You can't see me\" is a catchphrase of which wrestler?\nA.John Cena\nB. Dwayne Johnson\nC. Hulk Hogan\nD. Dennis Rodman\n", "A golf ball is made up of?\nA. Plastic\nB. Rubber\nC. Metal\nD. Clay\n", "Who is the shortest NBA player with a height of 5 ft and 3 inches?\nA. Spud Webb\nB. Kay Felder\nC. Muggsy Bogues\nD. Isaiah Thomas\n", "Rain contains which vitamin?\nA. Vitamin B9\nB. Vitamin B10\nC. Vitamin B11\nD. Vitamin B12\n", "What type of blood group is a universal donor?\nA. O\nB. A\nC. B\nD. AB\n", "At the birth, how many bones do a baby have?\nA. 250\nB. 300\nC. 350\nD. 400\n", "Who sang the song Waka Waka?\nA. Beyonce\nB. Lady Gaga\nC. Shakira\nD. Taylor Swift\n", "The area of biology devoted to the study of fungi is known as?\nA. Microbiology\nB. Anatomy\nC. Phycology\nD. Mycology\n", "Which of these organs can grow back if some of it is removed?\nA. Liver\nB. Stomach\nC. Appendix\nD. Kidney\n", "Plants receive their nutrients mainly from\nA. Sun\nB. Soil\nC. Water\nD. Carbon Dioxide\n"]
    level_4 = ["What is the symbol for the element silver?\nA. Si\nB. Au\nC. Ag\nD. He\n", "What is the hottest planet of the solar system?\nA. Mercury\nB. Earth\nC. Mars\nD. Venus\n", "What is the age of the sun?\nA. 5 Billion Years\nB. 6 Billion years\nC. 7 Billion years\nD. 8 Billion years\n", "What is the symbol for the element gold?\nA. Si\nB. Au\nC. Ag\nD. He\n", "Which element can burn on the surface of water?\nA. Hydrogen\nB. Oxygen\nC. Potassium\nD. Carbon\n", "What is the lightest element?\nA. Oxygen\nB. Silicon\nC. Carbon\nD. Hydrogen\n", "What does the F stand for in FBI?\nA. Federal\nB. Federation\nC. Facility\nD. Factfinder\n", "After leaving Bethlehem, to which country did Joseph, Mary, and Jesus travel?\nA. Israel\nB. Egypt\nC. Turkey\nD. Qatar\n", "Which country does Santa Claus (Nicholas) originally belong to?\nA. Israel\nB. Egypt\nC. Turkey\nD. Qatar\n", "What is the highest score possible in 10 pin bowling?\nA. 150\nB. 200\nC. 250\nD. 300\n"]
    level_5 = ["Who discovered human cell?\nA. Robert Hooke\nB. Joseph Lister\nC. Charles Darwin\nD. Michael Harrison\n", "Who invented calculus?\nA. Pythagoras\nB. Sir Isaac Newton\nC. Archimedes\nD. James Waddell Alexander II\n", "Who is known as the father of mathematics?\nA. Pythagoras\nB. Sir Isaac Newton\nC. Archimedes\nD. James Waddell Alexander II\n", "Who invented the radioactive element called radium?\nA. Albert Einstein\nB. Galileo Galilei\nC. Alexander Fleming\nD. Marie Sklodowska-Curie\n", "30 is the atomic number of which element?\nA. Zinc\nB. Gallium\nC. Germanium\nD. Arsenic\n", "In 2017, Bill Gates held which position in the list of world's richest people?\nA. First position\nB. Second position\nC. Third position\nD. Fourth position\n", "Flutter is a group name of which beautiful creature?\nA. Fly\nB. Bees\nC. Butterfly\nD. Dragonfly\n", "Which sea is an extension of the Indian Ocean?\nA. Deep Sea\nB. Bering Sea\nC. Bali Sea\nD. Red Sea\n", "Who was the first person to invent a thermometer?\nA. Galileo Galilei\nB. Robert Hooke\nC. Aristotle\nD. Thomas Edison\n", "What is the middle layer of the Earth?\nA. Crust\nB. Mantle\nC. Inner Core\nD. Outer Core\n"]
    level_6 = ["Which city is the capital of Australia?\nA. Sydney\nB. Liverpool\nC. Canberra\nD. Melbourne\n", "Which is the capital of Quezon Province?\nA. Lucban\nB. Tayabas\nC. Infanta\nD. Lucena\n", "The Bataan Death March took place in what year?\nA. 1942\nB. 1947\nC. 1952\nD. 1957\n", "Who was the first Filipina to win the Miss International beauty title in 1964?\nA. Margarita Moran\nB. Gemma Cruz\nC. Gloria Diaz\nD. Tetchie Agbayani\n", "Gloria Diaz won the Miss Universe contest in what year?\nA. 1963\nB. 1966\nC. 1969\nD. 1972\n", "Which country is the largest producer of coffee?\nA. Philippines\nB. Congo\nC. Indonesia\nD. Brazil\n", "What is the name of the Pharaoh for whom the great pyramid of Giza was built?\nA. Khufu\nB. Narmer\nC. Nectanebo II\nD. Cleopatra\n", "Who made the first telescopic observations of the planet Mars?\nA. Pythagoras\nB. Galileo Galilei\nC. Robert Hooke\nD. Aristotle\n", "Who wrote the famous book, \"Snow White and the Seven Dwarfs\"?\nA. Grimm Brothers\nB. Hans Christian Andersen\nC. Wanda Gag\nD. Sir Briones\n", "Which year the APA style of citation originated?\nA. 1926\nB. 1927\nC. 1928\nD. 1929\n"]
    level_7 = ["Complete The Fibonacci Sequences 0, 1, 1, 2, 3, 5, 8, 13, 21, 34\nA. 55\nB. 56\nC. 57\nD. 58\n", "What Mathematical Symbol was determined by Whiz Ferdinand Von Lindemann in 1882?\nA. e\nB. Pi\nC. Theta\nD. alpha\n", "How many sides does an Icosahedron has?\nA. 10\nB. 15\nC. 20\nD. 30\n","In which civilization dot patterns were first employed to represent numbers?\nA. Indian\nB. Egyptians\nC. Sumerians\nD. Chinese\n", "In which ancient civilization introduced the representation of digits into words?\nA. Indian\nB. Egyptians\nC. Sumerians\nD. Chinese\n", "Which is the most ancient?\nA. Fibonacci\nB. Figurate\nC. Kaprekar\nD. Mersenne\n", "Who coined the word \"biochemistry\"?\nA. Alexander Fleming\nB. Sir Briones\nC. Wilhelm Kuhne\nD. Robert Hooke\n", "Which river serves as the international border between America and Canada?\nA. Nile River\nB. Mackenzie River\nC. Yukon River\nD. Niagara Falls\n", "How many teeth are there in an adult's mouth?\nA. 32\nB. 30\nC. 28\nD. 26\n", "In which city of Spain did Columbus die?\nA. Madrid\nB. Valladolid\nC. Valencia\nD. Palma\n"]
    level_8 = ["Which ocean bounds with South America from the west?\nA. Indian Ocean\nB. Arctic Ocean\nC. Pacific Ocean\nD. Atlantic Ocean\n", "What is the sea that has the Earth's lowest elevation?\nA. Red Sea\nB. Baffin Sea\nC. Queen Victoria Sea\nD. Salt Sea\n", "In 2016, two countries confirmed signing the Paris Climate agreement. One of them was the USA. Name the other country?\nA. China\nB. Russia\nC. France\nD. Singapore\n", "What's the other name of Mississippi Rivers?\nA. Mother of the rivers\nB.  Father of the rivers\nC. Queen of the Rivers\nD. King of the Rivers\n", "Ottawa is the capital of which country?\nA. Austria\nB. Australia\nC. Canada\nD. Singapore\n", "\"To die, to sleep - To sleep, perchance to dream - ay, there's the rub, For in this sleep of death what dreams may come..\" The dialogue belongs to which play?\nA. Romeo and Juliet\nB. Julius Caesar\nC. Macbeth\nD. Hamlet\n", "How many countries are there in Europe?\nA. 50\nB. 55\nC. 60\nD. 65\n", "Which Italian city is known as the City of Water?\nA. Verona\nB. Venice\nC. Messina\nD. Bologna\n", "Bolognese is the national dish of which country?\nA. France\nB. Germany\nC. Italy\nD. Philippines\n", "Who is the founder of the formula of Coca-Cola?\nA. John Richard\nB. John Peppermint\nC. John Permington\nD. John Permberton\n"]
    level_9 = ["A snail can sleep for how many years?\nA. 3 years\nB. 4 years\nC. 5 years\nD. 6 years\n", "How many heart chambers a cockroach has?\nA. 10\nB. 12\nC. 14\nD. 16\n", "Which animal has the highest blood pressure?\nA. Elephant\nB. Turtles\nC. Giraffe\nD. Lion\n", "A mandrill is what type of creature?\nA. Dog\nB. Cat\nC. Weasel\nD. Monkey\n", "Name the oldest giant panda, which died in 2016 at the age of 114?\nA. Jia Jia\nB. Chi Chi\nC. Quin\nD. Xiao Lao\n", "Out of twelve, how many dogs survive in the Titanic disaster?\nA. 2\nB. 3\nC. 4\nD. 5\n", "Which bird is a symbol of good luck?\nA. Dove\nB. Eagle\nC. Storks\nD. Flamingo\n", "Hominoidea is a scientific name of which animal?\nA. Turtle\nB. Penguin\nC. Tiger\nD. Ape\n", "The blind Dolphins are found in which river?\nA. Indus River\nB. Nile River\nC. Mississippi River\nD. Yukon River\n", "The fingerprints of which animal extremely resembles the humans?\nA. Tiger\nB. Koala\nC. Ape\nD. Monkey\n"]
    level_10 = ["What is the biggest island of the world?\nA. Antartica\nB. Iceland\nC. Greenland\nD. Japan\n", "How many states are there in the United States of America?\nA. 35\nB. 40\nC. 45\nD. 50\n", "Which is the largest lake of the world?\nA. Caspian Sea\nB.  Lake Baikal\nC. Taal Lake\nD. Don Juan Pond\n", "What is another name of Counter Strike?\nA. Death Battle\nB. Half-Life\nC. Counter Punch\nD. Free Fire\n", "How many maximum controllers are supported by PS3 System?\nA. 5\nB. 6\nC. 7\nD. 8\n", "Which PC game was delayed in the release because of a hidden picture of a developer's ass?\nA.  Counter Strike\nB. DOTA\nC. Halo\nD. Halo 2\n", "What is the name of the creator of PS4?\nA. Mark Cerny\nB. Minh Le\nC. Steve Feak\nD. Sir Briones\n", "Where is the Mountain Thor situated?\nA. USA\nB. Canada\nC. Mexico\nD. Austria\n", "Which is the third largest continent in the world?\nA. Europe\nB. Africa\nC. North America\nD. South America\n", "How much area of Egypt is acquired by the River Nile?\nA. 10%\nB. 15%\nC. 20%\nD. 22%\n"]
    level_11 = ["India is how many times larger than Japan?\nA. 8 times\nB. 10 times\nC. 12 times\nD. 14 times", "Which is the greenest country in the world?\nA. Greenland\nB. Finland\nC. Iceland\nD. Japan\n", "Which Spanish artist said he would eat his wife when she died?\nA. Lluis Rigalt\nB. Bernardo Piquer\nC. Salvador Dali\nD. Francisco Lameyer\n", "What did Joseph Priesley discover in 1774?\nA. Hydrogen\nB. Helium\nC. Carbon Dioxide\nD. Oxygen\n", "Where is the smallest bone in the body?\nA. Ear\nB. Mouth\nC. Backbone\nD. Nose\n", "What's the best known artificial international language?\nA. Kotava\nB. Esperanto\nC. Klingon\nD. Lingwa de planeta\n", "What is the capital of Kenya?\nA. Litein\nB. Machakos\nC. Nairobi\nD. Wundanyi\n", "What is the capital of Ethiopia?\nA. Adama\nB. Arba Minch\nC. Asella\nD. Addis Ababa\n", "What is the capital of Ecuador?\nA. Quito\nB. Tulcan\nC. Duran\nD. Esmeraldas\n", "Who invented television?\nA. Alexander Graham Bell\nB. John Logie Baird\nC. Sir Briones\nD. Thomas Edison\n"]
    level_12 = ["What star other than the sun is closest to the Earth?\nA. Alula Borealis\nB. Copernicus\nC. Proxima Centauri\nD. Vega\n", "What is the top selling spice in the world?\nA. Mustard\nB. Sugar\nC. Salt\nD. Pepper\n", "What is the most widely eaten fish in the world?\nA. Herring\nB. Tuna\nC. Sea Bass\nD. Tilapia\n", "What nation produces two thirds of the world's vanilla?\nA. Indonesia\nB. Madagascar\nC. Mexico\nD. China\n", "What country suffered the worst two earthquakes in history, killing 830000 in 1556 and 750000 in 1976?\nA. Indonesia\nB. Japan\nC. China\nD. Singapore\n", "What is the most malleable metal?\nA. Aluminum\nB. Platinum\nC. Silver\nD. Gold\n", "Which planet spins the fastest?\nA. Jupiter\nB. Venus\nC. Neptune\nD. Uranus\n", "Which planet spins the slowest?\nA. Jupiter\nB. Venus\nC. Neptune\nD. Uranus\n", "How long is a Martian year?\nA. ~487 days\nB. ~587 days\nC. ~687 days\nD. ~787 days\n", "What was the first organ successfully transplanted from a cadaver to a live person?\nA. Liver\nB. Heart\nC. Brain\nD. Kidney\n"]
    level_13 = ["Where is the world's largest supply of fresh water?\nA. Brazil\nB. Canada\nC. Russia\nD. Japan\n", "What bird was domesticated first?\nA. Chicken\nB. Goose\nC. Duck\nD. Dove\n", "Who was the last president of Soviet Union?\nA. Joseph Stalin\nB. Yuri Andropov\nC. Mikhail Gorbachev\nD. Konstantin Chernenko\n", "Where did the pineapple plant originate?\nA. Southeast Asia\nB. Pacific Islands\nC. North America\nD. South America\n", "How much milk does a cow give in her lifetime in average?\nA. 200000 glasses\nB. 250000 glasses\nC. 300000 glasses\nD. 350000 glasses\n", "In which century did mathematicians first use plus and minus sign?\nA. 15th century\nB. 16th century\nC. 17th century\n 18th century\n","What is the most frequently diagnosed cancer in men?\nA. Brain Cancer\nB. Thyroid Cancer\nC. Prostate Cancer\nD. Lung Cancer\n", "What do leukemia sufferers have too many of?\nA. Bacteria Cells\nB. Platelets\nC. Red blood cells\nD. White blood cells\n", "What's the only metal that's not a solid at room temperature?\nA. Mercury\nB. Silicon\nC. Hydrogen\nD. Gold\n", "How long does it take light from the sun to reach the earth?\nA. Around 7 minutes\nB. Around 8 minutes\nC. Around 9 minutes\nD. Around 10 minutes\n"]
    level_14 = ["How big is the Milky Way?\nA. 50000 light years\nB. 80000 light years\nC. 100000 light years\nD. 130000 light years\n", "Alborg Roedslet International Airport is in which Country?\nA. Germany\nB. USA\nC. Canada\nD. Denmark\n", "What was Elvis's last No. 1 in his lifetime?\nA. Suspicious Minds\nB. Hard Headed Woman\nC. Are You Lonesome Tonight?\nD. Surrender\n", "What was the first fairy tale that Walt Disney made a cartoon about?\nA. Jack and The Beanstalk\nB. Little Red Riding Hood\nC. Snow White and The Seven Dwarves\nD. Cinderella\n", "What is the first name of the composer Vivaldi?\nA. Giovanni\nB. Mario\nC. Antonio\nD. Francesco\n", "What is the name of Batman's son?\nA. Richard Grayson\nB. Richard Wayne\nC. Tim Drake\nD. Damian Wayne\n", "In the sport of Judo, what belt color follows an orange belt?\nA. Green\nB. Yellow\nC. Blue\nD. Red\n", "Which country claims the world's tallest building?\nA. Japan\nB. Malaysia\nC. Dubai\nD. China\n", "What is Freddie Mercury's birth name?\nA. Freddie Bulsara\nB. Jel Bulsara\nC. Farrokh Bulsara\nD. Zanzibar Bulsara\n", "What is Triskadekaphobia?\nA. Fear of tripping\nB. Fear of drinking alcohol\nC. Fear of three-legged things\nD. Fear of Number 13"]
    level_15 = ["In 1959, how many countries signed the Antarctic Treaty?\nA. 12\nB. 13\nC. 14\nD. 15\n", "Which year did the Spanish Civil war end?\nA. 1934\nB. 1939\nC. 1944\nD. 1949\n", "What is the diameter of our Earth?\nA. 10 742 km\nB. 11 742 km\nC. 12 742 km\nD. 13 742 km\n", "Which year the Minecraft was released?\nA. 2006\nB. 2007\nC. 2008\nD. 2009\n", "Which year the PS4 was released?\nA. 2013\nB. 2014\nC. 2015\nD. 2016\n", "What year is the EDSA revolution?\nA. 1985\nB. 1986\nC. 1987\nD. 1988\n", "When was the wheel invented?\nA. 2500 BC\nB. 3000 BC\nC. 3500 BC\nD. 4000 BC\n", "When was Microsoft established?\nA. 1960\nB. 1965\nC. 1970\nD. 1975\n", "Which year did the United Nations establish?\nA. 1945\nB. 1946\nC. 1947\nD. 1948\n", "When was Superman created as a fiction character?\nA. 1923\nB. 1933\nC. 1943\nD. 1953\n"]

    clear(player)
    #round 1
    r = random.randint(0,9)
    text(player,"Level 1\nPrize: 1000 php\n" + level_1[r] + "E. USE LIFELINE\n")
    fifty, call_friend, audience, score = get_ans(player, 15, choice[r % 4], choice_small[r % 4], fifty, call_friend, audience, 1)
    if score == -1:
        return
    clear(player)

    r = random.randint(0,9)
    text(player,"Level 2\nPrize: 2000 php\n" + level_2[r] + "E. USE LIFELINE\n")
    fifty, call_friend, audience,score = get_ans(player, 15, choice[(r + 2) % 4], choice_small[(r + 2) % 4], fifty, call_friend, audience, 2)
    if score == -1:
        return
    clear(player)

    r = random.randint(0,9)
    text(player,"Level 3\nPrize: 3000 php\n" + level_3[r] + "E. USE LIFELINE\n")
    fifty, call_friend, audience,score = get_ans(player, 15, choice[r % 4], choice_small[r % 4], fifty, call_friend, audience, 3)
    if score == -1:
        return
    clear(player)

    r = random.randint(0,9)
    text(player,"Level 4\nPrize: 5000 php\n" + level_4[r] + "E. USE LIFELINE\n")
    fifty, call_friend, audience, score = get_ans(player, 15, choice[(r + 2) % 4], choice_small[(r + 2) % 4], fifty, call_friend, audience, 4)
    if score == -1:
        return
    clear(player)

    r = random.randint(0,9)
    text(player,"Level 5\nPrize: 10000 php\n" + level_5[r] + "E. USE LIFELINE\n")
    fifty, call_friend, audience,score = get_ans(player, 15, choice[r % 4], choice_small[r % 4], fifty, call_friend, audience, 5)
    if score == -1:
        return
    clear(player)

    #round 2
    r = random.randint(0,9)
    text(player,"Level 6\nPrize: 20000 php\n" + level_6[r] + "E. USE LIFELINE\n")
    fifty, call_friend, audience,score = get_ans(player, 30, choice[(r + 2) % 4], choice_small[(r + 2) % 4], fifty, call_friend, audience, 6)
    if score == -1:
        return
    clear(player)

    r = random.randint(0,9)
    text(player,"Level 7\nPrize: 30000 php\n" + level_7[r] + "E. USE LIFELINE\n")
    fifty, call_friend, audience,score = get_ans(player, 30, choice[r % 4], choice_small[r % 4], fifty, call_friend, audience, 7)
    if score == -1:
        return
    clear(player)

    r = random.randint(0,9)
    text(player,"Level 8\nPrize: 40000 php\n" + level_8[r] + "E. USE LIFELINE\n")
    fifty, call_friend, audience,score = get_ans(player, 30, choice[(r + 2) % 4], choice_small[(r + 2) % 4], fifty, call_friend, audience, 8)
    if score == -1:
        return
    clear(player)

    r = random.randint(0,9)
    text(player,"Level 9\nPrize: 50000 php\n" + level_9[r] + "E. USE LIFELINE\n")
    fifty, call_friend, audience,score = get_ans(player, 30, choice[r % 4], choice_small[r % 4], fifty, call_friend, audience, 9)
    if score == -1:
        return
    clear(player)

    r = random.randint(0,9)
    text(player,"Level 10\nPrize: 100000 php\n" + level_10[r] + "E. USE LIFELINE\n")
    fifty, call_friend, audience,score = get_ans(player, 30, choice[(r + 2) % 4], choice_small[(r + 2) % 4], fifty, call_friend, audience, 10)
    if score == -1:
        return
    clear(player)

    #round 3
    r = random.randint(0,9)
    text(player,"Level 11\nPrize: 200000 php\n" + level_11[r] + "E. USE LIFELINE\n")
    fifty, call_friend, audience,score = get_ans(player, 45, choice[r % 4], choice_small[r % 4], fifty, call_friend, audience, 11)
    if score == -1:
        return
    clear(player)

    r = random.randint(0,9)
    text(player,"Level 12\nPrize: 300000 php\n" + level_12[r] + "E. USE LIFELINE\n")
    fifty, call_friend, audience,score = get_ans(player, 45, choice[(r + 2) % 4], choice_small[(r + 2) % 4], fifty, call_friend, audience, 12)
    if score == -1:
        return
    clear(player)

    r = random.randint(0,9)
    text(player,"Level 13\nPrize: 400000 php\n" + level_13[r] + "E. USE LIFELINE\n")
    fifty, call_friend, audience,score = get_ans(player, 45, choice[r % 4], choice_small[r % 4], fifty, call_friend, audience, 13)
    if score == -1:
        return
    clear(player)

    r = random.randint(0,9)
    text(player,"Level 14\nPrize: 500000 php\n" + level_14[r] + "E. USE LIFELINE\n")
    fifty, call_friend, audience,score = get_ans(player, 45, choice[(r + 2) % 4], choice_small[(r + 2) % 4], fifty, call_friend, audience, 14)
    if score == -1:
        return
    clear(player)

    r = random.randint(0,9)
    text(player,"Level 15\nPrize: 1000000 php\n" + level_15[r] + "E. USE LIFELINE\n")
    fifty, call_friend, audience,score = get_ans(player, 45, choice[r % 4], choice_small[r % 4], fifty, call_friend, audience, 15)
    if score == -1:
        return
    clear(player)

def clear(player):
    player.send((bytes("$$clr$$", "utf8")))
    time.sleep(0.5)
def text(player, msg):
    player.send((bytes(msg, "utf8")))
    time.sleep(1)
