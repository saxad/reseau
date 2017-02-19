#! /usr/bin/env python
# -*- coding:utf8 -*-

from socket import *
import time
from getpass import getpass


connexion = socket(AF_INET,SOCK_STREAM)

connexion.connect(('127.0.0.1',8888))

while True:
	print(connexion.recv(1024))
	data = raw_input("")
	connexion.send(data)
	data = ""

	data = connexion.recv(1024)
	print(repr(data))
	print("le client a recu : {}   \n".format(data))

	if data == "ok":
		print("id ok \n")
	else:
		print("nom n'exista pas recommencez l'identification : \n")
		continue
	data =""

	print(connexion.recv(1024))
	data = raw_input("")
	connexion.send(data)
	data = connexion.recv(1024)
	print(data)
	if data == "ok":
		print("prenom ok ")
	else:
		print("prenom n'exista pas recommencez l'identification : \n")
		continue

	data=""
	data = connexion.recv(1024)
	print(data)
	data = getpass("entre mot de passe : ")
	
	connexion.send(data)
	data = ""
	data = connexion.recv(1024)
	print(repr(data))
	if data == "nok":
		print("mot de passe incorrect recommencez l'identification")
		continue
	else:
		print("vous connectez au serveur")
