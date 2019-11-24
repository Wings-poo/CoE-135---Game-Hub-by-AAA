# python3 code
# CoE 135 - Client
# ===================================

import socket
import sys
import re
from threading import Thread
import time
from os import system, name


# ==== Clears screen ====
def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')



# ==== Handles receiving of messages ====
def receive():

	while True:
		try:
			msg = client.recv(BUFSIZ).decode("utf8")

			if msg == "$$quit$$" or msg == '':
				client.close()
				break

			elif msg == "$$clr$$":
				clear()
				continue

			print(msg)
		except OSError:  # Possibly client has left the chat.
			break


# ==== Handles sending of messages ====
def send():		# event is passed by binders.

	while True:
		msg = input()
		client.send(bytes(msg, "utf8"))




# ==== Main function ====
# HOST = input('Server IP: ')
# PORT = int(input('Port number: '))
HOST = "127.0.0.1"
PORT = 6969
BUFSIZ = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try: client.connect((HOST, PORT))
except:		#If couldn't connect or invalid HOST/PORT
	print('Could not connect to %s:%d' % (HOST, PORT) )
	sys.exit()

receive_thread = Thread(target = receive)
send_thread = Thread(target = send)
# receive_thread.daemon = True
send_thread.daemon = True
receive_thread.start()
send_thread.start()
receive_thread.join()

# ===================================
# Code and info gotten from these websites:
# https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170
# https://github.com/SrishtiSengupta/MultithreadedChat/blob/master/client_ipv6.py
# https://docs.python.org/3/library/re.html#re.IGNORECASE
# https://stackoverflow.com/questions/28955005/python-replace-nth-word-in-string
# https://stackoverflow.com/questions/1635080/terminate-a-multi-thread-python-program
# ===================================
