#!/usr/bin/python
# coding: utf-8
from Tkinter import *

def alert():
    showinfo("alerte", "Bravo!")

def main():
	fenetre = Tk()
	fenetre.wm_title("La Brulerie")

	menubar = Menu(fenetre)

	menu1 = Menu(menubar, tearoff=0)
	menu1.add_command(label="Quitter", command=fenetre.quit)
	menubar.add_cascade(label="Fichier", menu=menu1)

	menu2 = Menu(menubar, tearoff=0)
	menu2.add_command(label="À propos", command=alert)
	menubar.add_cascade(label="Aide", menu=menu2)
	fenetre.config(menu=menubar)

	OPTIONS = [
	    ("Attaquer", option1()),
	    ("Défendre", option2())
	]

	for texte, com in OPTIONS:
	    Button(fenetre, text=texte, command = com).pack(fill="both",padx=2, pady=2)

	fenetre.mainloop()

def option1():
	fenetre = Tk()
	fenetre.wm_title("Attaque")
	label = LabelFrame(fenetre, text="Ordinateurs connectés sur le réseau :")
	label.pack(fill="both", expand="yes", side=TOP, padx=5, pady=5)
	#identifier()
def option2():
	print "2"
	#defendre()



main()