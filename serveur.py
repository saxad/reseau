#! /usr/bin/env python
# -*- coding: utf8 -*-


from authentification import *
import socket
import threading
import sys

host = '127.0.0.1'
port = 7412

########### THREAD QUI S'OCCUPE DES CLIENTS ###########

class threadclient(threading.Thread):  # threadclient herite les caractéristique de THREAD

    def __init__(self, client):   # constructeur de classe
        threading.Thread.__init__(self)
        self.connexion = client


# run c'est une methode de la classe thread qu'on va surchargé
    def run(self):
        nom = self.getName()
        print("la valeur de nom ", nom)
        while 1 :
            authentificationserveur(self.connexion)
            
#################### FIN DU THREAD ####################



connexion_principal = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    connexion_principal.bind((host,port))
except socket.error:
    print("erreur du bind")
    sys.exit()

print("le serveur attend des clients\n")
connexion_principal.listen(10)

while 1:
    client, adresse = connexion_principal.accept()
    ##################    creation du threading
    th = threadclient(client)
    th.start()  # demmarer le thread
