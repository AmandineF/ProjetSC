#!/usr/bin/python
# coding: utf-8

def main():
	boucle = False
	print "Options disponibles : \n"
	print "0 - Quitter le programme.\n"
	print "1 - Observer les ordinateurs connectés au routeur.\n"
	print "2 - Couper tous les autres ordinateurs connectés au routeur.\n"
	print "3 - Couper un ordinateur connecté au routeur.\n"
	print "4 - Récupérer les informations d'une personne connectée.\n"
	print "5 - Outil de défense.\n"
	while not(boucle):
		choix = int(raw_input("Que voulez-vous faire ? "))
		if choix == 0:
			boucle = True
			option0()
		elif choix == 1:
			boucle = True
			option1()
		elif choix == 2:
			boucle = True
			option2()
		elif choix == 3:
			boucle = True
			option3()
		elif choix == 4:
			boucle = True
			option4() 
		elif choix == 5:
			boucle = True
			option5()
		else: 
			print "Veuillez rentrer une valeur entière comprise entre 0 et 5. \n"

def option0():
	exit()
def option1():
	print "1"
def option2():
	print "2"
def option3():
	print "3"
def option4():
	print "4"
def option5():
	print "5"

main()