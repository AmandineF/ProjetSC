MACIP = []
#On enregistre dans une liste les adresses IP et MAC des ordinateurs qui ont repondu aux requetes ARP
for send,recv in rec:
	couple = ("nom", recv.sprintf(r'%ARP.psrc%'), recv.sprintf(r'%Ether.src%'))
	MACIP.append(couple) 
