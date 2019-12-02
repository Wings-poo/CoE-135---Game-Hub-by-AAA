# python3 code
# CoE 135 - My Last Days with You - Dating Sim
# ===================================

from time import sleep
import socket

BUFSIZ = 1024
BF = "Deredere"
TIMELIMIT = 30 #seconds

# ==== Main ====
def play(room, player):
	clear(player)
	room.datingsim()
	player.send((bytes("My Last Days with You - Dating Sim", "utf8")))
	sleep(1)
	day1(room, player)
	clear(player)
	day2(room, player)
	clear(player)
	day3(room, player)
	clear(player)
	day4(room, player)
	clear(player)
	day5(room, player)
	clear(player)
	day6(room, player)
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
	msg = "It may be Armageddon but it seems something more interesting will happen today."
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
	msg = "\n%s, I accept your confession." % room.user[winner]
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
	player.settimeout(None)

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
	player.settimeout(TIMELIMIT)
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
		msg = "\n1) I guess I'm okay."
		msg += "\n2) Badly."
		text(player, msg)

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

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

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

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


	msg = "\n%s: I see. It's fine. We have our reasons." % BF
	text(player, msg)
	msg = "..."
	text(player, msg)
	sleep(1)
	msg = "Is it okay if I accompany you for awhile?"
	text(player, msg)
	msg = "\n%s: It's fine. I don't mind." % name
	text(player, msg)
	msg = "\n%s: Thanks." % BF
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

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

		if ans is 1:
			msg = "\n%s: I'm lost. Can you help me?" % name
			gamecast(room.names, msg)
			msg = "\n%s: Well aren't you funny." % BF
			gamecast(room.names, msg)
			msg = "\n%s: I can't help it. I got lost in your eyes." % name
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
			msg = "You're so nice."
			gamecast(room.names, msg)
			msg = "\n%s: My mind went blank for a second. Sheesh." % name
			gamecast(room.names, msg)
			msg = "Give me a break."
			gamecast(room.names, msg)
			room.score[player] += 3

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\n%s: Haha." % BF
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
	msg = "\n%s: Why you gotta be so rude?" % BF
	text(player, msg)
	sleep(1)
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
	msg = "You guess there's people who rather continue their work than stay at home."
	text(player, msg)
	msg = "You should do that too but..."
	text(player, msg)
	msg = "Is there a point still?"
	text(player, msg)
	sleep(1)
	msg = "You guess you should be thankful there's a place you can go to still."
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

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

		if ans is 1:
			msg = "\n%s: I would have made a mistake that I'm in a library." % name
			gamecast(room.names, msg)
			msg = "As far as I know, you don't read."
			gamecast(room.names, msg)
			msg = "\n%s: Rude!" % BF
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
			msg = "\n%s: Stop it. Why are you so mean?" % BF
			gamecast(room.names, msg)
			room.score[player] += 7

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\n%s: I'm just surprised to find you here." % name
	text(player, msg)
	msg = "You're more of a sporty-type than a book-type."
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



def day2(room, player):
	init(room)
	player.settimeout(None)

	msg = "\n\nDay 2: Our Present"
	text(player, msg)
	msg = "\n\nA day has passed since the end of the world has been announced."
	text(player, msg)
	msg = "Instead of going to work, you decided to waste the day somewhere."
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
	player.settimeout(TIMELIMIT)
	if room.taken[0] is True:
		home2(room, player)
	if room.taken[1] is True:
		park2(room, player)
	if room.taken[2] is True:
		schl2(room, player)
	if room.taken[3] is True:
		lib2(room, player)



def home2(room, player):
	room.choice = 0
	name = room.user[room.place[0]]

	clear(player)
	msg = "You've always dreamt of staying at home and doing nothing."
	text(player, msg)
	msg = "That dream is now a reality."
	text(player, msg)
	msg = "The difference is Deredere isn't here."
	text(player, msg)
	msg = "..."
	text(player, msg)
	sleep(1)
	msg = "You guess there's nothing wrong in making that part into reality."
	text(player, msg)
	msg = "You called Deredere."
	text(player, msg)
	msg = "You wait for him to pick up."
	text(player, msg)
	msg = "\n%s: Hello?" % BF
	text(player, msg)

	# Time to choose
	if player is room.place[0]:
		msg = "\n1) Prank him."
		msg += "\n2) Talk."
		text(player, msg)

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

		if ans is 1:
			msg = "\n%s: Is your refrigerator running?" % name
			gamecast(room.names, msg)
			msg = "\n%s: Yes?" % BF
			gamecast(room.names, msg)
			msg = "\n%s: Then you better catch it. HAHAHAHAHA!" % name
			gamecast(room.names, msg)
			room.score[player] += 7

		elif ans is 2:
			msg = "\n%s: Hi." % name
			gamecast(room.names, msg)
			msg = "\n%s: Ummm... Why did you call?" % BF
			gamecast(room.names, msg)
			msg = "\n%s: I just wanted to talk." % name
			gamecast(room.names, msg)
			msg = "\n%s: Okay then." % BF
			gamecast(room.names, msg)
			msg = "\n%s: ..." % name
			gamecast(room.names, msg)
			sleep(1)
			msg = "\n%s: ..." % BF
			gamecast(room.names, msg)
			sleep(1)
			msg = "\n%s: ..." % name
			gamecast(room.names, msg)
			sleep(1)
			room.score[player] += 5

		else:
			msg = "\n%s: Ummm, hello?" % BF
			gamecast(room.names, msg)
			msg = "%s, you do know I can see who's calling me right?" % name
			gamecast(room.names, msg)
			msg = "\n%s: Uhhh... Damn it." % name
			gamecast(room.names, msg)
			room.score[player] += 3

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\n%s: What is wrong with you? Haha." % BF
	text(player, msg)
	msg = "\n%s: Shut up. I called because I wanted to talk but now I'm blanking out." % name
	text(player, msg)
	msg = "\n%s: Ahhh." % BF
	text(player, msg)
	msg = "\n%s: I want to ask \"How are you\" but that seems weird." % name
	text(player, msg)
	msg = "So how about \"What's cooking, good looking?\""
	text(player, msg)
	msg = "\n%s: HAHA. Is that how we're going to do this?" % BF
	text(player, msg)
	msg = "\n%s: Why not? Hahaha." % name
	text(player, msg)
	msg = "\n%s: Okay then. I don't mind." % BF
	text(player, msg)
	msg = "\nYou conversed more with Deredere."
	text(player, msg)
	sleep(3)



def park2(room, player):
	room.choice = 0
	name = room.user[room.place[1]]

	clear(player)
	msg = "You don't know what's gotten into you but exercising in the park means it's probably the devil."
	text(player, msg)
	msg = "You haven't jogged since..."
	text(player, msg)
	msg = "..."
	text(player, msg)
	sleep(1)
	msg = "You've never jogged at all. At least, not by your choice."
	text(player, msg)
	msg = "The only reason you jogged before is because Deredere is there to push you."
	text(player, msg)
	sleep(1)
	msg = "\n%s: The world may be ending but it seems miracles continue to happen." % BF
	text(player, msg)
	msg = "\nIt seems Deredere is also jogging."
	text(player, msg)
	msg = "\n%s: I didn't ask for your opinion, did I?" % name
	text(player, msg)
	msg = "\n%s: Harsh. Haha." % BF
	text(player, msg)
	sleep(1)
	msg = "So what's gotten into you that you're jogging now?"
	text(player, msg)

	# Time to choose
	if player is room.place[1]:
		msg = "\n1) It clears my mind."
		msg += "\n2) I want to die sexy."
		text(player, msg)

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

		if ans is 1:
			msg = "\n%s: Surprisingly, jogging clears my mind." % name
			gamecast(room.names, msg)
			msg = "Though it could also be the devil possessing me. Hahaha."
			gamecast(room.names, msg)
			room.score[player] += 7

		elif ans is 2:
			msg = "\n%s: I want to die sexy." % name
			gamecast(room.names, msg)
			msg = "\n%s: Oh wow. Haha." % BF
			gamecast(room.names, msg)
			msg = "\n%s: Hahaha." % name
			gamecast(room.names, msg)
			room.score[player] += 5

		else:
			msg = "\n%s: Why are you staying quiet?" % BF
			gamecast(room.names, msg)
			msg = "Are you hiding something from me?"
			gamecast(room.names, msg)
			msg = "\n%s: I'm not. I just wanted to jog, is all." % name
			gamecast(room.names, msg)
			sleep(1)
			room.score[player] += 3

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\n%s: It's nice seeing you jog though." % BF
	text(player, msg)
	msg = "I've always have to force you to jog with me."
	text(player, msg)
	msg = "\n%s: Why do you want to jog with me in the first place?" % name
	text(player, msg)
	msg = "\n%s: I've always wanted to jog with someone." % BF
	text(player, msg)
	msg = "If I'm going to find that someone, might as well be you."
	text(player, msg)
	msg = "\n%s: ..." % name
	text(player, msg)
	sleep(1)
	msg = "\n%s: Come on! Let's have 5 more laps." % BF
	text(player, msg)
	msg = "\n%s: WHAT?!?" % name
	text(player, msg)
	msg = "\nYou let Deredere drag you around."
	text(player, msg)
	sleep(3)



