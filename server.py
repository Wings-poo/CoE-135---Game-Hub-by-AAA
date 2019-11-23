# python3 code
# CoE 135 - Server
# ===================================

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import hangman


# ==== The struct of the room ====
class Room(object):
	names = [];						# List of players (client variable)
	user = [];						# List of usernames of the players
	game = "";						# Name of the game to be played
	password = "";

	def __init__(self, name, username, game, password):
		super(Room, self).__init__()
		self.names.append(name);
		self.user.append(username);
		self.game = game;
		self.password = password;

	def add(self, name, username):
		self.names.append(name);
		self.user.append(username);


# ==== Server for multithreaded (asynchronous) chat application ====

txt = "What game will you play?\n";
txt += "A) My Last Days with You - Dating Sim\n";
txt += "B) BFF Test\n";
txt += "C) Who wants to be a Millionaire\n";



# ==== Sets up handling for incoming clients ====
def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept();
        print("%s:%s has connected." % client_address);
        client.send(bytes("Username: 8 ASCII characters only", "utf8"));
        addresses[client] = client_address;
        Thread(target = handle_client, args = (client,)).start();


# ==== Handles a single client connection ====
def handle_client(client):  # Takes client socket as argument.
	global room;
	global hub;
	host = False;

	# If the username is not within specs/taken at the start
	while True:
		name = client.recv(BUFSIZ).decode("utf8");

		if not name.isprintable():
			# Detected characters that could not be printed (non-ASCII)
			client.send(bytes("Detected non-ASCII characters. Please try again.", "utf8"));
		elif name not in username and len(name) <= 8:
			break;
		elif len(name) > 8:
			client.send(bytes("Username exceeds 8 characters. Please try again.", "utf8"));
		elif name in username:
			client.send(bytes("Username is taken. Please try again", "utf8"));

	welcome = 'Welcome %s! ' % name;
	client.send(bytes(welcome, "utf8"));

	PASSWORD = "123";
	client.send(bytes("Will you A) join a room or B) create one? (A/B)", "utf8"));
	msg = client.recv(BUFSIZ);
	msg = msg.decode("utf8");

	if msg == "A" or msg == "a":
		if room is False: #No room exists? Get kicked
			client.send(bytes("There's no room. GG", "utf8"));
			client.send(bytes("$$quit$$", "utf8"));
			client.close();
			print("%s:%s has disconnected" % addresses[client]);
			return;

		client.send(bytes("Type the room password", "utf8"));
		msg = client.recv(BUFSIZ);

		if msg != bytes(PASSWORD, "utf8"): #Get kicked
			client.send(bytes("GG. U SUK", "utf8"));
			client.send(bytes("$$quit$$", "utf8"));
			client.close();
			print("%s:%s has disconnected" % addresses[client]);
			return;

		# Join the room
		hub.add(client, name);


	elif msg == "B" or msg == "b":
		if room: #Room exists? Get kicked
			client.send(bytes("GG, room is made", "utf8"));
			client.send(bytes("$$quit$$", "utf8"));
			client.close();
			print("%s:%s has disconnected" % addresses[client]);
			return;

		client.send(bytes("Room is created successfully. Password is " + PASSWORD, "utf8"));
		host = True;
		room = True;

		# Which game to play?
		while True:
			client.send(bytes(txt, "utf8"));
			msg = client.recv(BUFSIZ);

			# Initialize the class
			msg = msg.decode("utf8");
			if (msg >= "A" and msg <= "C") or (msg >= "a" and msg <= "c"):
				hub = Room(client, name, msg, PASSWORD);
				break;


		client.send(bytes("Waiting for other players...", "utf8"));

	else: #Incorrect == Get kicked
		client.send(bytes("GG. U SUK", "utf8"));
		client.send(bytes("$$quit$$", "utf8"));
		client.close();
		print("%s:%s has disconnected" % addresses[client]);
		return;



	clients[client] = name;
	username[name] = client;

	msg = "%s has joined the server!" % name;
	widecast(client, bytes(msg, "utf8"), "");

	while True:
		msg = client.recv(BUFSIZ);

		# print('Game state:'+str(game_state));

		# ==== Forced to be in the game ====
		if hangman.game_state == True:
			hangman.hangMan(client, clients);
			client.send(bytes(" ==== Game ended ====\n", "utf8"));

		# ==== Client leaves ====
		elif msg == bytes("$$quit$$", "utf8"):
			# Delete the existence of the client
			client.send(bytes("$$quit$$", "utf8"));
			client.close();
			del clients[client];

			# Remove the usernames used by the client that left
			for key, value in dict(username).items():
				if value == client:
					del username[key];

			# Inform the server and the other clients who left
			print("%s:%s has disconnected" % addresses[client]);
			broadcast(bytes("%s has left the server." % name, "utf8"));

			if host == True: # Room is now gone
				room = False;

			break;


		# ==== Commands ====
		elif msg.decode("utf8").startswith('$$') and msg.decode("utf8").endswith('$$'):
			split_msg = msg.decode("utf8");
			split_msg = split_msg[2:-2];			# Remove the $$
			split_msg = split_msg.split(',');		# Tokenize

						# ==== Game ====
			if "game" == split_msg[0]:
				hangman.game_state = True;
				hangman.guesses = 0;

				hangman.word = hangman.selectWord()
				hangman.word_list = [];
				for i in range(len(hangman.word)):
					hangman.word_list += hangman.word[i]

				hangman.blanks = "_ ";
				hangman.blanks_list = [];
				for i in range(len(hangman.word)):
					hangman.blanks_list.append(hangman.blanks)

				hangman.new_blanks_list = [];
				for i in range(len(hangman.word)):
					hangman.new_blanks_list.append(hangman.blanks)

				hangman.game_broadcast(bytes("Let's play hangman!\n", "utf8"), clients)
				hangman.print_scaffold(hangman.guesses, hangman.word, clients)
				hangman.game_broadcast(bytes("\n", "utf8"), clients)
				hangman.game_broadcast(bytes("" + ' '.join(hangman.blanks_list), "utf8"), clients)
				hangman.game_broadcast(bytes("\n", "utf8"), clients)
				hangman.game_broadcast(bytes("Guess a letter.\n", "utf8"), clients)

				hangman.guess_list = []
				hangman.hangMan(client, clients);
				client.send(bytes(" ==== Game ended ====\n", "utf8"));


			elif "room" == split_msg[0]:
				print(hub.game);
				print(hub.password);
				for a in hub.user:
					print(a);

			# ==== Error Message ====
			else:
				client.send(bytes("Error: Command not found", "utf8"));

		else:
			widecast(client, msg, "%-8s: " %name);



# ==== Broadcasts a message to all the clients ====
def broadcast(msg, prefix = ""):  # prefix is for name identification.

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg);



# ==== Broadcasts a message to all the clients except sender ====
def widecast(sender, msg, prefix = ""):  # prefix is for name identification.

	for sock in clients:
		if sock != sender:
			sock.send(bytes(prefix, "utf8")+msg);



# ==== Main function ====
username = {};						# Lists of usernames (Checks for duplicates)
clients = {};						# Clients and their current username
addresses = {};
room = False;

# HOST = input('Server IP: ');
# PORT = int(input('Port number: '));
HOST = "127.0.0.1";
PORT = 9999;
BUFSIZ = 1024;
ADDR = (HOST, PORT);

SERVER = socket(AF_INET, SOCK_STREAM);
SERVER.bind(ADDR);

if __name__ == "__main__":
    SERVER.listen(5);
    print("Waiting for connection...");
    ACCEPT_THREAD = Thread(target=accept_incoming_connections);
    ACCEPT_THREAD.start();
    ACCEPT_THREAD.join();
SERVER.close();

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
