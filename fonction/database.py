#! /usr/bin/env python
# -*- coding: utf8 -*-


import sqlite3



def creation():
	""" creation de la table initiale avec des mdp par defaut azerty, qwerty"""
	try:

		bdd = "employees"
		conn = sqlite3.connect(bdd)
		conn.text_factory = str
		cur = conn.cursor()


		cur.execute("CREATE TABLE employee (nom TEXT, prenom TEXT, mdp TEXT) ")
		cur.execute("INSERT INTO employee(nom, prenom, mdp) VALUES('prieur','paul','azerty')")
		cur.execute("INSERT INTO employee(nom, prenom, mdp) VALUES('zizi','saad','azerty')")
		cur.execute("INSERT INTO employee(nom, prenom, mdp) VALUES('dendekker','benjamin','azerty')")
		cur.execute("INSERT INTO employee(nom, prenom, mdp) VALUES('hue','charly','azerty')")

		conn.commit()
		cur.execute("SELECT * FROM employee")
		for i in cur:
			print(i)
	except:
		None



def isintable( nomid, prenomid, mdpid,bdd="employees"):

	conn = sqlite3.connect(bdd)
	cur = conn.cursor()
	personne = cur.execute("SELECT *  FROM employee WHERE nom= ? and prenom= ? and mdp= ?  ",(nomid,prenomid,mdpid))

	liste = cur.fetchall()

	if  len(liste) == 0   :
		print("mdp ou nom/prenom incorrecte")
		return 0
	else:
		print("utilisateur accepté \nVous etes connecté au serveur de l'Hopital")
		return 1

if __name__ == "__main__":
	creation()
	isintable('prieur','paul','azerty',"employees")