def schl2(room, player):
	room.choice = 0
	name = room.user[room.place[2]]

	clear(player)
	msg = "You invited Deredere to accompany you to your old school."
	text(player, msg)
	msg = "Might as well go down memory lane with someone."
	text(player, msg)
	msg = "You both decided to roam around the grade school area."
	text(player, msg)
	msg = "You wait by the entrance."
	text(player, msg)
	msg = "\n%s: Did you wait long?" % BF
	text(player, msg)
	msg = "\n%s: A bit but I don't mind waiting for you." % name
	text(player, msg)
	msg = "\n%s: Well then, where do you want to go?" % BF
	text(player, msg)

	# Time to choose
	if player is room.place[2]:
		msg = "\n1) Classrooms."
		msg += "\n2) Playground."
		text(player, msg)

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

		if ans is 1:
			msg = "\n%s: Let's go to the classrooms." % name
			gamecast(room.names, msg)
			msg = "\n%s: Sure. Let's go." % BF
			gamecast(room.names, msg)
			room.score[player] += 3

		elif ans is 2:
			msg = "\n%s: Let's go to the playground." % name
			gamecast(room.names, msg)
			msg = "\n%s: I guess some things never change, huh?" % BF
			gamecast(room.names, msg)
			msg = "\n%s: Come on! I want to slide." % name
			gamecast(room.names, msg)
			msg = "\n%s: Okay okay. Haha." % BF
			gamecast(room.names, msg)
			room.score[player] += 7

		else:
			msg = "\n%s: Can't pick?" % BF
			gamecast(room.names, msg)
			msg = "\n%s: Sorry." % name
			gamecast(room.names, msg)
			msg = "We can go around wherever. Let our feet take us there."
			gamecast(room.names, msg)
			msg = "\n%s: Sounds good to me." % BF
			gamecast(room.names, msg)
			room.score[player] += 5

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\n%s: Hey, do you remember when we were kids, we would send each other notes?" % name
	text(player, msg)
	msg = "No matter how far apart our chairs are, we always find a way to send it to each other."
	text(player, msg)
	msg = "\n%s: Oh! I remember that." % BF
	text(player, msg)
	msg = "I usually get caught though."
	text(player, msg)
	msg = "\n%s: It's because you're bad at being discreet." % name
	text(player, msg)
	msg = "Even if I'm at the front and you're at the back, I can tell that you're passing paper."
	text(player, msg)
	msg = "You're really bad at it."
	text(player, msg)
	msg = "\n%s: Come on! It's all in the past." % BF
	text(player, msg)
	msg = "I'm better now, I swear."
	text(player, msg)
	msg = "\n%s: Sure sure. Hahaha." % name
	text(player, msg)
	msg = "\nYou enjoyed reminiscing together."
	text(player, msg)
	sleep(3)



def lib2(room, player):
	room.choice = 0
	name = room.user[room.place[3]]

	clear(player)
	msg = "You went to the library with Deredere."
	text(player, msg)
	msg = "You want to borrow a book now that you have time to read."
	text(player, msg)
	msg = "Deredere decided to join for whatever reason."
	text(player, msg)
	msg = "You don't mind though. You like his company."
	text(player, msg)
	msg = "You watch him look around the bookshelves with wonder."
	text(player, msg)

	# Time to choose
	if player is room.place[3]:
		msg = "\n1) You're a child."
		msg += "\n2) You find something interesting?"
		text(player, msg)

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

		if ans is 1:
			msg = "\n%s: You look like a child in a candy shop." % name
			gamecast(room.names, msg)
			msg = "\n%s: Do I? Haha." % BF
			gamecast(room.names, msg)
			msg = "I didn't expect that the library will look so colorful."
			gamecast(room.names, msg)
			msg = "I expected it to be bland and boring."
			gamecast(room.names, msg)
			msg = "This is..."
			gamecast(room.names, msg)
			sleep(1)
			msg = "This is really nice."
			gamecast(room.names, msg)
			msg = "\n%s: I'm glad you're enjoying yourself." % name
			gamecast(room.names, msg)
			msg = "\n%s: Thanks for letting me accompany you." % BF
			gamecast(room.names, msg)
			room.score[player] += 5

		elif ans is 2:
			msg = "\n%s: Find something interesting?" % name
			gamecast(room.names, msg)
			msg = "\n%s: Nope. I'm just at awe at how many books there are." % BF
			gamecast(room.names, msg)
			msg = "I rarely go here because I expected that libraries are boring."
			gamecast(room.names, msg)
			msg = "If I'm going to be here, it's only because I have to."
			gamecast(room.names, msg)
			msg = "Not because I want to."
			gamecast(room.names, msg)
			msg = "\n%s: Nice to know your change of heart." % name
			gamecast(room.names, msg)
			msg = "\n%s: It's all thanks to you." % BF
			gamecast(room.names, msg)
			room.score[player] += 3

		else:
			msg = "You let him be."
			gamecast(room.names, msg)
			msg = "Instead of looking for a book to read, you find your eyes drawing to him."
			gamecast(room.names, msg)
			msg = "Even if the world ends, Deredere will always be Deredere."
			gamecast(room.names, msg)
			sleep(1)
			room.score[player] += 7

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\nYou enjoyed the silence together as you continue to pick your book."
	text(player, msg)
	sleep(3)



def day3(room, player):
	init(room)
	player.settimeout(None)

	msg = "\n\nDay 3: Our Favorite Memory"
	text(player, msg)
	msg = "\n\nAnother day has passed."
	text(player, msg)
	msg = "You decided to go back to work."
	text(player, msg)
	msg = "There's less people in the office but it seems you're not the only one who decided to go back."
	text(player, msg)
	msg = "You talked to your coworkers."
	text(player, msg)
	msg = "And the day passed by, just like any other."
	text(player, msg)
	sleep(1)
	msg = "It's late afternoon. There's still time."
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
				msg = "You chose to go back home."
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
	player.settimeout(TIMELIMIT)
	if room.taken[1] is True:
		park3(room, player)
	if room.taken[2] is True:
		schl3(room, player)
	if room.taken[0] is True:
		home3(room, player)
	if room.taken[3] is True:
		lib3(room, player)



def home3(room, player):
	room.choice = 0
	name = room.user[room.place[0]]

	clear(player)
	msg = "As you were walking home, you passed by Deredere's house."
	text(player, msg)
	msg = "The lights inside are on. It seems he's home."
	text(player, msg)
	msg = "You decided to visit him before going straight home."
	text(player, msg)
	msg = "You went up his house and knocked on his door."
	text(player, msg)
	msg = "\n%s: This is a surprise. It's not even the weekend and you're here." % BF
	text(player, msg)
	msg = "\n%s: What? I can't visit my dear friend? Hahaha." % name
	text(player, msg)
	msg = "\n%s: I don't know. You might be burglar for all I know." % BF
	text(player, msg)
	msg = "Haha. I'm kidding."
	text(player, msg)
	msg = "You know you're always welcome here."
	text(player, msg)
	msg = "Come in."
	text(player, msg)
	msg = "\nYou entered his home and sat on his couch."
	text(player, msg)
	msg = "\n%s: You visiting suddenly makes me nostalgic." % BF
	text(player, msg)

	# Time to choose
	if player is room.place[0]:
		msg = "\n1) Bring up embarrassing memory."
		msg += "\n2) Bring up favorite memory."
		text(player, msg)

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

		if ans is 1:
			msg = "\n%s: Hmmm~ Is you crying for your mom whenever you lost make you nostalgic?" % name
			gamecast(room.names, msg)
			msg = "\n%s: Hey! Why must you ruin the mood?" % BF
			gamecast(room.names, msg)
			msg = "I am trying to be wholesome here."
			gamecast(room.names, msg)
			msg = "Thank you very much."
			gamecast(room.names, msg)
			msg = "\n%s: You're just easy to tease. Hahaha." % name
			gamecast(room.names, msg)
			room.score[player] += 5

		elif ans is 2:
			msg = "\n%s: Remember when we used to build a pillow fort in your house?" % name
			gamecast(room.names, msg)
			msg = "\n%s: Oh yeah!" % BF
			gamecast(room.names, msg)
			msg = "You guys will bring your own pillows from home."
			gamecast(room.names, msg)
			msg = "Then you'll run back to mine and we practically covered the living room with pillows."
			gamecast(room.names, msg)
			msg = "\n%s: That's my favorite memory." % name
			gamecast(room.names, msg)
			msg = "It was so fun."
			gamecast(room.names, msg)
			room.score[player] += 7

		else:
			msg = "\n%s: Haha. Sorry about that." % BF
			gamecast(room.names, msg)
			msg = "I ruined the atmosphere."
			gamecast(room.names, msg)
			msg = "\n%s: No no. It's fine." % name
			gamecast(room.names, msg)
			msg = "..."
			gamecast(room.names, msg)
			sleep(1)
			room.score[player] += 3

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\n%s: We've grown up. Haven't we?" % BF
	text(player, msg)
	msg = "\n%s: Yeah." % name
	text(player, msg)
	msg = "But I'm happy to have experience those memories at all."
	text(player, msg)
	msg = "\n%s: Me too." % BF
	text(player, msg)
	msg = "..."
	text(player, msg)
	sleep(1)
	msg = "Want to stay for dinner? I'm making mashed potatoes."
	text(player, msg)
	msg = "\n%s: Sure. Free food is free food. Hahaha" % name
	text(player, msg)
	msg = "\nYou stayed to eat dinner."
	text(player, msg)
	sleep(3)



