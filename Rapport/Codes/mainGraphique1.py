#On recupere les informations telles que l'IP et l'@ mac de la victime dans la selection (TabStr[1] : IPVictim ; TabStr[2] : MacVictim)
for i in selectList:
	string = listeOrdi.get(i)
TabStr = string.split()
#On lance le thread permettant l'attaque
tmpThread = attaque.sniffer(TabStr[1], TabStr[2], IpGw, MacGw)
threadSniff.append(tmpThread)
tmpThread.start()
#On lance le thread permettant l'ecoute
tmpThread2 = ecoute.sniffer(TabStr[1])
threadSniff.append(tmpThread2)
tmpThread2.start()

