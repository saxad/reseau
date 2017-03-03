#! /usr/bin/env python
# -*- coding: utf8 -*-


import socket
import signal
import sys
from authentification import *

def decon(signal, frame):
	"""deconnecxion avec ctrl+C  """

	client.send("fin")
	client.close()
	print("deconnexion\n")
	sys.exit(0)

signal.signal(signal.SIGINT, decon)


hote = '127.0.0.1'
port = 12800
buf = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((hote,port))
print("connexion avec le serveur ")

connexion = True

while  connexion:

################################################################
#			 	    Authentification			  			   #
################################################################

	authentificationclient(client)
		
#	data = raw_input("... en attente d'une action a envoyer")

################################################################
#			 	  ici faut mettre les actions	  			   #
################################################################

	data = client.recv(buf)
	print(data)
	data = raw_input("message envoyee: ")
	client.send(data)
	if data == "fin":
		break
	data = client.recv(buf)
	print("message recu : {}" .format(data))



client.close()