def park3(room, player):
	room.choice = 0
	name = room.user[room.place[1]]

	clear(player)
	msg = "The park looks different in the late afternoon sun."
	text(player, msg)
	msg = "You saw Deredere jogging."
	text(player, msg)
	msg = "It seems he's on his way home."
	text(player, msg)
	msg = "You called out to him."
	text(player, msg)
	msg = "\n%s: Oh hey!" % BF
	text(player, msg)
	msg = "Are you here to have an evening jog?"
	text(player, msg)
	msg = "\n%s: No. I just got off from work and decided to come here in the mean time." % name
	text(player, msg)
	msg = "\n%s: Ahhh, you should try it. Evening jogs are fun." % BF
	text(player, msg)
	msg = "I know! You should join me!"
	text(player, msg)

	# Time to choose
	if player is room.place[1]:
		msg = "\n1) I'll think about it."
		msg += "\n2) No."
		text(player, msg)

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

		if ans is 1:
			msg = "\n%s: I'll think about it." % name
			gamecast(room.names, msg)
			msg = "\n%s: That's not a yes." % BF
			gamecast(room.names, msg)
			msg = "\n%s: It's not a no either. Hahaha." % name
			gamecast(room.names, msg)
			room.score[player] += 7

		elif ans is 2:
			msg = "\n%s: No, thank you." % name
			gamecast(room.names, msg)
			msg = "\n%s: Wow. No right from the start?" % BF
			gamecast(room.names, msg)
			msg = "\n%s: I don't like to exercise though." % name
			gamecast(room.names, msg)
			room.score[player] += 3

		else:
			msg = "\n%s: You look conflicted. Don't force yourself. Haha." % BF
			gamecast(room.names, msg)
			msg = "\n%s: It sounds appealing coming from you." % name
			gamecast(room.names, msg)
			msg = "My want to be healthy is telling yes."
			gamecast(room.names, msg)
			msg = "But my lazy bum is screaming no. Hahaha."
			gamecast(room.names, msg)
			room.score[player] += 5

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\n%s: Well, think about my offer more." % BF
	text(player, msg)
	msg = "You never know. You might just like it."
	text(player, msg)
	msg = "It would also make me happy. Haha."
	text(player, msg)
	sleep(1)
	msg = "Anyways, I have to go now. I'll see you when I see you."
	text(player, msg)
	msg = "\nDeredere then continued his way home."
	text(player, msg)
	msg = "You thought more of what he said."
	text(player, msg)
	msg = "You find yourself wanting to jog but your laziness still won out."
	text(player, msg)
	msg = "You proceeded to go home instead."
	text(player, msg)
	sleep(3)



def schl3(room, player):
	room.choice = 0
	name = room.user[room.place[2]]

	clear(player)
	msg = "Why are you here?"
	text(player, msg)
	msg = "You got off from work and you went straight to your old school."
	text(player, msg)
	msg = "It was a weird choice but you can't help but long for the past."
	text(player, msg)
	msg = "You decided to pass through the shortcut on your way home."
	text(player, msg)
	msg = "You bumped into Deredere."
	text(player, msg)
	msg = "\n%s: Oh, sorry about that." % name
	text(player, msg)
	msg = "\n%s: It's fine." % BF
	text(player, msg)
	msg = "Where did you came from?"
	text(player, msg)
	msg = "\n%s: I passed by our old school." % name
	text(player, msg)
	msg = "I suddenly got war flashbacks. Hahaha."
	text(player, msg)

	# Time to choose
	if player is room.place[2]:
		msg = "\n1) Reminisce about the school."
		msg += "\n2) Reminisce about the shortcut."
		text(player, msg)

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

		if ans is 1:
			msg = "\n%s: I can't believe you used to have a fanclub back then." % name
			gamecast(room.names, msg)
			msg = "\n%s: Hey! I'm good-looking enough to deserve a fanclub." % BF
			gamecast(room.names, msg)
			msg = "Not only that but I'm really good at soccer. So I have the skills worth fangirling for."
			gamecast(room.names, msg)
			sleep(1)
			msg = "\n%s: Yes. The skills to handle balls. Very admirable indeed." % name
			gamecast(room.names, msg)
			msg = "\n%s: Don't reduce my skills to that!" % BF
			gamecast(room.names, msg)
			msg = "\n%s: Hahaha." % name
			gamecast(room.names, msg)
			room.score[player] += 5

		elif ans is 2:
			msg = "\n%s: Remember when we used to walk on these streets?" % name
			gamecast(room.names, msg)
			msg = "We even have a race on who can get home the fastest."
			gamecast(room.names, msg)
			msg = "\n%s: Oh yeah! I always win though." % BF
			gamecast(room.names, msg)
			msg = "\n%s: It's because you play soccer. None of us play sports." % name
			gamecast(room.names, msg)
			msg = "You already have the advantage of being fit."
			gamecast(room.names, msg)
			msg = "\n%s: Get good then. Haha." % BF
			gamecast(room.names, msg)
			msg = "\n%s: If that's your way of telling me to exercise, then screw you. Hahaha." % name
			gamecast(room.names, msg)
			sleep(1)
			room.score[player] += 7

		else:
			msg = "\n%s: We did have a war back then." % BF
			gamecast(room.names, msg)
			msg = "Intramurals is always intense. Haha."
			gamecast(room.names, msg)
			msg = "\n%s: I know someone who went overboard at playing soccer." % name
			gamecast(room.names, msg)
			msg = "I can't believe you have a fanclub back then."
			gamecast(room.names, msg)
			msg = "\n%s: I have to admit, I am amazing at soccer. Haha." % BF
			gamecast(room.names, msg)
			msg = "\n%s: Hahaha." % name
			gamecast(room.names, msg)
			room.score[player] += 3

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\n%s: Since we're talking about school," % BF
	text(player, msg)
	msg = "Want to go home together like back then?"
	text(player, msg)
	msg = "\n%s: Sure." % name
	text(player, msg)
	msg = "\nYou went home together like old times."
	text(player, msg)
	sleep(3)



def lib3(room, player):
	room.choice = 0
	name = room.user[room.place[3]]

	clear(player)
	msg = "You went inside the library."
	text(player, msg)
	msg = "You picked up a random book off the shelf and read."
	text(player, msg)
	msg = "Time passed by and before you know it, it's already late."
	text(player, msg)
	msg = "It looks like the library isn't closing anytime soon, so you stayed a little more."
	text(player, msg)
	msg = "You take a glance at the entrance and saw Deredere walk inside."
	text(player, msg)
	msg = "You decided to approach him."
	text(player, msg)
	msg = "\n%s: Oh! I didn't noticed you were here." % BF
	text(player, msg)
	msg = "\n%s: What are you doing here?" % name
	text(player, msg)
	msg = "\n%s: Well I want to borrow a book but I don't know where to start." % BF
	text(player, msg)
	msg = "Do you have something to suggest?"
	text(player, msg)

	# Time to choose
	if player is room.place[3]:
		msg = "\n1) Suggest \"The Little Prince\"."
		msg += "\n2) Suggest \"Animal Farm\""
		text(player, msg)

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

		if ans is 1:
			msg = "\n%s: I suggest the \"Little Prince\"." % name
			gamecast(room.names, msg)
			msg = "\n%s: What's that about?" % BF
			gamecast(room.names, msg)
			msg = "\n%s: It's considered as a children's book." % name
			gamecast(room.names, msg)
			msg = "But the themes are very applicable, no matter the age."
			gamecast(room.names, msg)
			msg = "You're thrown into the perspective of a child."
			gamecast(room.names, msg)
			msg = "It talks about what is important in life"
			gamecast(room.names, msg)
			msg = "And why they're important."
			gamecast(room.names, msg)
			msg = "\n%s: Sounds nice. I'll pick that up." % BF
			gamecast(room.names, msg)
			msg = "\n%s: Great! It's one of my favorites." % name
			gamecast(room.names, msg)
			room.score[player] += 7

		elif ans is 2:
			msg = "\n%s: I suggest \"Animal Farm\"." % name
			gamecast(room.names, msg)
			msg = "It's about a group of animals who rebels against their human farmer."
			gamecast(room.names, msg)
			msg = "In the hopes of creating a society that is free, equal and happy."
			gamecast(room.names, msg)
			msg = "They wrote it so that even children can appreciate it."
			gamecast(room.names, msg)
			msg = "\n%s: Sounds interesting. I'll pick that up." % BF
			gamecast(room.names, msg)
			msg = "\n%s: Great! It's one of my favorites." % name
			gamecast(room.names, msg)
			room.score[player] += 5

		else:
			msg = "\n%s: Sorry. I can't think of anything on the spot." % name
			gamecast(room.names, msg)
			room.score[player] += 3

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\n%s: Ummm... I want to go look for more books." % BF
	text(player, msg)
	msg = "Could you accompany me?"
	text(player, msg)
	msg = "\n%s: Sure. I don't mind." % name
	text(player, msg)
	msg = "\nYou help him find a book to borrow."
	text(player, msg)
	sleep(3)



