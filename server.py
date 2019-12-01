# python3 code
# CoE 135 - Game Hub Server
# ===================================

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import password
import dating
import bfftest
import wwtbm

# ==== The struct of the room ====
class Room(object):

	def __init__(self, name, username, game, password):
		super(Room, self).__init__()
		# Initialize the variables first
		self.names = []
		self.user = {}
		self.game = ""
		self.password = ""
		self.num = 0
		self.state = False				# If playing or not

		self.names.append(name)			# List of players (client variable)
		self.user[name] = username		# List of usernames of the players
		self.game = game				# Name of the game to be played
		self.password = password
		self.num = 1;					# Number of players in room

	def add(self, name, username):
		self.names.append(name)
		self.user[name] = username
		self.num += 1

	def datingsim(self):
		# Initialize the variables needed for dating sim
		self.place = []
		self.taken = []
		self.choice = 0
		self.score = {}

		for i in range(4):
			self.place.append("")
			self.taken.append(False)

		for i in self.names:
			self.score[i] = 0



# ==== Server for multithreaded (asynchronous) chat application ====

txt = "\nWhat game will you play?\n"
txt += "A) My Last Days with You - Dating Sim\n"
txt += "B) BFF Test\n"
txt += "C) Who wants to be a Millionaire\n"



# ==== Sets up handling for incoming clients ====
def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Username: 8 ASCII characters only", "utf8"))
        addresses[client] = client_address
        Thread(target = handle_client, args = (client,)).start()




# ==== Handles a single client connection ====
def handle_client(client):  # Takes client socket as argument.
	global hotel
	host = False

	# If the username is not within specs/taken at the start
	while True:
		name = client.recv(BUFSIZ).decode("utf8")

		if not name.isprintable():
			# Detected characters that could not be printed (non-ASCII)
			client.send(bytes("Detected non-ASCII characters. Please try again.", "utf8"))
		elif name not in username and len(name) <= 8:
			break
		elif len(name) > 8:
			client.send(bytes("Username exceeds 8 characters. Please try again.", "utf8"))
		elif name in username:
			client.send(bytes("Username is taken. Please try again", "utf8"))

	client.send(bytes("Welcome %s!" % name, "utf8"))


	# Ask what to do
	client.send(bytes("Will you A) join a room or B) create one?", "utf8"))
	msg = client.recv(BUFSIZ)
	msg = msg.decode("utf8").upper()

	if msg == "A":
		if not hotel: #No room exists? Get kicked
			client.send(bytes("There's no room. GG", "utf8"))
			client.send(bytes("$$quit$$", "utf8"))
			client.close()
			print("%s:%s has disconnected" % addresses[client])
			return

		client.send(bytes("Type the room password", "utf8"))
		msg = client.recv(BUFSIZ)
		msg = msg.decode("utf8")

		if msg in hotel.keys(): # Password exists
			pw = msg

			if hotel[pw].num == 4 or (hotel[pw].num >= 1 and hotel[pw].game == "C"): # Room is full
				client.send(bytes("Sadt. Room is full", "utf8"))
				client.send(bytes("$$quit$$", "utf8"))
				client.close()
				print("%s:%s has disconnected" % addresses[client])
				return

			# Join the room
			hotel[pw].add(client, name)
			client.send(bytes("You've successfully joined a room", "utf8"))


		else: #Get kicked
			client.send(bytes("GG. No room with that password. Get rekt", "utf8"))
			client.send(bytes("$$quit$$", "utf8"))
			client.close()
			print("%s:%s has disconnected" % addresses[client])
			return


	elif msg == "B":
		# Create password
		pw = password.create()
			# If room with the password exists already, create new
		while pw in hotel.keys():
			pw = password.create()

		client.send(bytes("Room is created successfully. Password is " + pw, "utf8"))
		host = True

		# Which game to play?
		while True:
			client.send(bytes(txt, "utf8"))
			msg = client.recv(BUFSIZ)

			# Initialize the class
			msg = msg.decode("utf8").upper()
			if (msg >= "A" and msg <= "B"):
				hotel[pw] = Room(client, name, msg, pw)
				client.send(bytes("Waiting for other players...", "utf8"))
				break
			elif (msg == "C"):
				hotel[pw] = Room(client, name, msg, pw)
				client.send(bytes("Type $$game$$ to start", "utf8"))
				break


	else: #Incorrect == Get kicked
		client.send(bytes("GG. U SUK", "utf8"))
		client.send(bytes("$$quit$$", "utf8"))
		client.close()
		print("%s:%s has disconnected" % addresses[client])
		return



	clients[client] = name
	username[name] = client
	msg = "%s has joined the server!" % name
	widecast(client, hotel[pw].names, bytes(msg, "utf8"), "")
	msg = ""

	while True:
		while host == True: # Wait for the start game
			msg = client.recv(BUFSIZ)
			msg = msg.decode("utf8")

			if msg == "$$game$$" and hotel[pw].num > 1:
				hotel[pw].state = True
				if hotel[pw].game == "A":		# Play the dating sim
					dating.play(hotel[pw], client)
				elif hotel[pw].game == "B":		# Play the BFF test
					bfftest.play(hotel[pw], client)


				hotel[pw].state = False
				msg = "$$quit$$"
				break
			elif msg == "$$game$$" and hotel[pw].num == 1 and hotel[pw].game == "C": # Play the Who wants to be a Millionaire
				hotel[pw].state = True
				wwtbm.menu(client)
				hotel[pw].state = False
				msg = "$$quit$$"
				break
			elif msg == "$$game$$":
				client.send(bytes("Not enough players", "utf8"))


		# ==== Forced to be in the game ====
		if hotel[pw].state == True:
			if hotel[pw].game == "A":		# Play the dating sim
				dating.play(hotel[pw], client)
			elif hotel[pw].game == "B":		# Play the BFF test
				bfftest.play(hotel[pw], client)
			else:							# Play the Who wants to be a Millionaire
				wwtbm.menu(client)


			msg = "$$quit$$"


		# ==== Game done ====
		if msg == "$$quit$$":
			# Delete the existence of the client
			client.send(bytes("$$quit$$", "utf8"))
			client.close()
			del clients[client]

			# Remove the usernames used by the client that left
			for key, value in dict(username).items():
				if value == client:
					del username[key]

			# Inform the server and the other clients who left
			print("%s:%s has disconnected" % addresses[client])

			if host == True: # Room is now gone
				del hotel[pw]

			break




