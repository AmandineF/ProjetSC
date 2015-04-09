#!/usr/bin/python
# coding: utf-8

from scapy.all import *
import netifaces
import netaddr
from subprocess import Popen, PIPE
import re
import socket, struct
 
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
	print "%s--> %s" % (IP, mac)

 
if __name__ == '__main__':
	print get_default_gateway_linux()