def day4(room, player):
	init(room)
	player.settimeout(None)

	msg = "\n\nDay 4: Good Morning"
	text(player, msg)
	msg = "\n\nYou plan to go back to work again."
	text(player, msg)
	msg = "There isn't a point to continue doing so but it gave you a sense of normality."
	text(player, msg)
	msg = "It's still early and you have time to go somewhere."
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
	player.settimeout(TIMELIMIT)
	if room.taken[1] is True:
		park4(room, player)
	if room.taken[0] is True:
		home4(room, player)
	if room.taken[3] is True:
		lib4(room, player)
	if room.taken[2] is True:
		schl4(room, player)



def home4(room, player):
	room.choice = 0
	name = room.user[room.place[0]]

	clear(player)
	msg = "You decided to start making breakfast."
	text(player, msg)
	msg = "You thought to make it more fancy than usual since you woke up early."
	text(player, msg)
	msg = "You were preparing the ingredients when you heard a knock on the door."
	text(player, msg)
	msg = "\n%s: Hey, %s! Let me in." % (BF, name)
	text(player, msg)
	msg = "\nYou dropped the ingredients on the table and rushed to the door."
	text(player, msg)
	msg = "You let Deredere in."
	text(player, msg)
	msg = "\n%s: Why are you here?" % name
	text(player, msg)
	msg = "It's 5AM."
	text(player, msg)
	msg = "\n%s: I want to eat some breakfast." % BF
	text(player, msg)
	msg = "So I decided that I might as well barge into your house. Haha."
	text(player, msg)
	msg = "\n%s: ..." % name
	text(player, msg)
	sleep(1)
	msg = "Well as long as you help me cook then."
	text(player, msg)
	msg = "\n%s: You have a lot of ingredients laid out." % name
	text(player, msg)
	msg = "What are you making?"
	text(player, msg)

	# Time to choose
	if player is room.place[0]:
		msg = "\n1) Pancakes with macerated fruits and whipped cream."
		msg += "\n2) Bacon and egg salad with buttered toast."
		text(player, msg)

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

		if ans is 1:
			msg = "\n%s: I'm making fancy pancakes." % name
			gamecast(room.names, msg)
			msg = "\n%s: Fancy pancakes?" % BF
			gamecast(room.names, msg)
			msg = "\n%s: Yes. I'm adding macerated fruits and whipped cream on it." % name
			gamecast(room.names, msg)
			msg = "Ahhh~ Just the thought of the food is making me excited."
			gamecast(room.names, msg)
			msg = "\n%s: That's sweet." % BF
			gamecast(room.names, msg)
			msg = "I thought you were on a diet. Haha."
			gamecast(room.names, msg)
			msg = "\n%s: The world is ending so let me cheat." % name
			gamecast(room.names, msg)
			msg = "\n%s: Sure sure. If it makes you happy then I'm happy." % BF
			gamecast(room.names, msg)
			room.score[player] += 7

		elif ans is 2:
			msg = "\n%s: I'm making bacon and egg salad with buttered toast." % name
			gamecast(room.names, msg)
			msg = "I'll probably add something more, like fruits for dessert."
			gamecast(room.names, msg)
			msg = "\n%s: How fancy. Haha." % BF
			gamecast(room.names, msg)
			msg = "\n%s: Be glad I'm sharing some with you in the first place!" % name
			gamecast(room.names, msg)
			msg = "\n%s: Don't worry." % BF
			gamecast(room.names, msg)
			msg = "I'm very happy."
			gamecast(room.names, msg)
			sleep(1)
			room.score[player] += 5

		else:
			msg = "\n%s: You do have an idea, right?" % BF
			gamecast(room.names, msg)
			msg = "You didn't just took random ingredients and dump them on the table."
			gamecast(room.names, msg)
			msg = "..."
			gamecast(room.names, msg)
			sleep(1)
			msg = "Right?"
			gamecast(room.names, msg)
			msg = "\n%s: I..." % name
			gamecast(room.names, msg)
			msg = "\n%s: Oh no. Haha." % BF
			gamecast(room.names, msg)
			msg = "\n%s: Don't judge." % name
			gamecast(room.names, msg)
			msg = "I swear I had a plan."
			gamecast(room.names, msg)
			msg = "\n%s: Well then. Why don't I make breakfast." % BF
			gamecast(room.names, msg)
			msg = "And you help me instead?"
			gamecast(room.names, msg)
			msg = "\n%s: I can't believe you're ordering me in my own house." % name
			gamecast(room.names, msg)
			msg = "\n%s: Haha." % BF
			gamecast(room.names, msg)
			room.score[player] += 3

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\nYou made breakfast together."
	text(player, msg)
	sleep(3)



def park4(room, player):
	room.choice = 0
	name = room.user[room.place[1]]

	clear(player)
	msg = "You went to the park and sat on a bench."
	text(player, msg)
	msg = "It's early so the wind is still cool."
	text(player, msg)
	msg = "You regret going out without anything to keep you warm."
	text(player, msg)
	msg = "You couldn't stand the cold so you stood up."
	text(player, msg)
	msg = "\n%s: %s!" %(BF, name)
	text(player, msg)
	msg = "\n%s: Deredere." % name
	text(player, msg)
	msg = "What are you doing here?"
	text(player, msg)
	msg = "\n%s: The usual. Having my morning walk." % BF
	text(player, msg)
	msg = "It's nice to walk around when the air is cool."
	text(player, msg)
	msg = "..."
	text(player, msg)
	sleep(1)
	msg = "Are you okay? You're shivering."
	text(player, msg)

	# Time to choose
	if player is room.place[1]:
		msg = "\n1) I'm fine. Just cold."
		msg += "\n2) No. I forgot my jacket."
		text(player, msg)

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

		if ans is 1:
			msg = "\n%s: I'm just cold so I'll be fine." % name
			gamecast(room.names, msg)
			msg = "You don't have to worry about me."
			gamecast(room.names, msg)
			msg = "\n%s: You say that but you can't stop me from worrying still." % BF
			gamecast(room.names, msg)
			msg = "\n%s: Deredere..." % name
			gamecast(room.names, msg)
			sleep(1)
			room.score[player] += 5

		elif ans is 2:
			msg = "\n%s: Nope. I'm freezing. Hahaha." % name
			gamecast(room.names, msg)
			msg = "I forgot to bring my jacket."
			gamecast(room.names, msg)
			msg = "I didn't expect it'll be this chilly."
			gamecast(room.names, msg)
			room.score[player] += 7

		else:
			msg = "\n%s: ..." % BF
			gamecast(room.names, msg)
			msg = "Okay, it's getting obvious that you're not okay."
			gamecast(room.names, msg)
			msg = "You know you can tell me if you're not feeling well."
			gamecast(room.names, msg)
			msg = "I'm always willing to help."
			gamecast(room.names, msg)
			msg = "So just say tell me, okay?"
			gamecast(room.names, msg)
			msg = "\n%s: Thanks, Deredere." % name
			gamecast(room.names, msg)
			msg = "That means a lot to me."
			gamecast(room.names, msg)
			sleep(1)
			room.score[player] += 3

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\n%s: Here. I'll lend you my jacket." % BF
	text(player, msg)
	msg = "\n%s: But you'll be cold." % name
	text(player, msg)
	msg = "\n%s: I'll be fine. You need it more than I do." % BF
	text(player, msg)
	msg = "\n%s: Don't you have a morning walk to finish?" % name
	text(player, msg)
	msg = "You'll be out longer than I am since I'm about to go home."
	text(player, msg)
	msg = "So you don't have to lend it to me."
	text(player, msg)
	msg = "\n%s: I said I'll be fine." % BF
	text(player, msg)
	msg = "Let me do this for you."
	text(player, msg)
	msg = "I insist."
	text(player, msg)
	msg = "\n%s: ..." % name
	text(player, msg)
	sleep(1)
	msg = "Okay."
	text(player, msg)
	msg = "\n%s: That's my %s!" % (BF, name)
	text(player, msg)
	msg = "Anyways, I'll continue on."
	text(player, msg)
	msg = "I'll go get my jacket from you later tonight."
	text(player, msg)
	msg = "\n%s: Sure. I'll see you later." % name
	text(player, msg)
	msg = "\n%s: See you!" % BF
	text(player, msg)
	msg = "\nDeredere left."
	text(player, msg)
	msg = "\nYou pause for a moment and let reality sink in."
	text(player, msg)
	msg = "You look at the jacket you're now wearing."
	text(player, msg)
	msg = "It's warm and cozy. Just like Deredere."
	text(player, msg)
	msg = "It's like he never left."
	text(player, msg)
	msg = "\nYou linger in his warmth as you go home."
	text(player, msg)
	sleep(3)



