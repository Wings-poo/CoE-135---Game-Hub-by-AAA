# python3 code
# CoE 135 - My Last Days with You - Dating Sim
# ===================================

from time import sleep
from threading import Timer

BUFSIZ = 1024
BF = "Deredere"
TIMELIMIT = 60 #seconds

# ==== Main ====
def play(room, player):
	clear(player)
	room.datingsim()
	player.send((bytes("My Last Days with You - Dating Sim", "utf8")))
	sleep(1)
	day1(room, player)
	clear(player)
	# day2(room, player)
	# clear(player)
	# day3(room, player)
	# clear(player)
	# day4(room, player)
	# clear(player)
	# day5(room, player)
	# clear(player)
	# day6(room, player)
	clear(player)
	day7(room, player)
	player.send((bytes("\n=========== Game End ===========", "utf8")))
	sleep(0.5)


def day7(room, player):
	winner = max(room.score, key = room.score.get)

	msg = "\n\nDay 7: Our Last day"
	text(player, msg)
	msg = "\n\nToday, Deredere invited everyone to meet up with him."
	text(player, msg)
	msg = "It may be Armageddon but it seems something will happen today."
	text(player, msg)
	msg = "\n%s: I invited everyone here today and I think you all know why." % BF
	text(player, msg)
	msg = "I love you all and I'm happy to have you guys as my friends."
	text(player, msg)
	msg = "You guys were the ones who sticked by me even when I used to be a weakling."
	text(player, msg)
	msg = "I wish to accept all of your confessions but there's only one I can truly accept."
	text(player, msg)
	sleep(2)
	msg = "%s, I accept your confession." % room.user[winner]
	text(player, msg)

	msg = "\n\nAnd the world ended with Deredere and %s as lovers." % room.user[winner]
	text(player, msg)
	sleep(2)
	msg = "\n\n\n\n\nScores are:"
	text(player, msg)
	for i in room.names:
		msg = "%s: %d" % (room.user[i], room.score[i])
		text(player, msg)
	sleep(0.5)



def day1(room, player):

	msg = "\n\nDay 1: Armageddon"
	text(player, msg)
	msg = "\n\nIt was a bright morning today. You're eating breakfast with your friends since childhood."
	text(player, msg)
	msg = "You don't know how you guys were able to stick through after all this time."
	text(player, msg)
	msg = "You're a weird group, after all."
	text(player, msg)

	for i in room.user.values():
		text(player, i)

	msg = "And most importantly, Deredere. The glue of the group.\n"
	text(player, msg)
	msg = "You're watching those weird morning shows as you eat, when the news suddenly popped up."
	text(player, msg)
	msg = "\"Breaking news! NASA has found an asteroid approaching Earth as we speak.\""
	text(player, msg)
	msg = "\"It is said that this asteroid will hit the Earth in 7 days, destroying the world.\""
	text(player, msg)

	sleep(1)
	msg = "\n\nSilence...\n\n"
	text(player, msg)
	sleep(1)

	msg = "Deredere turned off the TV. Leaving, he murmured about needing to clear his head."
	text(player, msg)
	msg = "One by one, you all do the same."
	text(player, msg)

	# Time to choose
	while True:
		msg = "\nWhere do you want to go?"
		msg += "\n1) Home"
		msg += "\n2) Park"
		msg += "\n3) School"
		msg += "\n4) Library"
		text(player, msg)

		ans = int(player.recv(BUFSIZ).decode("utf8"))
		ans -= 1

		if (ans < 4 and ans >= 0) and room.taken[ans] == False:
			room.taken[ans] = True
			room.place[ans] = player

			if ans is 0:
				msg = "You chose to stay at home."
			elif ans is 1:
				msg = "You chose to go to the park."
			elif ans is 2:
				msg = "You chose to go your old school."
			else:
				msg = "You chose to go to the library."
			text(player, msg)
			room.choice += 1
			break

		elif (ans < 4 and ans >= 0) and room.taken[ans] == True:
			msg = "Place is taken."
			player.send(bytes(msg, "utf8"))

		else:
			msg = "%d is invalid." %ans
			player.send(bytes(msg, "utf8"))


	# Wait until everyone has made a choice
	while room.choice < room.num:
		i = 0				# Do nothing

	sleep(0.5)
	if room.taken[0] is True:
		home1(room, player)
	if room.taken[1] is True:
		park1(room, player)
	if room.taken[2] is True:
		schl1(room, player)
	if room.taken[3] is True:
		lib1(room, player)



