#On parcourt la liste des interfaces de l'ordinateur afin de reperer laquelle est utilisee 
for interface in netifaces.interfaces():
	#On ne tien pas compte de l'interface locale (lo0 sur MACOSX et lo sur Linux)
	if(str(interface) == 'lo0' or str(interface) == 'lo'):
		pass
	else:
		try:
			#On rentre  ici si l'interface est celle utilisee
			#On recupere l'adresse IP de l'ordinateur 
			adresse_ip = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
			#On recupere le masque de sous-reseau
			masque_sr = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['netmask']
			#On effectue un bit a bit pour recuperer l'adresse du reseau
			netaddr_masque_sr = netaddr.IPAddress(masque_sr)
			netaddr_adresse_ip = netaddr.IPAddress(adresse_ip)
			netaddr_reseau_ip = netaddr_adresse_ip & netaddr_masque_sr
			#On recupere la plage d'adresses du reseau
			netaddr_reseau = netaddr.IPNetwork(str(netaddr_reseau_ip) + '/' + str(netaddr_masque_sr))
			network = str(netaddr_reseau)
			print network
			break
		except:
			#Si ce n'est pas l'interface utilisee, on passe 
			network  = 'erreur'
			pass
		