def schl4(room, player):
	room.choice = 0
	name = room.user[room.place[2]]

	clear(player)
	msg = "You went to the cafe in front of your old school."
	text(player, msg)
	msg = "You remember going here with your friends after school."
	text(player, msg)
	msg = "It's either you splurge on sweets or you race home."
	text(player, msg)
	msg = "It brings you good memories."
	text(player, msg)
	msg = "You messaged Deredere that you're at the cafe already."
	text(player, msg)
	msg = "You wait for his reply."
	text(player, msg)
	sleep(1)
	msg = "\nSomeone covered your eyes."
	text(player, msg)
	msg = "\n%s: Guess who. Haha." % BF
	text(player, msg)
	msg = "\n%s: It's obviously you Deredere." % name
	text(player, msg)
	msg = "\n%s: Come on! Can't you indulge me a little?" % BF
	text(player, msg)
	msg = "\n%s: Just take your hands off my face, you weirdo." % name
	text(player, msg)
	msg = "\n%s: After asking me out, you're now being mean." % BF
	text(player, msg)
	msg = "This is why you're single."
	text(player, msg)

	# Time to choose
	if player is room.place[2]:
		msg = "\n1) You're also single."
		msg += "\n2) I'm just waiting for you."
		text(player, msg)

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

		if ans is 1:
			msg = "\n%s: It takes one to know one." % name
			gamecast(room.names, msg)
			msg = "\n%s: Hey!" % BF
			gamecast(room.names, msg)
			room.score[player] += 3

		elif ans is 2:
			msg = "\n%s: I'm just waiting for someone, you know." % name
			gamecast(room.names, msg)
			msg = "\n%s: Oh? Who?" % BF
			gamecast(room.names, msg)
			msg = "\n%s: You." % name
			gamecast(room.names, msg)
			sleep(1)
			msg = "\n%s: Is this really the game we're playing?" % BF
			gamecast(room.names, msg)
			msg = "Who can drop pickup lines the longest?"
			gamecast(room.names, msg)
			room.score[player] += 7

		else:
			msg = "\n%s: Hey, I didn't offend you did I?" % BF
			gamecast(room.names, msg)
			msg = "I'm sorry."
			gamecast(room.names, msg)
			msg = "There's nothing wrong with being single."
			gamecast(room.names, msg)
			msg = "\n%s: Don't worry. I'm just surprised." % name
			gamecast(room.names, msg)
			msg = "A single person is teasing another single person."
			gamecast(room.names, msg)
			msg = "As far as I know, you can't even ask someone out."
			gamecast(room.names, msg)
			msg = "\n%s: Hey! Why you got to do me so dirty." % BF
			gamecast(room.names, msg)
			room.score[player] += 5

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\n%s: You think you can beat me? Hahaha." % name
	text(player, msg)
	msg = "I like to see you try."
	text(player, msg)
	msg = "\n%s: Haha." % BF
	text(player, msg)
	msg = "\nYou bickered in the cafe like children."
	text(player, msg)
	sleep(3)



def lib4(room, player):
	room.choice = 0
	name = room.user[room.place[3]]

	clear(player)
	msg = "You looked at the close sign of the library door."
	text(player, msg)
	msg = "Maybe before going to a place, you should have checked the schedule."
	text(player, msg)
	msg = "But you didn't expect that the library will be closed still."
	text(player, msg)
	msg = "Since it's closed, you're now lost on what to do."
	text(player, msg)
	msg = "You looked at the sky."
	text(player, msg)
	msg = "A waving hand entered your vision."
	text(player, msg)
	msg = "\n%s: What are you looking at?" % BF
	text(player, msg)
	msg = "\n%s: The sky?" % name
	text(player, msg)
	msg = "Why are you here anyway? The library is closed."
	text(player, msg)
	msg = "\n%s: I was just passing by when I saw you." % BF
	text(player, msg)
	msg = "Can't I even say hi to my dearest friend?"
	text(player, msg)
	msg = "\n%s: Sush." % name
	text(player, msg)
	sleep(1)
	msg = "\n%s: You know, I was skimming books here when I read a nice quote."
	text(player, msg)
	msg = "\"Next to trying and winning, the best thing is trying and failing.\""
	text(player, msg)
	msg = "It's by Lucy Maud Montgomery. The book is \"Anne of the Green Gables\"."
	text(player, msg)

	# Time to choose
	if player is room.place[3]:
		msg = "\n1) That's very like you."
		msg += "\n2) Are you telling me something?"
		text(player, msg)

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

		if ans is 1:
			msg = "\n%s: That quote fits you a lot." % name
			gamecast(room.names, msg)
			msg = "\n%s: Really? Haha." % BF
			gamecast(room.names, msg)
			msg = "I didn't think of that."
			gamecast(room.names, msg)
			msg = "Thanks. That means a lot."
			gamecast(room.names, msg)
			msg = "\n%s: You're welcome." % name
			gamecast(room.names, msg)
			room.score[player] += 7

		elif ans is 2:
			msg = "\n%s: Are you telling me..." % name
			gamecast(room.names, msg)
			msg = "To raid the library?"
			gamecast(room.names, msg)
			msg = "\n%s: What?" % BF
			gamecast(room.names, msg)
			msg = "I..."
			gamecast(room.names, msg)
			sleep(1)
			msg = "No! What the heck?!?"
			gamecast(room.names, msg)
			msg = "\n%s: Hahaha. I'm just messing with you." % name
			gamecast(room.names, msg)
			msg = "\n%s: You always find a way to tease me, don't you?" % BF
			gamecast(room.names, msg)
			msg = "\n%s: That's why we're good friends. Hahaha." % name
			gamecast(room.names, msg)
			room.score[player] += 5

		else:
			msg = "\n%s: Oh. I see." % name
			gamecast(room.names, msg)
			room.score[player] += 3

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\n%s: Oh! The library is being opened." % BF
	text(player, msg)
	msg = "I guess I'll go now."
	text(player, msg)
	msg = "\n%s: Thanks for accompanying me." % name
	text(player, msg)
	msg = "\n%s: Anything for you. Haha." % BF
	text(player, msg)
	msg = "\nYou entered the library and check out that book."
	text(player, msg)
	sleep(3)



def day5(room, player):
	init(room)
	player.settimeout(None)

	msg = "\n\nDay 5: Last Wishes"
	text(player, msg)
	msg = "\n\nThe asteroid that is about to hit Earth is now observable."
	text(player, msg)
	msg = "It's still a speck in the sky."
	text(player, msg)
	msg = "But to think something so small now will bring the end of everything."
	text(player, msg)
	msg = "You don't want to dwell on it."
	text(player, msg)
	sleep(1)
	msg = "Three days left until the Armageddon."
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
	player.settimeout(TIMELIMIT)
	if room.taken[1] is True:
		park5(room, player)
	if room.taken[2] is True:
		schl5(room, player)
	if room.taken[3] is True:
		lib5(room, player)
	if room.taken[0] is True:
		home5(room, player)