def home1(room, player):
	room.choice = 0
	name = room.user[room.place[0]]

	clear(player)
	msg = "The house has been quiet since everyone left."
	text(player, msg)
	msg = "The sunlight peaks through the window and the birds continue to chirp."
	text(player, msg)
	msg = "It doesn't feel like the world is ending at all with how peaceful things still are."
	text(player, msg)
	msg = "\n*knock knock*\n"
	text(player, msg)
	msg = "There's someone knocking on the door."
	text(player, msg)
	msg = "\n%s: Hey, %s! Can you let me in?" % (BF, name)
	text(player, msg)
	msg = "\n%s: The door is open. You can come in." % name
	text(player, msg)
	msg = "\n%s: Sorry to bother you but I just need company for a while." % BF
	text(player, msg)
	msg = "How are you holding up?"
	text(player, msg)

	# Time to choose
	if player is room.place[0]:
		msg = "\n1) I guess I'm okay..."
		msg += "\n2) Badly."
		text(player, msg)

		ans = int(player.recv(BUFSIZ).decode("utf8"))

		if ans is 1:
			msg = "\n%s: You could say I'm okay." % name
			gamecast(room.names, msg)
			msg = "Not bad but not good either. Just okay."
			gamecast(room.names, msg)
			room.score[player] += 5

		elif ans is 2:
			msg = "\n%s: I'm not taking this well." % name
			gamecast(room.names, msg)
			msg = "How could the world just end?"
			gamecast(room.names, msg)
			room.score[player] += 3

		else:
			msg = "\n%s: Speechless still, huh?" % BF
			gamecast(room.names, msg)
			msg = "I can understand that."
			gamecast(room.names, msg)
			msg = "\n%s: ..." % name
			gamecast(room.names, msg)
			room.score[player] += 7

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\n%s: Yeah. Finding out the world is ending..." % BF
	text(player, msg)
	msg = "It's really shocking."
	text(player, msg)
	msg = "I can't accept it still because there's so many things I want to do."
	text(player, msg)
	msg = "I won't be able to achieve any of that."
	text(player, msg)
	msg = "I feel so bitter."
	text(player, msg)
	msg = "..."
	text(player, msg)
	sleep(1)
	msg = "Sorry. I just needed to vent..."
	text(player, msg)
	msg = "I'll leave you now."
	text(player, msg)

	msg = "\nDeredere left."
	text(player, msg)
	sleep(3)



def park1(room, player):
	room.choice = 0
	name = room.user[room.place[1]]

	clear(player)
	msg = "The park is void of any people."
	text(player, msg)
	msg = "I guess it should be expected when the world is ending."
	text(player, msg)
	msg = "Yet with how peaceful this place is, no one would have thought it'll be gone in 7 days."
	text(player, msg)
	msg = "\n%s: Hey, %s!" %(BF, name)
	text(player, msg)
	msg = "I didn't expect to see you here."
	text(player, msg)
	msg = "\n%s: Neither do I." % name
	text(player, msg)
	msg = "What brings you here?"
	text(player, msg)
	msg = "\n%s: Just going around and about." % BF
	text(player, msg)
	msg = "I don't feel at ease at home so I decided to wander instead."
	text(player, msg)
	msg = "How about you? Why are you here?"
	text(player, msg)

	# Time to choose
	if player is room.place[1]:
		msg = "\n1) Same as you."
		msg += "\n2) I want to be alone."
		text(player, msg)

		ans = int(player.recv(BUFSIZ).decode("utf8"))

		if ans is 1:
			msg = "\n%s: Same reason. I want to be somewhere else." % name
			gamecast(room.names, msg)
			room.score[player] += 7

		elif ans is 2:
			msg = "\n%s: I want to be alone..." % name
			gamecast(room.names, msg)
			room.score[player] += 5

		else:
			msg = "\n%s: You don't want to say, huh?" % BF
			gamecast(room.names, msg)
			msg = "\n%s: I'm sorry." % name
			gamecast(room.names, msg)
			room.score[player] += 3

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\n%s: It's fine. We have our reasons." % BF
	text(player, msg)
	msg = "..."
	text(player, msg)
	sleep(1)
	msg = "Is it okay if I accompany you for awhile?"
	text(player, msg)
	msg = "\n%s: It's fine. I don't mind." % name
	text(player, msg)
	msg = "\n%s: Thanks :)" % BF
	text(player, msg)
	msg = "\nYou both stayed for a little longer."
	text(player, msg)
	sleep(3)