# ==== Broadcasts a message to all the clients except sender ====
def widecast(sender, room, msg, prefix = ""):  # prefix is for name identification.

	for sock in room:
		if sock != sender:
			sock.send(bytes(prefix, "utf8")+msg)




# ==== Main function ====
username = {}						# Lists of usernames (Checks for duplicates)
clients = {}						# Clients and their current username
addresses = {}
hotel = {}							# Lists of rooms (key is password)

# HOST = input('Server IP: ')
# PORT = int(input('Port number: '))
HOST = "127.0.0.1"
PORT = 6969
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
SERVER.close()
# ===================================
# Code and info gotten from these websites:
# https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170
# https://pyformat.info/
# https://docs.python.org/3.7/library/stdtypes.html#str.isprintable
# https://stackoverflow.com/questions/29218750/what-is-the-best-way-to-remove-a-dictionary-item-by-value-in-python
# https://stackoverflow.com/questions/35568543/python-adding-an-empty-list-as-value-to-a-dictionary/35568620
# https://trinket.io/python/99f458ee11
# https://stackoverflow.com/questions/12454675/whats-the-return-value-of-socket-accept-in-python
# https://stackoverflow.com/questions/45370731/what-does-the-parameter-of-1-mean-in-listen1-method-of-socket-module-in-pyth
# http://net-informations.com/python/iq/global.htm
# https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3
# https://www.hackerearth.com/practice/python/object-oriented-programming/classes-and-objects-i/tutorial/
# ===================================