def home5(room, player):
	room.choice = 0
	name = room.user[room.place[0]]

	clear(player)
	msg = "You put the popcorn in the microwave and set the timer on."
	text(player, msg)
	msg = "You want the last few memories to be watching movies together with Deredere."
	text(player, msg)
	sleep(1)
	msg = "Deredere is helping you set up your living room."
	text(player, msg)
	msg = "\n%s: Hey, %s! What movie are we watching?" % (BF, name)
	text(player, msg)

	# Time to choose
	if player is room.place[0]:
		msg = "\n1) Your favorite."
		msg += "\n2) Choose whatever."
		text(player, msg)

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

		if ans is 1:
			msg = "\n%s: Get your favorite movie." % name
			gamecast(room.names, msg)
			msg = "I'm willing to indulge you."
			gamecast(room.names, msg)
			msg = "\n%s: Really!?!" % BF
			gamecast(room.names, msg)
			msg = "You're the best, %s!" % name
			gamecast(room.names, msg)
			msg = "I'll go put it in."
			gamecast(room.names, msg)
			room.score[player] += 7

		elif ans is 2:
			msg = "\n%s: Go choose whatever you like." % name
			gamecast(room.names, msg)
			msg = "As long as it's not the usual."
			gamecast(room.names, msg)
			msg = "\n%s: Oh man. I was hoping to pick my favorite!" % BF
			gamecast(room.names, msg)
			msg = "\n%s: That's nice and all but no." % name
			gamecast(room.names, msg)
			msg = "We watched that way too much that I lost count."
			gamecast(room.names, msg)
			msg = "\n%s: It's a good movie though." % BF
			gamecast(room.names, msg)
			msg = "\n%s: Don't push it. Hahaha." % name
			gamecast(room.names, msg)
			msg = "\n%s: Well at least I get to pick. Haha." % BF
			gamecast(room.names, msg)
			room.score[player] += 5

		else:
			msg = "\n%s: I'm going to pick if you're not suggesting anything." % BF
			gamecast(room.names, msg)
			msg = "\n%s: Okay." % name
			gamecast(room.names, msg)
			room.score[player] += 3

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\nYou watched Deredere set up the movie."
	text(player, msg)
	msg = "He's smiling really big."
	text(player, msg)
	msg = "His smile is nice. You like it a lot."
	text(player, msg)
	msg = "It gives you a fluttering feeling."
	text(player, msg)
	sleep(1)
	msg = "\nYou put the popcorn in a bowl and brought it to the living room."
	text(player, msg)
	msg = "You and Deredere chatter while watching the movie."
	text(player, msg)
	sleep(1)
	msg = "\nTime passes by quickly."
	text(player, msg)
	msg = "It's getting very late and you're on your 3rd movie."
	text(player, msg)
	msg = "You feel so comfortable next to Deredere."
	text(player, msg)
	msg = "You find your eyelids closing."
	text(player, msg)
	msg = "You fell asleep on his shoulder with the movie as your lullaby."
	text(player, msg)
	sleep(3)



def park5(room, player):
	room.choice = 0
	name = room.user[room.place[1]]

	clear(player)
	msg = "You don't know how you found yourself in this situation."
	text(player, msg)
	msg = "But hiding from Deredere in the park playing hide-and-seek is..."
	text(player, msg)
	msg = "\n%s: Found you!" % BF
	text(player, msg)
	msg = "\n%s: AAAAAAAAAAAAAHHHHHHHHHHHHHHH!" % name
	text(player, msg)
	msg = "\n%s: HAHA. Did you see your face?" % BF
	text(player, msg)
	msg = "That was priceless!"
	text(player, msg)
	msg = "\n%s: You almost gave me a heart attack!" % name
	text(player, msg)
	msg = "Do you really need to sneak up on me?"
	text(player, msg)
	msg = "\n%s: Of course. That's the point of hide-and-seek. Haha." % BF
	text(player, msg)
	msg = "So what are we going to do next?"
	text(player, msg)
	msg = "\n%s: I'm done hiding. Let's have a chase." % name
	text(player, msg)
	msg = "I bet I can catch you."
	text(player, msg)
	msg = "\n%s: Ohhh. Confident. I like that." % BF
	text(player, msg)
	msg = "What will you bet?"
	text(player, msg)

	# Time to choose
	if player is room.place[1]:
		msg = "\n1) My heart."
		msg += "\n2) Money."
		text(player, msg)

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

		if ans is 1:
			msg = "\n%s: My heart." % name
			gamecast(room.names, msg)
			msg = "\n%s: Ewww. No thanks." % BF
			gamecast(room.names, msg)
			msg = "\n%s: How dare you!" % name
			gamecast(room.names, msg)
			msg = "Get back here and let me hit you."
			gamecast(room.names, msg)
			msg = "\n%s: Haha." % BF
			gamecast(room.names, msg)
			room.score[player] += 5

		elif ans is 2:
			msg = "\n%s: I'll give my money." % name
			gamecast(room.names, msg)
			msg = "\n%s: The world's ending though." % BF
			gamecast(room.names, msg)
			msg = "\n%s: Tsk tsk tsk." % name
			gamecast(room.names, msg)
			msg = "Obviously not just any money."
			gamecast(room.names, msg)
			msg = "I'm talking about my collection."
			gamecast(room.names, msg)
			msg = "\n%s: No way. You're betting the limited edition coins?" % BF
			gamecast(room.names, msg)
			msg = "\n%s: Well? Will you accept?" % name
			gamecast(room.names, msg)
			msg = "\n%s: Well if I were you, I'll run now." % BF
			gamecast(room.names, msg)
			msg = "I'll make sure you regret betting that."
			gamecast(room.names, msg)
			room.score[player] += 3

		else:
			msg = "\n%s: You're letting me pick then?" % BF
			gamecast(room.names, msg)
			msg = "\n%s: Sure. Go ahead." % name
			gamecast(room.names, msg)
			msg = "\n%s: Well you better run cause you won't like it. Haha." % BF
			gamecast(room.names, msg)
			msg = "\n%s: ..." % name
			gamecast(room.names, msg)
			msg = "\nYou bolted."
			gamecast(room.names, msg)
			room.score[player] += 7

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\nYou chase around the park like children."
	text(player, msg)
	sleep(3)



def schl5(room, player):
	room.choice = 0
	name = room.user[room.place[2]]

	clear(player)
	msg = "Ever since the announcement of the world ending, the old school has been open to the public."
	text(player, msg)
	sleep(1)
	msg = "You invited Deredere to eat lunch with you at the rooftop."
	text(player, msg)
	msg = "You told him that you'll pack your lunches so he doesn't have to bring anything."
	text(player, msg)
	msg = "The breeze on the rooftop is nice."
	text(player, msg)
	msg = "\n%s: Did you wait long?" % BF
	text(player, msg)
	msg = "\n%s: No." % name
	text(player, msg)
	msg = "Nice to see you. Hahaha."
	text(player, msg)
	msg = "\n%s: I know you told me not to bring any but I still brought some fruits for dessert." % BF
	text(player, msg)
	msg = "\n%s: Wow! That's nice." % name
	text(player, msg)
	msg = "\n%s: So what's for lunch?" % BF
	text(player, msg)

	# Time to choose
	if player is room.place[2]:
		msg = "\n1) Carbonara and garlic bread."
		msg += "\n2) Buttered chicken and baby potatoes."
		text(player, msg)

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

		if ans is 1:
			msg = "\n%s: It's pasta and garlic bread." % name
			gamecast(room.names, msg)
			msg = "Carbonara to be exact. Hahaha."
			gamecast(room.names, msg)
			msg = "\n%s: One of your favorites then. Haha." % BF
			gamecast(room.names, msg)
			msg = "\n%s: Yeah. I hope you'll like it." % name
			gamecast(room.names, msg)
			msg = "\n%s: Even if it tastes bad, I'll still like it." % BF
			gamecast(room.names, msg)
			msg = "Because you made it for me. Haha."
			gamecast(room.names, msg)
			msg = "\n%s: Stop with the flirting and let's eat." % name
			gamecast(room.names, msg)
			msg = "\n%s: Haha. Okay." % BF
			gamecast(room.names, msg)
			room.score[player] += 5

		elif ans is 2:
			msg = "\n%s: It's buttered chicken and baby potatoes." % name
			gamecast(room.names, msg)
			msg = "Just like the lunches at the school cafeteria. Hahaha."
			gamecast(room.names, msg)
			msg = "\n%s: But I bet it tastes better than the food served then." % BF
			gamecast(room.names, msg)
			msg = "Since you made it. Haha."
			gamecast(room.names, msg)
			msg = "\n%s: Sush. You and your pickup lines." % name
			gamecast(room.names, msg)
			msg = "Come on. Let's eat. I'm hungry."
			gamecast(room.names, msg)
			msg = "\n%s: Sure sure. Thanks for the food." % BF
			gamecast(room.names, msg)
			room.score[player] += 7

		else:
			msg = "\n%s: What? Is it a secret?" % BF
			gamecast(room.names, msg)
			msg = "Is this a mystery box?"
			gamecast(room.names, msg)
			msg = "Is it poison? Are you killing when the world's ending?"
			gamecast(room.names, msg)
			msg = "\n%s: Shut up." % name
			gamecast(room.names, msg)
			msg = "You'll find out anyway so why ask?"
			gamecast(room.names, msg)
			msg = "\n%s: For presentation. Haha." % BF
			gamecast(room.names, msg)
			msg = "Makes it more interesting."
			gamecast(room.names, msg)
			msg = "Also, it's your time to flex."
			gamecast(room.names, msg)
			msg = "\n%s: Ewww. Just eat your food." % name
			gamecast(room.names, msg)
			msg = "\n%s: Okay okay. Haha." % BF
			gamecast(room.names, msg)
			room.score[player] += 3

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\nYou enjoyed the sunny weather as you eat."
	text(player, msg)
	sleep(3)



