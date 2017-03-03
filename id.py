#! /usr/bin/env python 
# -*- coding:utf8 -*-

from socket import *
import time
import sqlite3

############## creation d'une base de donnée 
try:
	bdd ="employées"

	conn = sqlite3.connect(bdd)
	cur = conn.cursor()
	cur.execute("CREATE TABLE employee (nom TEXT, prenom TEXT,mdp TEXT)")
	cur.execute("INSERT INTO employee(nom,prenom,mdp) VALUES('zizi','saad','azerty')")
	cur.execute("INSERT INTO employee(nom,prenom,mdp) VALUES('idil','rida','qwerty')")
	cur.execute("INSERT INTO employee(nom,prenom,mdp) VALUES('nanah','ayoub','raja')")
	conn.commit()
	cur.execute("SELECT *  FROM employee")
	for i in cur:
		print(i)
except:
	None

#############################################

host ='127.0.0.1'
port = 8888
# stdr standardiste
stdr = socket(AF_INET,SOCK_STREAM)
stdr.bind((host,port))
stdr.listen(10)

print("[{}] serveur en écoute sur le port[{}] \n" .format(time.ctime(),port))
# cc = connection client , infoc = info client
cc , infoc = stdr.accept()

print("bienvenue sur le serveur de l'hopitale\nprocessus d'identifcation :\n")
print("=================================================================\n")

while True:
	
	cc.send(b"entrez votre nom :")
	nom = cc.recv(1024)
	print("info recu à [{}] : {}" .format(time.ctime(), nom))
		

##########    chercher si il ya un nom pareil dans la base de donnée
	if nom == "zizi":
		cc.send("ok")
		time.sleep(1)
	else:
		cc.send("nok")
		time.sleep(1)	
		continue

####################################################################
	cc.send("entrez votre prenom : ")
	prenom = cc.recv(1024)
	print("info recu à [{}] : {}" .format(time.ctime(), prenom))
##########    chercher si il ya un nom pareil dans la base de donnée
	if prenom == "saad":
		cc.send("ok")
		time.sleep(1)
	else:
		cc.send("nok")
		time.sleep(1)	
		continue

#####################################################################

	cc.send("entrez votre mpt de passe : ")
	mdp = cc.recv(1024)
	print("info recu à [{}] : {}" .format(time.ctime(), mdp))

	if mdp == "azerty":
		print(infoc,"est connecte")
	else:
		cc.send("nok")
		time.sleep(1)
		continue
