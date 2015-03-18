#!/usr/bin/python
# coding: utf-8
from Tkinter import *
import identifier

def alert():
    showinfo("alerte", "Bravo!")

def main():
	fenetre = Tk()
	fenetre.wm_title("La Brulerie")

	menubar = Menu(fenetre)

	menu1 = Menu(menubar, tearoff=0)
	menu1.add_command(label="Créer", command=alert)
	menu1.add_command(label="Editer", command=alert)
	menu1.add_separator()
	menu1.add_command(label="Quitter", command=fenetre.quit)
	menubar.add_cascade(label="Fichier", menu=menu1)

	menu2 = Menu(menubar, tearoff=0)
	menu2.add_command(label="À propos", command=alert)
	menubar.add_cascade(label="Aide", menu=menu2)
	fenetre.config(menu=menubar)

	label = LabelFrame(fenetre, text="Options disponibles :")
	label.pack(fill="both", expand="yes", side=TOP, padx=5, pady=5)


	OPTIONS = [
	    ("Observer les ordinateurs connectés au routeur.", option1()),
	    ("Couper tous les autres ordinateurs connectés au routeur.", option2()),
	    ("Couper un ordinateur connecté au routeur.", option3()),
	    ("Récupérer les informations d'une personne connectée.", option4()),
	    ("Outil de défense.", option5())
	]

	for texte, com in OPTIONS:
	    Button(label, text=texte, command = com).pack(fill="both",padx=2, pady=2)

	fenetre.mainloop()

def option1():
	identifier()
def option2():
	print "2"
def option3():
	print "3"
def option4():
	print "4"
def option5():
	print "5"



main()