def lib5(room, player):
	room.choice = 0
	name = room.user[room.place[3]]

	clear(player)
	msg = "You went to the library with Deredere."
	text(player, msg)
	msg = "He promised he'll read with you."
	text(player, msg)
	msg = "Looking at him, he obviously broke his promise."
	text(player, msg)
	msg = "If he wanted to sleep, he could have stayed at home."
	text(player, msg)
	msg = "He doesn't have to accompany you."
	text(player, msg)
	msg = "You look at him and decided what to do."
	text(player, msg)

	# Time to choose
	if player is room.place[3]:
		msg = "\n1) Wake him up gently."
		msg += "\n2) Smack him."
		text(player, msg)

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

		if ans is 1:
			msg = "\n%s: Hey, Deredere. Wake up." % name
			gamecast(room.names, msg)
			msg = "\nYou shook his shoulders gently."
			gamecast(room.names, msg)
			msg = "\n%s: Five more minutes please." % BF
			gamecast(room.names, msg)
			msg = "\n%s: Seriously, don't sleep in the library." % name
			gamecast(room.names, msg)
			msg = "You promised you'll read with me."
			gamecast(room.names, msg)
			msg = "\n%s: Fine. I'll wake up just for you." % BF
			gamecast(room.names, msg)
			msg = "See. I'm awake now."
			gamecast(room.names, msg)
			msg = "\n%s: Sitting up with your eyes still closed does not count." % name
			gamecast(room.names, msg)
			msg = "Fine. I'll let you sleep."
			gamecast(room.names, msg)
			msg = "\n%s: Nice. Thanks. You're the best." % BF
			gamecast(room.names, msg)
			msg = "\nDeredere went back to sleep."
			gamecast(room.names, msg)
			room.score[player] += 5

		elif ans is 2:
			msg = "\n%s: You're so not sleeping in the library." % name
			gamecast(room.names, msg)
			msg = "\nYou smacked Deredere awake."
			gamecast(room.names, msg)
			msg = "\n%s: What? What? What?" % BF
			gamecast(room.names, msg)
			msg = "Did something happened?"
			gamecast(room.names, msg)
			msg = "Did I hit my head? Why does my head hurts?"
			gamecast(room.names, msg)
			msg = "\n%s: Can't you sleep somewhere else?" % name
			gamecast(room.names, msg)
			msg = "You promised you'll read with me but you're sleeping."
			gamecast(room.names, msg)
			msg = "\n%s: I'm sorry." % BF
			gamecast(room.names, msg)
			msg = "I just felt so relaxed and I can't help but fall asleep."
			gamecast(room.names, msg)
			msg = "Here, I'll read with you."
			gamecast(room.names, msg)
			msg = "\nDeredere picked up a random book nearby and attempted to read."
			gamecast(room.names, msg)
			msg = "You can see him going back to sleep."
			gamecast(room.names, msg)
			msg = "You shook your head and let him be."
			gamecast(room.names, msg)
			room.score[player] += 3

		else:
			msg = "You left him be."
			gamecast(room.names, msg)
			msg = "You admire his sleeping face."
			gamecast(room.names, msg)
			msg = "You find yourself at awe of his looks."
			gamecast(room.names, msg)
			msg = "He looks relaxed."
			gamecast(room.names, msg)
			msg = "You wish you could see more of this side of him."
			gamecast(room.names, msg)
			room.score[player] += 7

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\nYou went back to reading."
	text(player, msg)
	sleep(3)



def day6(room, player):
	init(room)
	player.settimeout(None)

	msg = "\n\nDay 6: Our Confession"
	text(player, msg)
	msg = "\n\nTomorrow is the last day."
	text(player, msg)
	msg = "The asteroid that was a speck yesterday is now bigger."
	text(player, msg)
	msg = "You decided to confess today."
	text(player, msg)
	msg = "You have to pick the perfect place to do so."
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
				msg = "You chose to confess by home."
			elif ans is 1:
				msg = "You chose to confess in the park."
			elif ans is 2:
				msg = "You chose to confess by your old school."
			else:
				msg = "You chose to confess in the library."
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
	player.settimeout(TIMELIMIT)
	if room.taken[0] is True:
		home6(room, player)
	if room.taken[1] is True:
		park6(room, player)
	if room.taken[2] is True:
		schl6(room, player)
	if room.taken[3] is True:
		lib6(room, player)



def home6(room, player):
	room.choice = 0
	name = room.user[room.place[0]]

	clear(player)
	msg = "You're on your way to Deredere's house."
	text(player, msg)
	msg = "You decided to write down your feelings in a letter."
	text(player, msg)
	msg = "It was embarrassing and old-fashioned."
	text(player, msg)
	msg = "But you can't handle the thought of actually saying those words."
	text(player, msg)
	msg = "You reached his house and opened his mailbox."
	text(player, msg)
	msg = "You discreetly put the letter inside."
	text(player, msg)
	msg = "\n%s: %s? What are you doing?" % (BF, name)
	text(player, msg)
	msg = "\n%s: Deredere!" % name
	text(player, msg)

	# Time to choose
	if player is room.place[0]:
		msg = "\n1) I'm just leaving a note."
		msg += "\n2) Nothing."
		text(player, msg)

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

		if ans is 1:
			msg = "\n%s: Ohhh. Ummm..." % name
			gamecast(room.names, msg)
			msg = "I'm just leaving a note. Hahaha."
			gamecast(room.names, msg)
			msg = "I thought you were outside."
			gamecast(room.names, msg)
			msg = "\n%s: You could just called me if you want to leave a message." % BF
			gamecast(room.names, msg)
			sleep(1)
			msg = "You don't have to go through the trouble of putting it in my mailbox."
			gamecast(room.names, msg)
			sleep(1)
			msg = "\nDeredere approaches you."
			gamecast(room.names, msg)
			msg = "\n%s: Ummm! Well, you see, I was just passing by." % name
			gamecast(room.names, msg)
			msg = "So I thought that I'll just leave you a note."
			gamecast(room.names, msg)
			msg = "Since I have some urgent things to do."
			gamecast(room.names, msg)
			msg = "Anyways, goodbye!"
			gamecast(room.names, msg)
			room.score[player] += 5

		elif ans is 2:
			msg = "\n%s: I'm not doing anything..." % name
			gamecast(room.names, msg)
			msg = "\n%s: You're not doing anything?" % BF
			gamecast(room.names, msg)
			msg = "Then why are you at my mailbox then?"
			gamecast(room.names, msg)
			msg = "\n%s: Uhhh..." % name
			gamecast(room.names, msg)
			msg = "I'm expecting a package!"
			gamecast(room.names, msg)
			msg = "I haven't receive it yet so I thought I accidentally wrote down you guys' addresses."
			gamecast(room.names, msg)
			sleep(1)
			msg = "So I was just checking. Hahaha."
			gamecast(room.names, msg)
			msg = "\n%s: You do know you could just call me, right?" % BF
			gamecast(room.names, msg)
			msg = "I can bring your package for you if ever."
			gamecast(room.names, msg)
			msg = "\n%s: No no. It's fine. Hahaha." % name
			gamecast(room.names, msg)
			msg = "Why go through the extra trouble. Hahaha."
			gamecast(room.names, msg)
			msg = "\n%s: Are you okay?" % BF
			gamecast(room.names, msg)
			msg = "\nDeredere approaches you."
			gamecast(room.names, msg)
			msg = "\n%s: Hahaha. I'm fine." % name
			gamecast(room.names, msg)
			msg = "I remember I got some things to do."
			gamecast(room.names, msg)
			msg = "I'll see you when I see you!"
			gamecast(room.names, msg)
			room.score[player] += 3

		else:
			msg = "\n%s: %s?" % (BF, name)
			gamecast(room.names, msg)
			msg = "\nYou turned to Deredere."
			gamecast(room.names, msg)
			msg = "Your face is red and you avoid his eyes."
			gamecast(room.names, msg)
			msg = "Deredere is shocked at the expression you made."
			gamecast(room.names, msg)
			msg = "\n%s: %s-" % (BF, name)
			gamecast(room.names, msg)
			room.score[player] += 7

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\nYou ran away quickly."
	text(player, msg)
	msg = "You hope that Deredere will read your letter."
	text(player, msg)
	msg = "But for now, you need to be as far away as possible."
	text(player, msg)
	msg = "That was so embarrassing!"
	text(player, msg)
	sleep(3)



