#! /usr/bin/env python
# -*- coding: utf8 -*-


import socket
import signal
import sys


def decon(signal, frame):
	"""deconnection brutal """
		
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
	
	data = raw_input("message envoyee: ")
	client.send(data)
	if data == "fin":
		break
	data = client.recv(buf)
	print("message recu : {}" .format(data))
	

client.close()


