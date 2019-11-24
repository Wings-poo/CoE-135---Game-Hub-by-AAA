# python3 code
# CoE 135 - My Last Days with You - Dating Sim
# ===================================

from time import sleep

BUFSIZ = 1024


# ==== Main ====
def play(room, player):
	clear(player)
	sleep(0.5)
	player.send((bytes("My Last Days with You - Dating Sim", "utf8")))
	sleep(1)
	day1(room, player)
	# day2(room, player)
	# day3(room, player)
	# day4(room, player)
	# day5(room, player)
	# day6(room, player)
	# day7(room, player)
	player.send((bytes("=========== Game End ===========", "utf8")))
	sleep(0.5)



def day1(room, player):
	room.datingsim(True)

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

		if (ans < 4 and ans >= 0)and room.taken[ans] == False:
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

		elif (ans < 4 and ans >= 0)and room.taken[ans] == True:
			msg = "Place is taken."
			player.send(bytes(msg, "utf8"))

		else:
			msg = "%d is invalid." %ans
			player.send(bytes(msg, "utf8"))


	# Wait until everyone has made a choice
	while room.choice < room.num:
		i = 0				# Do nothing

	sleep(0.5)
	clear(player)
	sleep(0.5)
	if room.taken[0] is True:
		home1(room, player)
	# if room.taken[1] is True:
	# 	park1(room, player)
	# if room.taken[2] is True:
	# 	schl1(room, player)
	# if room.taken[3] is True:
	# 	lib1(room, player)



def home1(room, player):
	room.choice = 0
	name = room.user[room.place[0]]

	msg = "Home. What is home?"
	text(player, msg)

	if name is room.user[player]:
		msg = "I don't know..."
		text(player, msg)



# ==== Send game text ====
def text(player, msg):
	player.send(bytes(msg, "utf8"))
	sleep(1)



# ==== Calls clear screen in client ====
def clear(player):
	player.send((bytes("$$clr$$", "utf8")))



# ===================================
# Code and info gotten from these websites:
# https://stackoverflow.com/questions/7002429/how-can-i-extract-all-values-from-a-dictionary-in-python
# ===================================
