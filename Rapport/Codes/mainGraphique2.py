#On cree le thread qui s'executera en arriere plan de notre interface puis on ajoute le thread aux tableaux des threads
tmpThread = couper.couperVictime(TabStr[1], TabStr[2], IpGw, MacGw)			
threadTab.append(tmpThread)
tmpThread.start()




