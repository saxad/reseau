# -*- coding: utf8 -*-
#serveur d’écho (version concurrente) 
#j'ai rajouté une ligne  mais c'est un mauvais choix
import thread, time
from socket import *

Host = '127.0.0.1'
Port = 8888
s = socket(AF_INET, SOCK_STREAM)
s.bind((Host, Port))
s.listen(5)
def now():
	return time.ctime(time.time())
def handleClient(connection):
	time.sleep(5)
	while 1:
		data = connection.recv(1024)
		if not data: break
		connection.send('Echo=>%s at %s' % (data, now()))
	connection.close()
def dispatcher():
	while 1:
		connection, address = s.accept()
		print 'Server connected by', address,
		print 'at', now()
		thread.start_new(handleClient, (connection,))
dispatcher()