def schl1(room, player):
	room.choice = 0
	name = room.user[room.place[2]]

	clear(player)
	msg = "Walking about, you found yourself back at your old school."
	text(player, msg)
	msg = "It's giving you mixed feelings."
	text(player, msg)
	msg = "You wish you could go back to when you're kids."
	text(player, msg)
	msg = "No worries to think about. No world is ending."
	text(player, msg)
	msg = "Just ignorant bliss..."
	text(player, msg)
	msg = "You spot Deredere walking down. You called out to him."
	text(player, msg)
	msg = "\n%s: Oh! Hey, %s." %(BF, name)
	text(player, msg)
	msg = "What's up?"
	text(player, msg)

	# Time to choose
	if player is room.place[2]:
		msg = "\n1) I'm lost."
		msg += "\n2) Hi."
		text(player, msg)

		ans = int(player.recv(BUFSIZ).decode("utf8"))

		if ans is 1:
			msg = "\n%s: I'm lost. Can you help me?" % name
			gamecast(room.names, msg)
			msg = "\n%s: Well aren't you funny." % BF
			gamecast(room.names, msg)
			room.score[player] += 5

		elif ans is 2:
			msg = "\n%s: I saw you and I wanted to say hi." % name
			gamecast(room.names, msg)
			msg = "\n%s: Even though we saw each other this morning?" % BF
			gamecast(room.names, msg)
			msg = "\n%s: Shut up! Don't tease me." % name
			gamecast(room.names, msg)
			room.score[player] += 7

		else:
			msg = "\n%s: Wow~ Calling me out then shutting up." % BF
			gamecast(room.names, msg)
			msg = "You're so nice." % BF
			gamecast(room.names, msg)
			room.score[player] += 3

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "Haha."
	text(player, msg)
	sleep(1)
	msg = "I'm guessing you're here to calm down?"
	text(player, msg)
	msg = "\n%s: Yeah. I was just walking along this path in auto-pilot." % name
	text(player, msg)
	msg = "Didn't expect that it'll lead me here."
	text(player, msg)
	msg = "\n%s: The same goes for me too." % BF
	text(player, msg)
	msg = "Though I wish I didn't end up here. Ugh, school."
	text(player, msg)
	msg = "\n%s: Hey! School wasn't that bad. You just suck." % name
	text(player, msg)
	msg = "\n%s: Why you gotta be so rude? D:" % BF
	text(player, msg)
	msg = "Haha. Anyways, I want to walk around more."
	text(player, msg)
	msg = "I'll see you when I see you?"
	text(player, msg)
	msg = "\n%s: Yeah. I'll see you." % name
	text(player, msg)
	msg = "\nYou parted ways."
	text(player, msg)
	sleep(3)



def lib1(room, player):
	room.choice = 0
	name = room.user[room.place[3]]

	clear(player)
	msg = "The library is surprisingly open."
	text(player, msg)
	msg = "I guess there's people who rather continue their work than stay at home."
	text(player, msg)
	msg = "I should do that too but..."
	text(player, msg)
	msg = "Is there a point still?..."
	text(player, msg)
	sleep(1)
	msg = "I guess I should be thankful there's a place I can go to still."
	text(player, msg)
	msg = "You went inside."
	text(player, msg)
	msg = "You breathed in the airconditioned air when someone tapped you on the shoulder."
	text(player, msg)
	msg = "\n%s: Deredere!" % name
	text(player, msg)
	msg = "\n%s: Shhh~ Don't you know you're in the library? Haha." % BF
	text(player, msg)

	# Time to choose
	if player is room.place[3]:
		msg = "\n1) You don't read."
		msg += "\n2) Why are you here?"
		text(player, msg)

		ans = int(player.recv(BUFSIZ).decode("utf8"))

		if ans is 1:
			msg = "\n%s: I would have made a mistake that I'm in a library." % name
			gamecast(room.names, msg)
			msg = "As far as I know, you don't read." % BF
			gamecast(room.names, msg)
			msg = "\n%s: D:" % BF
			gamecast(room.names, msg)
			room.score[player] += 3

		elif ans is 2:
			msg = "\n%s: What are you doing here?" % name
			gamecast(room.names, msg)
			msg = "\n%s: Am I not allowed to be here?" % BF
			gamecast(room.names, msg)
			room.score[player] += 5

		else:
			msg = "\n%s: Why are you looking at me with those judging eyes?" % BF
			gamecast(room.names, msg)
			msg = "\n%s: ..." % name
			gamecast(room.names, msg)
			msg = "\n%s: Stop it. Why are you so mean? D:" % BF
			gamecast(room.names, msg)
			room.score[player] += 7

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\n%s: I'm just surprised to find you here." % name
	text(player, msg)
	msg = "You more of a sporty-type than a book-type."
	text(player, msg)
	msg = "\n%s: Then I'm breaking the status quo just by being here." % BF
	text(player, msg)
	msg = "\n%s: When the world is about to end?" % name
	text(player, msg)
	msg = "\n%s: Better late than never. Don't you think so, %s?" % (BF, name)
	text(player, msg)
	msg = "Want to go look around?"
	text(player, msg)
	msg = "\n%s: Sure. Doing something different sounds nice." % name
	text(player, msg)
	msg = "\nYou explored the library together."
	text(player, msg)
	sleep(3)



# ==== Broadcasts a message to all players in the room ====
def gamecast(players, msg):

	for sock in players:
		sock.send(bytes(msg, "utf8"))

	sleep(1)



# ==== Send game text ====
def text(player, msg):
	player.send(bytes(msg, "utf8"))
	sleep(1)



# ==== Calls clear screen in client ====
def clear(player):
	player.send((bytes("$$clr$$", "utf8")))
	sleep(0.5)



# ==== Initialize the variables ====
def init(room):
	self.place = []
	self.taken = []
	self.choice = 0

	for i in range(4):
		self.place.append("")
		self.taken.append(False)



# ===================================
# Code and info gotten from these websites:
# https://stackoverflow.com/questions/7002429/how-can-i-extract-all-values-from-a-dictionary-in-python
# https://docs.python.org/3/library/threading.html#timer-objects
# https://stackoverflow.com/questions/53453887/how-to-set-a-time-limit-for-a-game
# ===================================
