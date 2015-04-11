#Creee et envoie des paquets ARP afin de detecter les IP qui repondent sur le reseau
rec,unans=srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=network),timeout=10)