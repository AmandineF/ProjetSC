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
		#os.system("python antinetcut.py start