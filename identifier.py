#!/usr/bin/python
# coding: utf-8

from scapy.all import *
import netaddr

def identification():
	#a revoir pour automatiser ??
	network = '192.168.0.0/24'

	#Crée et envoie des paquets ARP
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



identification()