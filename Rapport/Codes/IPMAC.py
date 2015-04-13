#get my MAC address
        self.logger.info("Device is %s" % device)
        myMAC = get_if_hwaddr(device)
        if not len(myMAC) > 0:
           self.logger.error("Fatal Error: Cannot Detect my MAC address: %s" % sys.exc_info())
           exit(3)
        #get my IP address
        if not len(myIP) >0:
           self.logger.error("Fatal Error: Cannot Detect my IP address: %s" % sys.exc_info())
           exit(4)