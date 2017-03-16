import os
import subprocess as sub

Origin_Path = '/root/projet_reseau'


def cd(arg):
	if arg[0]!='/':
		path = os.getcwd() + '/' + arg
	else:
		path = arg
	try:
		os.chdir(path)
		return os.getcwd()[len(Origin_Path):]
	except:
		print "Repertoire inconnu"

def cat(arg):
	if arg[0]!='/':
		path = os.getcwd() + '/' + arg
	else:
		path = arg
	try :
		data=''
		file = open(path, 'r')
		file_content = file.readlines()
		for line in file_content:
			data+=line
		file.close()
	except :
		data = "Nom de fichier incorrect"
	return data

def shell(client):
	path = ''
	os.chdir(Origin_Path)
	#client.send('Tapez exit pour quitter\n>> ')
	cmd = client.recv(1024)
	while cmd != 'exit':
		if cmd[:2] == 'cd':
			path = cd(cmd[3:])
			if path != '' : path += '/'

		elif cmd[:3] == 'cat':
			data = cat(cmd[4:])

		else:
			try:
				data = sub.check_output(cmd, shell=False)
				print(data)

			except:
				data = ('Commande inconnue')

		client.send(data)
		#client.send(path + '>> ') #il faut modifier cette ligne pour que path+ '>> ' soit envoye au client
		cmd = client.recv(1024)

#shell()