def park6(room, player):
	room.choice = 0
	name = room.user[room.place[1]]

	clear(player)
	msg = "Maybe confessing through food isn't a good idea."
	text(player, msg)
	msg = "You can't help but be embarrassed."
	text(player, msg)
	msg = "You have no other choice though."
	text(player, msg)
	msg = "It's either this or keep your feelings 'til you die."
	text(player, msg)
	msg = "..."
	text(player, msg)
	sleep(1)
	msg = "Yes. Confessing through food is a good idea."
	text(player, msg)
	msg = "\n%s: %s!" % (BF, name)
	text(player, msg)
	msg = "\n%s: Oh! Yes, Deredere?" % name
	text(player, msg)
	msg = "\n%s: You're spacing out. Are you okay?" % BF
	text(player, msg)
	msg = "\n%s: Oh yeah. I'm fine."
	text(player, msg)
	msg = "Just thinking. That's all."
	text(player, msg)
	msg = "\n%s: If you say so."
	text(player, msg)
	msg = "\nYou returned to eating your food."
	text(player, msg)
	msg = "Deredere finally picked up the container with your confession in it."
	text(player, msg)
	msg = "Your doubts for using food to confess increases."
	text(player, msg)
	msg = "\n%s: %s? What is this?" % (BF, name)
	text(player, msg)
	msg = "Are you telling me something?"
	text(player, msg)

	# Time to choose
	if player is room.place[1]:
		msg = "\n1) It means what it means."
		msg += "\n2) I like you."
		text(player, msg)

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

		if ans is 1:
			msg = "\n%s: I don't have to explain, do I?" % name
			gamecast(room.names, msg)
			msg = "It means what it means."
			gamecast(room.names, msg)
			msg = "\n%s: %s, I-" % (BF, name)
			gamecast(room.names, msg)
			room.score[player] += 3

		elif ans is 2:
			msg = "\n%s: You're really making me say it..." % name
			gamecast(room.names, msg)
			msg = "I like you."
			gamecast(room.names, msg)
			sleep(1)
			msg = "I have liked you for a long time."
			gamecast(room.names, msg)
			msg = "\n%s: ..." % BF
			gamecast(room.names, msg)
			sleep(1)
			msg = "%s-" % name
			gamecast(room.names, msg)
			room.score[player] += 7

		else:
			msg = "\n%s: %s..." % (BF, name)
			gamecast(room.names, msg)
			room.score[player] += 5

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\n%s: I don't want to hear your answer now." % name
	text(player, msg)
	msg = "If it's okay, can you tell me tomorrow?"
	text(player, msg)
	msg = "\n%s: Okay..." % BF
	text(player, msg)
	msg = "\nYou've successfully confessed through food."
	text(player, msg)
	msg = "At the expense of highly embarrassing yourself."
	text(player, msg)
	sleep(3)



def schl6(room, player):
	room.choice = 0
	name = room.user[room.place[2]]

	clear(player)
	msg = "This has to be the most cringey confession you've ever planned."
	text(player, msg)
	msg = "IN YOUR ENTIRE LIFE."
	text(player, msg)
	msg = "From all of the ways you decide to confess."
	text(player, msg)
	msg = "It just have to be the confession behind the school."
	text(player, msg)
	msg = "Can you get anymore cliché?"
	text(player, msg)
	msg = "You're not even a student anymore."
	text(player, msg)
	msg = "AAAAAAAAAAAAAHHHHHHHHHHHHHHH"
	text(player, msg)
	sleep(1)
	msg = "\nYou're waiting for Deredere to come."
	text(player, msg)
	msg = "You're extremely nervous."
	text(player, msg)
	msg = "\n%s: %s?" % (BF, name)
	text(player, msg)
	msg = "\n%s: Deredere!" % name
	text(player, msg)
	msg = "\n%s: There you are. So why did we meet up here?" % BF
	text(player, msg)

	# Time to choose
	if player is room.place[2]:
		msg = "\n1) Please go out with me."
		msg += "\n2) I want to be with you."
		text(player, msg)

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

		if ans is 1:
			msg = "\n%s: I like you. Please go out with me." % name
			gamecast(room.names, msg)
			msg = "\n%s: %s?!?" % (BF, name)
			gamecast(room.names, msg)
			msg = "\n%s: You're like a child and you look like one." % name
			gamecast(room.names, msg)
			msg = "You're short but you're good at sports."
			gamecast(room.names, msg)
			msg = "You're nice but sometimes you're too nice."
			gamecast(room.names, msg)
			msg = "You attract a lot of people and I hate that I'm getting jealous everytime."
			gamecast(room.names, msg)
			msg = "Even though I'm one of the closest to you."
			gamecast(room.names, msg)
			msg = "But despite all these."
			gamecast(room.names, msg)
			msg = "All these things."
			gamecast(room.names, msg)
			sleep(1)
			msg = "I like all those parts of you."
			gamecast(room.names, msg)
			sleep(1)
			msg = "\n%s: %s..." % (BF, name)
			gamecast(room.names, msg)
			room.score[player] += 5

		elif ans is 2:
			msg = "\n%s: I want to be you." % name
			gamecast(room.names, msg)
			msg = "Whether the world is ending or not,"
			gamecast(room.names, msg)
			msg = "I want to be by your side."
			gamecast(room.names, msg)
			msg = "In the last few moments of our life,"
			gamecast(room.names, msg)
			msg = "Can I spend it with you?"
			gamecast(room.names, msg)
			msg = "\n%s: %s..." % (BF, name)
			gamecast(room.names, msg)
			room.score[player] += 7

		else:
			msg = "\n%s: %s?" % (BF, name)
			gamecast(room.names, msg)
			msg = "\n%s: ..." % name
			gamecast(room.names, msg)
			sleep(1)
			msg = "I'm having a hard time telling this to you."
			gamecast(room.names, msg)
			msg = "But I just want you to know..."
			gamecast(room.names, msg)
			msg = "Deredere, I like you."
			gamecast(room.names, msg)
			msg = "\n%s: ..." % BF
			gamecast(room.names, msg)
			room.score[player] += 3

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\n%s: I want to know your answer tomorrow." % name
	text(player, msg)
	msg = "Please?"
	text(player, msg)
	msg = "\n%s: Okay. I'll think about it." % BF
	text(player, msg)
	msg = "\n%s: Okay. Thank you." % name
	text(player, msg)
	msg = "\nYou've embarrassingly confessed like a school girl."
	text(player, msg)
	sleep(3)



def lib6(room, player):
	room.choice = 0
	name = room.user[room.place[3]]

	clear(player)
	msg = "You're in the innermost part of the library with Deredere."
	text(player, msg)
	msg = "You wanted to confess somewhere quiet."
	text(player, msg)
	msg = "The library seemed like a good idea."
	text(player, msg)
	msg = "It's now or never."
	text(player, msg)
	msg = "\n%s: Ummm... %s?" % (BF, name)
	text(player, msg)

	# Time to choose
	if player is room.place[3]:
		msg = "\n1) Confess outright."
		msg += "\n2) Suggest to hang out."
		text(player, msg)

		try:
			ans = int(player.recv(BUFSIZ).decode("utf8"))
		except socket.timeout:
			ans = 0

		if ans is 1:
			msg = "\n%s: I like you, Deredere." % name
			gamecast(room.names, msg)
			msg = "I have always liked you."
			gamecast(room.names, msg)
			msg = "Even if we clash and have different interests,"
			gamecast(room.names, msg)
			msg = "I didn't'mind them at all because it's you."
			gamecast(room.names, msg)
			msg = "..."
			gamecast(room.names, msg)
			sleep(1)
			msg = "I brought you here because I want you to hear me clearly."
			gamecast(room.names, msg)
			msg = "I want that these books will serve as my witnesses of my feelings for you."
			gamecast(room.names, msg)
			msg = "I'm happy that I met you."
			gamecast(room.names, msg)
			msg = "I'm happy that we became close friends."
			gamecast(room.names, msg)
			msg = "I'll be happier if we become something more."
			gamecast(room.names, msg)
			msg = "\n%s: ..." % BF
			gamecast(room.names, msg)
			room.score[player] += 7

		elif ans is 2:
			msg = "\n%s: These last few days had been fun." % name
			gamecast(room.names, msg)
			msg = "I wish I could spend more days with you."
			gamecast(room.names, msg)
			msg = "..."
			gamecast(room.names, msg)
			sleep(1)
			msg = "If I can, if you let me..."
			gamecast(room.names, msg)
			msg = "I want to hang out with you in our last day."
			gamecast(room.names, msg)
			msg = "\n%s: %s..." % (BF, name)
			gamecast(room.names, msg)
			room.score[player] += 5

		else:
			msg = "\nYou confessed under your breath."
			gamecast(room.names, msg)
			msg = "\n%s: I'm sorry. I didn't hear you." % BF
			gamecast(room.names, msg)
			msg = "\n%s: I said that I like you." % name
			gamecast(room.names, msg)
			msg = "\n%s: ..." % BF
			gamecast(room.names, msg)
			room.score[player] += 3

		room.choice = 1


	while room.choice == 0:
		i = 0				# Do nothing


	msg = "\n%s: You can tell me your answer tomorrow." % name
	text(player, msg)
	msg = "Okay?"
	text(player, msg)
	msg = "\n%s: Okay. I will." % BF
	text(player, msg)
	msg = "\nIt's quiet but your confession reached him loud and clear."
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
	room.place = []
	room.taken = []
	room.choice = 0

	for i in range(4):
		room.place.append("")
		room.taken.append(False)



# ===================================
# Code and info gotten from these websites:
# https://stackoverflow.com/questions/7002429/how-can-i-extract-all-values-from-a-dictionary-in-python
# https://kite.com/python/docs/socket.socket.settimeout
# ===================================
