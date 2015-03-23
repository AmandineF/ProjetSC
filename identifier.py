#!/usr/bin/python
# coding: utf-8

from scapy.all import *
import netaddr

def identification():
	conf.checkIPaddr = False
	listIP = []
	network = "192.168.0.0/24"
	addresses = netaddr.IPNetwork(network)
	liveCounter = 0
	for host in addresses:
		if (host == addresses.network or host == addresses.broadcast):
			continue
		resp = sr1(IP(dst=str(host))/ICMP(),timeout=0.000001,verbose=0)
		if (str(type(resp)) == "<type 'NoneType'>"):
			print str(host) + " is down or not responding."
		elif (int(resp.getlayer(ICMP).type)==3 and int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
		    print str(host) + " is blocking ICMP."
		else:
			print str(host) + " is responding."
			#On met dans une liste les adresses IP qui répondent
			listIP.append(str(host))
			liveCounter += 1

	#On affiche les adresses IP qui répondent
	i = 0
	while i < liveCounter:
		print listIP[i]
		i+=1

identification()