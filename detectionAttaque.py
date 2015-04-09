#!/usr/bin/env python
import os, time, netifaces, sys, logging
from sys import platform
from scapy.all import sniff

fichier = open("detection.txt", "w")

#On parcourt la liste des interfaces de l'ordinateur
#afin de reperer laquelle est utilisee
for interface in netifaces.interfaces():
    #On ne tien pas compte de l'interface locale
    #lo0 sur MACOSX et lo sur Linux
    if(str(interface) == 'lo0' or str(interface) == 'lo'):
        pass
    else:
        try:
            #On recupere l'adresse IP de l'ordinateur
            local_ip = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]["addr"]
            break
        except:
            network  = 'erreur'
            pass

requests = []

def check_spoof (source, mac, destination): 
    #Si la source du paquet n'est pas dans la liste requests et n'est pas l'adresse IP locale
    if not source in requests and source != local_ip:
        #Il y a surement une attaque, on enregistre l'adresse mac dans le fichier
        fichier.write(mac)
        fichier.write("\n")
    else:
        #si la source etait dans requests on la supprime de la liste, pour repartir de zero
        if source in requests:
            requests.remove(source)

def packet_filter (packet):
    #On filtre les donnes du paquet
    #On recupere l'adresse IP source du paquet
    source = packet.sprintf("%ARP.psrc%")
    #On recupere l'adresse IP de destination du paquet
    dest = packet.sprintf("%ARP.pdst%")
    #On recupere l'adresse Mac source du paquet
    source_mac = packet.sprintf("%ARP.hwsrc%")
    #On recupere l'operaction du paquet
    operation = packet.sprintf("%ARP.op%")
    #Si la source est l'adresse ip locale, on ajoute la destination a la liste requests
    if source == local_ip:
        requests.append(dest)
    #si c'est une operation is-at on verife si une attaque n'est pas en cours
    if operation == 'is-at':
        return check_spoof (source, source_mac, dest)

def main():
	print("Detection ARP Spoofing..")
	sniff(filter = "arp", prn = packet_filter, store = 0, count=10)


