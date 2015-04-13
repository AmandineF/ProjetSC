def detection():
	detectionAttaque.main()
	print "Lecture du fichier de detection..."
	#On recupere les lignes du fichiers ou sont stockes les donnees de detection
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
		tkMessageBox.showinfo("Detection", "Vous etes en train de vous faire attaquer par "+MacAdress)
	else: 
		tkMessageBox.showinfo("Detection", "Vous n'etes pas attaque")

