def check_spoof (source, mac, destination): 
    #Si la source du paquet n'est pas dans la liste requests et n'est pas l'adresse IP locale
    if not source in requests and source != local_ip:
        #Il y a surement une attaque, on enregistre l'adresse mac dans le fichier
        fichier = open("detection.txt", "w")
        fichier.write(mac)
        fichier.write("\n")
    else:
        #si la source etait dans requests on la supprime de la liste, pour repartir de zero
        if source in requests:
            requests.remove(source)

