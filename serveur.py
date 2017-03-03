# -*- coding: utf8 -*-
#serveur d’écho (version concurrente)

import thread, time

from socket import *


Host = '127.0.0.1'
Port = 8888
s = socket(AF_INET, SOCK_STREAM)
s.bind((Host, Port))
s.listen(5)
##########  retourn l'heure actuelle

def now():
	return time.ctime(time.time())

#############   imprimer ce qui est recu + temps
def handleClient(connection):
	time.sleep(5)
	while 1:
		data = connection.recv(1024)

#		if not data: break
		if data == "saad":
			connection.send('Echo (%s) : mot de passe correct' % (now()))
		else:
			print(repr(data)," c'est pas un mdp valable")
			
			continue
	connection.close()

############### accepte la connection d'un client
def dispatcher():
	while 1:
		connection, address = s.accept()
		print 'Server connected by', address,
		print 'at', now()
		thread.start_new(handleClient, (connection,))	

###############  debut du programme 
dispatcher()
