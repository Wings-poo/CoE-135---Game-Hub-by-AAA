import random
import sys
import time

def menu():
    print("WHO WANTS TO BE A MILLIONAIRE?\nPress spacebar to start\nPress ? for help\nPress other keys to exit\n")
    menu_press = input()
    if menu_press == '?':
        help_menu()
    elif menu_press == ' ':
        play()
    else:
        sys.exit()

def help_menu():
    print("__________\nHow to play?\n\nWho Wants to Be a Millionaire is a trivia game involving a series of trivia questions.\nWhat you have to do is answer each questions within the  time limit, which varies per round.\nThere is a total of three rounds with five questions per each round.\nYou will have 15 seconds to answer on the first round, 30 seconds on the second and 45 seconds on the third.\nYour score will be equivalent to the cash prize of the highest correct level that you answered.\n\nGOOD LUCK!\n___________\n")
    menu()

def play():
    choice = ["A", "B", "C", "D"]
    choice_small = ["a", "b", "c", "d"]

    #level 1
    level_1 = ["What is the first letter of the Alphabet?\nA. A\nB. B\nC. C\nD. D", "The female deer is known as?\nA. jill\nB. doe\nC. flyer\nD. hen\n", "Who among the following is a national hero of the Philippines?\nA. Marian Rivera\nB. James Reid\nC. Jose Rizal\nD. Sir Briones\n", "What is the currency of the Philippines?\nA. Dollar\nB. Yen\nC. Won\nD. Peso\n", "How many continents are in the world?\nA. 7\nB. 6\nC. 5\nD. 4","What is the formula for water?\nA. H3O\nB. H2O\nC. H3O2\nD. H2O2\n","How many sides a pentagon has?\nA. 3\nB. 4\nC. 5\nD. 6\n", "Up above the world so high, like a diamond in the sky. Which poem do the lyrics belong to?\nA. Old Macdonald\nB. Three Little Pigs\nC. Mary Had a Little Lamb\nD. Twinkle Twinkle Little Star\n", "What is the chemical Symbol for Oxygen?\nA. O\nB. C\nC. H\nD. He\n", "What is the largest planet?\nA. Earth\nB. Jupiter\nC. Sun\nD. Mars\n)"]

    r = random.randint(0,9)
    print(level_1[r])
    ans = input("Answer: ")
    if (ans == choice[r % 4]) | (ans == choice_small[r % 4]):
        print("correct!!\n")
    else:
        print("not correct!!\n")

menu()
