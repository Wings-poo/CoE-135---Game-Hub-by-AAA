# python3 code
# CoE 135 - Hangman
# ===================================

import random

# ==== Global variables ====
game_state = False;
guesses = 0;
word = ""
word_list = []
guess_list = []
blanks_list = []
new_blanks_list = []
BUFSIZ = 1024;

# === Game ====
# This is a word game

# ==== Game broadcast ====
def game_broadcast(msg, clients):

	for sock in clients:
		sock.send(msg);

def print_scaffold(guesses, wd, clients): # prints the scaffold
	global game_state
	if (guesses == 0):
		game_broadcast(bytes("_________\n", "utf8"), clients)
		game_broadcast(bytes("|	 |\n", "utf8"), clients)
		game_broadcast(bytes("|\n", "utf8"), clients)
		game_broadcast(bytes("|\n", "utf8"), clients)
		game_broadcast(bytes("|\n", "utf8"), clients)
		game_broadcast(bytes("|\n", "utf8"), clients)
		game_broadcast(bytes("|________\n", "utf8"), clients)
	elif (guesses == 1):
		game_broadcast(bytes("_________\n", "utf8"), clients)
		game_broadcast(bytes("|	 |\n", "utf8"), clients)
		game_broadcast(bytes("|	 O\n", "utf8"), clients)
		game_broadcast(bytes("|\n", "utf8"), clients)
		game_broadcast(bytes("|\n", "utf8"), clients)
		game_broadcast(bytes("|\n", "utf8"), clients)
		game_broadcast(bytes("|________\n", "utf8"), clients)
	elif (guesses == 2):
		game_broadcast(bytes("_________\n", "utf8"), clients)
		game_broadcast(bytes("|	 |\n", "utf8"), clients)
		game_broadcast(bytes("|	 O\n", "utf8"), clients)
		game_broadcast(bytes("|	 |\n", "utf8"), clients)
		game_broadcast(bytes("|	 |\n", "utf8"), clients)
		game_broadcast(bytes("|\n", "utf8"), clients)
		game_broadcast(bytes("|________\n", "utf8"), clients)
	elif (guesses == 3):
		game_broadcast(bytes("_________\n", "utf8"), clients)
		game_broadcast(bytes("|	 |\n", "utf8"), clients)
		game_broadcast(bytes("|	 O\n", "utf8"), clients)
		game_broadcast(bytes("|	\|\n", "utf8"), clients)
		game_broadcast(bytes("|	 |\n", "utf8"), clients)
		game_broadcast(bytes("|\n", "utf8"), clients)
		game_broadcast(bytes("|________\n", "utf8"), clients)
	elif (guesses == 4):
		game_broadcast(bytes("_________\n", "utf8"), clients)
		game_broadcast(bytes("|	 |\n", "utf8"), clients)
		game_broadcast(bytes("|	 O\n", "utf8"), clients)
		game_broadcast(bytes("|	\|/\n", "utf8"), clients)
		game_broadcast(bytes("|	 |\n", "utf8"), clients)
		game_broadcast(bytes("|\n", "utf8"), clients)
		game_broadcast(bytes("|________\n", "utf8"), clients)
	elif (guesses == 5):
		game_broadcast(bytes("_________\n", "utf8"), clients)
		game_broadcast(bytes("|	 |\n", "utf8"), clients)
		game_broadcast(bytes("|	 O\n", "utf8"), clients)
		game_broadcast(bytes("|	\|/\n", "utf8"), clients)
		game_broadcast(bytes("|	 |\n", "utf8"), clients)
		game_broadcast(bytes("|	/ \n", "utf8"), clients)
		game_broadcast(bytes("|________\n", "utf8"), clients)
	elif (guesses == 6):
		game_broadcast(bytes("_________\n", "utf8"), clients)
		game_broadcast(bytes("|	 |\n", "utf8"), clients)
		game_broadcast(bytes("|	 O\n", "utf8"), clients)
		game_broadcast(bytes("|	\|/\n", "utf8"), clients)
		game_broadcast(bytes("|	 |\n", "utf8"), clients)
		game_broadcast(bytes("|	/ \ \n", "utf8"), clients)
		game_broadcast(bytes("|________\n", "utf8"), clients)
		game_broadcast(bytes("\nThe word was %s.\n" %wd, "utf8"), clients)
		game_broadcast(bytes("\nYOU LOSE! TRY AGAIN!", "utf8"), clients)
		game_state = False
		return

def selectWord():
	file = open('FREQ')
	words = file.readlines()
	myword = 'a'
	while len(myword) < 4: # makes sure word is at least 4 letters long
		myword = random.choice(words)
		myword = str(myword).strip('[]')
		myword = str(myword).strip("''")
		myword = str(myword).strip("\n")
		myword = str(myword).strip("\r")
		myword = myword.lower()
	return myword


def hangMan(client, clients):
	global game_state;
	global guesses
	global word
	global word_list
	global guess_list
	global blanks_list
	global new_blanks_list

	while guesses < 6 and game_state == True:
		guess = client.recv(BUFSIZ).decode("utf8");
		guess = guess.lower()

		if game_state == False:
			break;

		if len(guess) > 1:
			game_broadcast(bytes("Stop cheating! Enter one letter at time.", "utf8"), clients)
		elif guess == "":
			game_broadcast(bytes("Don't you want to play? Enter one letter at a time.", "utf8"), clients)
		elif guess in guess_list:
			game_broadcast(bytes("You already guessed that letter! Here is what you've guessed:", "utf8"), clients)
			game_broadcast(bytes(' '.join(guess_list), "utf8"), clients)
		else:
			guess_list.append(guess)
			i = 0
			while i < len(word):
				if guess == word[i]:
					new_blanks_list[i] = word_list[i]
				i = i+1

			if new_blanks_list == blanks_list:
				game_broadcast(bytes("%s isn't here." %guess, "utf8"), clients)
				guesses = guesses + 1
				print_scaffold(guesses, word, clients)

				if guesses < 6:
					game_broadcast(bytes("Guess again.", "utf8"), clients)
					game_broadcast(bytes(' '.join(blanks_list), "utf8"), clients)

			elif word_list != blanks_list:

				blanks_list = new_blanks_list[:]
				game_broadcast(bytes(' '.join(blanks_list), "utf8"), clients)

				if word_list == blanks_list:
					game_broadcast(bytes("\nYOU WIN! Here is your prize: ", "utf8"), clients)
					game_broadcast(bytes("UwU\n", "utf8"), clients)

					game_state = False;
					return;

				else:
					game_broadcast(bytes("Great guess! Guess another!", "utf8"), clients)
