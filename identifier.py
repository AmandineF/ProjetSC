#!/usr/bin/python
# coding: utf-8

from scapy.all import *
def identification(rang):

	rep,non_rep = sr( IP(dst=rang) / ICMP() , timeout=0.5 )
	for elem in rep : # elem représente un couple (paquet émis, paquet reçu)
		if elem[1].type == 0 : # 0 <=> echo-reply
			print elem[1].src + ' a renvoye un echo-reply '