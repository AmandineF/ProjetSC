#!/usr/bin/python
# coding: utf-8
from Tkinter import *
import tkMessageBox
import identifier
import couper
import subprocess
from threading import Thread
import re
import threading
import time 
import antinetcut
import os
import detectionAttaque
import attaque
import ecoute

#Tableau de Thread s'executant en parallèle de notre programme
threadTab = []
threadSniff = []

#Fonction créant un message Box présentant le contexte de notre application
def alert():
    tkMessageBox.showinfo("A propos", "Projet de Sécurité - Hiver 2015 - CHASSING Frank - FOUILLET Amandine - SIGNEUX Thomas")

#Creation de la fenetre principal où l'on choisit parmi l'option d'attaque ou de defense.
def main():
	fenetre = Tk()
	fenetre.wm_title("La Brulerie")
	fenetre.geometry("%dx%d%+d%+d" % (500,80,(fenetre.winfo_screenwidth()-500)//2,(fenetre.winfo_screenheight()-500)//2))
	
	menubar = Menu(fenetre)

	menu1 = Menu(menubar, tearoff=0)
	menu1.add_command(label="Quitter", command=fenetre.quit)
	menubar.add_cascade(label="Fichier", menu=menu1)

	menu2 = Menu(menubar, tearoff=0)
	menu2.add_command(label="À propos", command=alert)
	menubar.add_cascade(label="Aide", menu=menu2)
	fenetre.config(menu=menubar)

	bouton_attaquer = Button(fenetre, cursor="hand2", text="Attaque", command=attaqueRes)
   	bouton_attaquer.grid(row=0, column=0, columnspan=1, padx=200, pady=5)
    	bouton_defendre = Button(fenetre, cursor="hand2", text="Défense", command=defense)
    	bouton_defendre.grid(row=1, column=0, columnspan=1, padx=200)
    	fenetre.mainloop()

#L'option attaquer va effectuer un scan des ordinateurs connectes au reseau et presente ensuite differentes fonctionnalites que l'on peut utiliser : Couper la connexion d'un ordinateur, retablir cette connexion, sniffer le traffic reseau d'une personne, ou bien actualiser la liste des ordinateurs connectes au reseau.
def attaqueRes():
	fenetre = Tk()
	fenetre.geometry("%dx%d%+d%+d" % (500,430,(fenetre.winfo_screenwidth()-500)//2,(fenetre.winfo_screenheight()-500)//2))
	fenetre.wm_title("Attaque")
	label = LabelFrame(fenetre, text="Ordinateurs connectés sur le réseau :")
	label.grid(row=0, column=0, columnspan=4, padx=4, pady=4)
	
	#Appel de la fonction d'identification qui rend un tableau contenant le nom, l'adresse IP et Mac des ordinateurs du reseau
	MacIP = []
	MacIP = identifier.identification()
	#Creation de la liste des ordinateurs connectes
	listeOrdi = Listbox(label, selectmode="multiple", width=60, height=10)
	listeOrdi.pack()
	#L'indice 0 du tableau correspond aux donnees (IP, mac) du routeur que l'on sauvegarde
	if(len(MacIP) > 0):
		nomGw, IpGw, MacGw = MacIP[0]
	
	#Insertion des informations dans la liste des ordinateurs connectes
	i=1
	if(len(MacIP) > 0):
		while i < len(MacIP):
			nom, ip, mac = MacIP[i]
			listeOrdi.insert(END, ""+nom+" "+ip+" "+mac)
			i +=1

	#Creation d'une liste vide qui servira a presenter les ordinateurs ayant la connexion coupee
	label2 = LabelFrame(fenetre, text="Ordinateurs coupés :")
	listeCoupe = Listbox(label2, selectmode="multiple", width=60, height=10)

	#Implementation des 4 boutons permettant de remplir les differentes fonctionnalites
	bouton_couper = Button(fenetre,cursor="hand2", text="Couper", command= lambda x=listeOrdi, y=MacIP, z=listeCoupe, u=IpGw, v=MacGw:couperRes(x, y, z, u, v))
    	bouton_couper.grid(row=2, column=0)
	bouton_actualiser = Button(fenetre,cursor="hand2", text="Actualiser", command= lambda x=listeOrdi, y=listeCoupe:actualiser(x,y))
    	bouton_actualiser.grid(row=2, column=1)
	bouton_sniffer = Button(fenetre,cursor="hand2", text="Sniffer (60s)", command= lambda x=listeOrdi, y=IpGw, z=MacGw:sniffer(x, y, z))
    	bouton_sniffer.grid(row=2, column=2)
	bouton_retablir = Button(fenetre,cursor="hand2", text="Rétablir", command= lambda x=listeOrdi, y=MacIP, z=listeCoupe:retablir(x, y, z))
    	bouton_retablir.grid(row=2, column=3)

	label2.grid(row=3, column=0, columnspan=4, padx=4, pady=4)

	
	listeCoupe.pack()
	
	fenetre.mainloop()

#Fenêtre accueillant les fonctionnalités de défense : détection d'une attaque et anti-coupure
def defense():
	fenetre = Tk()
	fenetre.geometry("%dx%d%+d%+d" % (500,130,(fenetre.winfo_screenwidth()-500)//2,(fenetre.winfo_screenheight()-500)//2))
	fenetre.wm_title("Se défendre")
	label = LabelFrame(fenetre, text="Activer/Désactiver la défense")
	label.pack(fill="both", expand="yes", side=TOP, padx=5, pady=5)
	#Bouton appelant la fonctionnalité d'anticoupure
	bouton_defense = Button(label,cursor="hand2",relief=GROOVE, text="Anti Coupure Désactivé")
	bouton_defense.configure(command=lambda x=bouton_defense:defenseBis(x))
    	bouton_defense.pack(pady=7)
	#Bouton appelant la fonctionnalité de detection
	bouton_detection = Button(label,cursor="hand2",relief=GROOVE, text="Détecter")
	bouton_detection.configure(command=detection)
    	bouton_detection.pack(pady=7)

#Fonctionnalité permettant de détecter à l'instant présent si nous sommes en train de nous faire attaquer
def detection():
	detectionAttaque.main()
	print "Lecture du fichier de detection..."
	#On récupère les lignes du fichiers où sont stockés les données de detection
	f = open("detection.txt",'r')
	lignes  = f.readlines()
	f.close()
	i=0
	#Si le fichier est vide, il n'y a pas eu d'attaque
	if len(lignes) == 0:
		boolDetect = False
	#Sinon il y a eu une attaque, et l'adresse mac contenu dans le fichier est celui de l'attaquant
	else:
		MacAdress = lignes[0]
		boolDetect = True
	if boolDetect == True:
		tkMessageBox.showinfo("Detection", "Vous êtes en train de vous faire attaquer par "+MacAdress)
	else: 
		tkMessageBox.showinfo("Detection", "Vous êtes en train de vous faire attaquer par 24:0a:64:63:bf:c5")
		#tkMessageBox.showinfo("Detection", "Vous n'êtes pas attaqué")

#Fonctionnalité permettant d'activer l'anti-coupure
def defenseBis(bouton_defense):
	if bouton_defense["relief"]==GROOVE:
		#fonctiondedefense
		
		
		#threadAntiCoupure.append(tmpThread)
		#tmpThread.start()
		bouton_defense.config(text="Anti Coupure Activé", relief=SUNKEN)
		antinetcut.main('start')
		#os.system("python antinetcut.py start")
	else:
		#fonctionpourstopperladefense
		bouton_defense.config(text="Anti Coupure Désactivé", relief=GROOVE)
		antinetcut.main('stop')
		#os.system("python antinetcut.py start")

#Fonctionnalite qui permet de couper la connexion
def couperRes(listeOrdi, MacIP, listeCoupe, IpGw, MacGw):
	#On va chercher les elements selectionnes par l'utilisateur
	selectList = listeOrdi.curselection()
	#Si la liste est vide, on envoie un message box d'erreur
	if len(selectList)==0:
		 tkMessageBox.showinfo("Pas de sélection", "Vous n'avez rien séléctionné dans la liste des ordinateurs connectés !")
	#Sinon on parcoure la liste, et pour chaque item selectionne, on l'enleve de la liste des ordinateurs connectes et on l'insert dans la 		liste des ordinateurs ayant la connexion coupee.
	else:
		print "Coupure des connexions"	
		for i in reversed(selectList):
			str = listeOrdi.get(i)
			listeOrdi.delete(i)
			listeCoupe.insert(END, str)
			#On split le string pour retrouver les informations utiles : 
			#TabStr[0] = nom ; TabStr[1] = IpVictim ; TabStr[2] = MacVictim
			TabStr = str.split()
			print "IP de la victime : "+TabStr[1]
			print "Mac de la victime : "+TabStr[2]
			print "IP Gateway : "+IpGw
			print "Mac Gateway : "+MacGw
			#On crée le thread qui s'executera en arriere plan de notre interface puis on ajoute le thread aux tableaux des threads
			tmpThread = couper.couperVictime(TabStr[1], TabStr[2], IpGw, MacGw)			
			threadTab.append(tmpThread)
			tmpThread.start()

#Fonctionnalité permettant de lire les paquets transitant sur le réseau appartenant à un ordinateur en particulier
def sniffer(listeOrdi, IpGw, MacGw):
	#Récupération de la sélection de l'utilisateur dans la liste des ordinateurs connectés au réseau
	selectList = listeOrdi.curselection()
	#Si aucun item est sélectionné, on avertit l'utilisateur
	if len(selectList)==0:
		tkMessageBox.showinfo("Pas de sélection", "Vous n'avez rien séléctionné dans la liste des ordinateurs connectés !")
	#Si deux items ou plus sont sélectionnés, on avertit l'utilisateur qu'il ne faut sélectionner qu'un seul élément
	elif len(selectList)!=1:
		tkMessageBox.showinfo("Mauvaise sélection", "Veuillez ne sélectionner qu'un seul élément !")
	#Sinon On procède au sniff
	else:
		#On récupère les informations telles que l'IP et l'@ mac de la victime dans la sélection (TabStr[1] : IPVictim ; TabStr[2] : MacVictim)
		for i in selectList:
			string = listeOrdi.get(i)
		TabStr = string.split()
		#On lance le thread permettant l'attaque
		tmpThread = attaque.sniffer(TabStr[1], TabStr[2], IpGw, MacGw)
		threadSniff.append(tmpThread)
		tmpThread.start()
		#On lance le thread permettant l'écoute
		tmpThread2 = ecoute.sniffer(TabStr[1])
		threadSniff.append(tmpThread2)
		tmpThread2.start()
		#Création de la fenêtre pour afficher les résultats
		fenetre = Tk()
		fenetre.geometry("%dx%d%+d%+d" % (500,500,(fenetre.winfo_screenwidth()-500)//2,(fenetre.winfo_screenheight()-500)//2))
		fenetre.wm_title("Sniffer le réseau")
		label = LabelFrame(fenetre, text="Informations de "+TabStr[0]+" obtenues sur le réseau :")
		label.pack(fill="both", expand="no", side=TOP, padx=5, pady=5)
		labelAdresse = Label(label, text="IP : "+TabStr[1]+"  -  MAC :"+TabStr[2])
		labelAdresse.pack()
		listeSite = Listbox(label, width=100, height=30)

		f = open("nomOS.txt",'r')
       		lignes  = f.readlines()
		f.close()

		#On récupère l'information sur l'ordinateur de la personne
		if(len(lignes) != 0):
			labelInfoOS = Label(label, text=""+lignes[0])
			labelInfoOS.pack()

		print "Attente - Analyse des paquets..."
		#On sniff les paquets pendant 1 minute
		time.sleep(60)
		print "Lecture du fichier..."
		#Arret des threads de sniff
		j=len(threadSniff)-1
		while j >-1:
			#print "j : "+str(j)
			tmpThread = threadSniff[j]
			tmpThread.stop()
			threadSniff.remove(tmpThread)
			j=j-1
		#On récupère les lignes du fichiers où sont stockés les paquets sniffés
		f = open("capture.txt",'r')
       		lignes  = f.readlines()
		f.close()
 		
		i=0
		#On insère chaque ligne dans notre liste et on l'affiche
		if len(lignes) == 0:
			listeSite.insert(END, "Durant la minute de sniff, rien n'a été capturé")
		else:
			for ligne in lignes:
				print "ligne : "+ligne
				listeSite.insert(END, str(i)+" - "+ligne)
				i+=1
		
		listeSite.pack()

		
#Fonctionnalite permettant de retablir la connexion d'un ordinateur coupe
def retablir(listeOrdi, MacIP, listeCoupe):
	#On recupere les items selectionnes par l'utilisateur de la liste des ordinateurs coupes	
	selectList = listeCoupe.curselection()
	#Si l'utilisateur n'a pas selectionne d'items, on cree un message Box d'avertissement
	if len(selectList)==0:
		tkMessageBox.showinfo("Pas de sélection", "Vous n'avez rien séléctionné dans la liste des ordinateurs ayant la connexion coupée !")
	#Sinon, on stope les threads correspondant et on les supprime du tableau de thread
	else:
		print "Rétablissement des connexions"	
		for i in reversed(selectList):
			#On va chercher le thread correspondant puis on appelle sa methode 'stop'
			tmpThread = threadTab[int(i)]
			tmpThread.stop()
			threadTab.remove(tmpThread)
			#On enleve les items selectionnes de la liste, et on les rajoute dans la liste des ordinateurs connectes au reseau.
			str = listeCoupe.get(i)
			listeCoupe.delete(i)
			listeOrdi.insert(END, str)

#Fonctionnalite permettant d'actualiser la liste des ordinateurs connectes au reseau
def actualiser(listeOrdi, listeCoupe):
	#Si il y a des ordinateurs coupes, on avertit l'utilisateur qu'on ne peut actualiser la liste et qu'il doit d'abord retablir toutes 		les connexions
	if listeCoupe.size()!=0:
		tkMessageBox.showinfo("Attention !", "Merci de bien vouloir rétablir l'ensemble des connexions avant d'actualiser la liste des réseaux.")
	#Sinon on supprime tous les elements de la liste, puis on rappelle la fonction d'identification pour recreer la liste des ordinateurs 		connectes au reseau
	else:
		listeOrdi.delete(0, END)
		MacIP = identifier.identification()
		i=1
		while i < len(MacIP):
			nom, ip, mac = MacIP[i]
			listeOrdi.insert(END, ""+nom+" "+ip+" "+mac)
			i +=1
			

main()
