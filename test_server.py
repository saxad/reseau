#! /usr/bin/env python
# -*- coding: utf8 -*-


import socket
import select
import signal


		

hote = '127.0.0.1'
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(10)
print("Le serveur écoute à présent sur le port {}".format(port))


serveur_lance = True

clients_connectes = []

while serveur_lance:
	    
	connexions_demandees, wlist, xlist = select.select([connexion_principale],[], [], 0)
    
	for connexion in connexions_demandees:
		connexion_avec_client, infos_connexion = connexion.accept()
		print("{} est connecte" .format(infos_connexion))
 		clients_connectes.append(connexion_avec_client)

	clients_a_lire = []
	
	try:
		clients_a_lire, wlist, xlist = select.select(clients_connectes,
                [], [], 0)
	except select.error:
		pass
	else:      
		for client in clients_a_lire:
       	     
######   ==============================>>>>      ici on doit rajouter la fonction d'identification   
###############    et le traitment sera dans cette partie
			
			msg_recu = client.recv(1024)
			msg_recu = msg_recu.decode()
			print("Reçu {}".format(msg_recu))
			client.send(b"recu")

			if msg_recu == "fin":
				client.close()
				clients_a_lire.remove(client)
				clients_connectes.remove(client)
#				serveur_lance = False

print("Fermeture des connexions")
for client in clients_connectes:
	client.close()

connexion_principale.close()
