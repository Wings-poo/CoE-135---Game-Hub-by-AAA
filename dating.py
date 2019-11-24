# python3 code
# CoE 135 - My Last Days with You - Dating Sim
# ===================================

from time import sleep

# ==== Main ====
def play(room, player):
	clear(player)
	sleep(0.5)
	player.send((bytes("My Last Days with You - Dating Sim", "utf8")))
	sleep(1)


	sleep(1)
	player.send((bytes("=========== Game End ===========", "utf8")))



# ==== Broadcasts a message to all players in the room ====
def gamecast(room, msg):

	for sock in room:
		sock.send(bytes(msg, "utf8"))



# ==== Calls clear screen in client ====
def clear(player):
	player.send((bytes("$$clr$$", "utf8")))



# ===================================
# Code and info gotten from these websites:
# https://www.geeksforgeeks.org/clear-screen-python/
# ===================================
