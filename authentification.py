#! /usr/bin/env python
# -*- coding: utf8 -*-

from getpass import getpass
from  database import *
import socket

def deconnexion(client, clients_a_lire,clients_connectes):
	client.close()
	clients_a_lire.remove(client)
	clients_connectes.remove(client)


def authentificationserveur(client):

	identification = 1
	#while identification != 0:

	print("=====================================\n")
	print("----Authentification cote serveur----\n")
	print("=====================================\n")

	buf = 1024
	nom = client.recv(buf)
	print "message recu : ",nom
	client.send("recu")

	prenom = client.recv(buf)

	print "message recu : ",prenom
	client.send("recu")

	mdp = client.recv(buf)
	print "message recu : ", mdp
	client.send("recu")

	identification = 	isintable(nom,prenom,mdp,"employees")
	print(identification)
	return 0



def authentificationclient(client):

	print("====================================\n")
	print("----Authentification cote client----\n")
	print("====================================\n")

	buf = 1024

	data = raw_input("entre ton nom : ")
	client.send(data)
	data = client.recv(buf)
	print "serveur : ", data

	data = raw_input("entre ton prenom : ")
	client.send(data)
	data = client.recv(buf)
	print "serveur : ", data

	data = getpass("entre ton mot de passe : ")
	###### Faut chiffrer le mot de passe avant de l'envoyer ######
	client.send(data)
	data = client.recv(buf)
	print "serveur : ", data
