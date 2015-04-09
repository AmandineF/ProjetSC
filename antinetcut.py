#!/usr/bin/env python
from UnixDaemon import UnixDaemon
from ManagementXMLRPC import *
from AntiNetCutClass import *
from scapy.all import *
import sys,time,os

def main(status):
    	print "status : "+status
    	#basic checking
	if os.getuid():
        	print "Operation Not Permitted. User must be root."
	service = AntiNetCut(pidfile = '/var/run/antinetcut.pid',name='antinetcut')
	if status == "start":
	    service.start()
		        
	elif 'stop' == status:
	    service.stop()
	    
	elif 'status' == status:
	    ret = service.status()
	    if ret:
		print "Antinetcut daemon is running..."
	    else:
		print "Antinetcut daemon is NOT running..."
		            
	elif 'restart' == status:
	    service.restart()
	else:
	    print "Invalid argument"

if __name__ == "__main__":
    main()
