#!/usr/bin/python
# coding: utf-8

from scapy.all import *
import netaddr
import netifaces
import socket
from uuid import *

def identification():
	for interface in netifaces.interfaces():
		if(str(interface) == 'lo0' or str(interface) == 'lo'):
			pass
		else:
			try:
				adresse_ip = netifaces.ifaddresses(interface)[2][0]['addr']
				masque_sr = netifaces.ifaddresses(interface)[2][0]['netmask']
				netaddr_masque_sr = netaddr.IPAddress(masque_sr)
				netaddr_adresse_ip = netaddr.IPAddress(adresse_ip)
				netaddr_reseau_ip = netaddr_adresse_ip & netaddr_masque_sr
				netaddr_reseau = netaddr.IPNetwork(str(netaddr_reseau_ip) + '/' + str(netaddr_masque_sr))
				netaddr_plage = netaddr.IPRange(netaddr_reseau[1], netaddr_reseau[-2])
				network = str(netaddr_reseau)
				break
			except:
				network  = 'erreur'
				pass

	if(network != 'erreur'):
		#Creee et envoie des paquets ARP
		rec,unans=srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=network),timeout=10)

		MACIP = []
		#On enregistre le résultat
		for send,recv in rec:
			couple = (recv.sprintf(r'%Ether.src%'), recv.sprintf(r'%ARP.psrc%'))
			MACIP.append(couple) 
		#On affiche le résultat
		i=0
		while i < len(MACIP):
			mac, ip = MACIP[i]
			print 'MAC : ' + mac + ' <-> IP : ' + ip
			i +=1
	else:
		print 'Erreur de reconnaissance réseau'

identification()