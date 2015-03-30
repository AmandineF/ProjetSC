#!/usr/bin/python
# coding: utf-8
from Tkinter import *
import tkMessageBox

def alert():
    tkMessageBox.showinfo("A propos", "Projet de Sécurité - Hiver 2015 - CHASSING Frank - FOUILLET Amandine - SIGNEUX Thomas")

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

	bouton_attaquer = Button(fenetre, cursor="hand2", text="Attaque", command=attaque)
    bouton_attaquer.grid(row=0, column=0, columnspan=1, padx=200, pady=5)
    bouton_defendre = Button(fenetre, cursor="hand2", text="Défense", command=defense)
    bouton_defendre.grid(row=1, column=0, columnspan=1, padx=200)
    fenetre.mainloop()

def attaque():
	fenetre = Tk()
	fenetre.geometry("%dx%d%+d%+d" % (500,430,(fenetre.winfo_screenwidth()-500)//2,(fenetre.winfo_screenheight()-500)//2))
	fenetre.wm_title("Attaque")
	label = LabelFrame(fenetre, text="Ordinateurs connectés sur le réseau :")
	label.grid(row=0, column=0, columnspan=3, padx=4, pady=4)
	
	MacIP = []
	couple = ("PCdeFrank", "192.168.0.106", "54:ae:27:2d:a3:6a")
	couple2 = ("MacDAmandine", "192.168.0.107", "54:ae:27:2d:c3:6b")
	MacIP.append(couple)
	MacIP.append(couple2)
	#MacIP = identification()
	listeOrdi = Listbox(label, selectmode="multiple", width=60, height=10)
	listeOrdi.pack()
	i=0
	while i < len(MacIP):
		nom, ip, mac = MacIP[i]
		listeOrdi.insert(END, ""+nom+" "+ip+" "+mac)
		i +=1

	label2 = LabelFrame(fenetre, text="Ordinateurs coupés :")
	listeCoupe = Listbox(label2, selectmode="multiple", width=60, height=10)

	bouton_couper = Button(fenetre,cursor="hand2", text="Couper", command= lambda x=listeOrdi, y=MacIP, z=listeCoupe:couper(x, y, z))
    bouton_couper.grid(row=2, column=0)
	bouton_sniffer = Button(fenetre,cursor="hand2", text="Sniffer", command= lambda x=listeOrdi, y=MacIP:sniffer(x, y))
    bouton_sniffer.grid(row=2, column=1)
	bouton_retablir = Button(fenetre,cursor="hand2", text="Rétablir", command= lambda x=listeOrdi, y=MacIP, z=listeCoupe:retablir(x, y, z))
    bouton_retablir.grid(row=2, column=2)

	label2.grid(row=3, column=0, columnspan=3, padx=4, pady=4)

	
	listeCoupe.pack()
	
	fenetre.mainloop()
def defense():
	fenetre = Tk()
	fenetre.geometry("%dx%d%+d%+d" % (500,80,(fenetre.winfo_screenwidth()-500)//2,(fenetre.winfo_screenheight()-500)//2))
	fenetre.wm_title("Se défendre")
	label = LabelFrame(fenetre, text="Activer/Désactiver la défense")
	label.pack(fill="both", expand="yes", side=TOP, padx=5, pady=5)
	champLabel = Label(label, text="Défense Inactive")
	#champLabel.pack()
	bouton_defense = Button(label,cursor="hand2",relief=GROOVE, text="Défense Désactivé")
	bouton_defense.configure(command=lambda x=bouton_defense, y=champLabel:defenseBis(x,y))
    bouton_defense.pack(pady=7)

def defenseBis(bouton_defense, champLabel):
	if bouton_defense["relief"]==GROOVE:
		#fonctiondedefense
		#champLabel.config(text="Défense Active")
		bouton_defense.config(text="Défense Activé", relief=SUNKEN)
	else:
		#fonctionpourstopperladefense
		#champLabel.config(text="Défense Inactive")
		bouton_defense.config(text="Défense Désactivé", relief=GROOVE)

def couper(listeOrdi, MacIP, listeCoupe):
	print "Couper la co"
	selectList = listeOrdi.curselection()
	print selectList
	if len(selectList)==0:
		 tkMessageBox.showinfo("Pas de sélection", "Vous n'avez rien séléctionné dans la liste des ordinateurs connectés !")
	else:
		print "Coupure des connexions"	
		for i in reversed(selectList):
			str = listeOrdi.get(i)
			listeOrdi.delete(i)
			listeCoupe.insert(END, str)
			#couper(ip, mac) -> parser pour obtenir l'ip et l'@ mac
			print str
	
def sniffer(listeOrdi, MacIP):
	selectList = listeOrdi.curselection()
	if len(selectList)==0:
		tkMessageBox.showinfo("Pas de sélection", "Vous n'avez rien séléctionné dans la liste des ordinateurs connectés !")
	elif len(selectList)!=1:
		tkMessageBox.showinfo("Mauvaise sélection", "Veuillez ne sélectionner qu'un seul élément !")
	else:
		fenetre = Tk()
		fenetre.geometry("%dx%d%+d%+d" % (500,500,(fenetre.winfo_screenwidth()-500)//2,(fenetre.winfo_screenheight()-500)//2))
		fenetre.wm_title("Sniffer le réseau")
		for i in selectList:
			string = listeOrdi.get(i)
			sTab = string.split()
		label = LabelFrame(fenetre, text="Informations de "+sTab[0]+" obtenues sur le réseau :")
		label.pack(fill="both", expand="no", side=TOP, padx=5, pady=5)
		labelAdresse = Label(label, text="IP : "+sTab[1]+"  -  MAC :"+sTab[2])
		labelAdresse.pack()
		strTab = []
		for j in range(1,15):
			strTab.append("www.google.fr")
			strTab.append("www.facebook.com")
			strTab.append("www.twitter.fr")
		#strTab = fonctiondesniff()
		listeSite = Listbox(label, width=100, height=30)
		listeSite.pack()
		i=1
		for s in strTab:
			print str(i)+" - "+s
			listeSite.insert(END, str(i)+" - "+s)
			i+=1
		

def retablir(listeOrdi, MacIP, listeCoupe):
	selectList = listeCoupe.curselection()
	if len(selectList)==0:
		tkMessageBox.showinfo("Pas de sélection", "Vous n'avez rien séléctionné dans la liste des ordinateurs ayant la connexion coupée !")
	else:
		print "Rétablissement des connexions"	
		for i in reversed(selectList):
			str = listeCoupe.get(i)
			listeCoupe.delete(i)
			listeOrdi.insert(END, str)
			#retablir(ip, mac) 
			print str			
	

main()