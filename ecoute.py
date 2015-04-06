#!/usr/bin/python
# coding: utf-8

from scapy.all import*
import regex 

listeAddresse = []

def http_header(packet):
    fichier = open("capture.txt", "w")
    http_packet=str(packet)
    if http_packet.find('GET'):
        ret = "\n".join(packet.sprintf("{Raw:%Raw.load%}\n").split(r"\r\n"))
        host = re.search('[Hh]ost: ', ret)
        if host:
            hostStg = ret.split('Host: ', 1)[1]
            #Add pour récuperer l'adresse web du serveur
            add = hostStg.split('\n', 1)[0]
            url = re.search('Referer: ', hostStg)
            if url:
                adu = hostStg.split('Referer: ', 1)[1]
                addurl = adu.split('\n', 1)[0]
                if not(("Addresse exacte : " + addurl) in listeAddresse):
                    listeAddresse.append("Addresse exacte : " + addurl)
            else: 
                if not(("Serveur : " + add) in listeAddresse):
                    listeAddresse.append("Serveur : " + add)
    for i in range(len(listeAddresse)):
        fichier.write(listeAddresse[i] + "\n")
    fichier.close()

def main():
    sniff(filter="host 192.168.0.2", prn=http_header)
    

main()