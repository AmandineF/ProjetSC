def packet_filter (packet):
    #On filtre les donnes du paquet
    #On recupere l'adresse IP source du paquet
    source = packet.sprintf("%ARP.psrc%")
    #On recupere l'adresse IP de destination du paquet
    dest = packet.sprintf("%ARP.pdst%")
    #On recupere l'adresse Mac source du paquet
    source_mac = packet.sprintf("%ARP.hwsrc%")
    #On recupere l'operaction du paquet
    operation = packet.sprintf("%ARP.op%")
    #Si la source est l'adresse ip locale, on ajoute la destination a la liste requests
    if source == local_ip:
        requests.append(dest)
    #si c'est une operation is-at on verife si une attaque n'est pas en cours
    if operation == 'is-at':
        return check_spoof (source, source_mac, dest)

