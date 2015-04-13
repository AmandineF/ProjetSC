self.logger.info("Protection Thread Started..")
        while not self.shouldTerminate:
            while self.shouldRun:
                self.logger.debug("Run Now")
                sendp(p1, verbose=0)
                sendp(p2,verbose=0)
                self.logger.debug("Sending Correction Packet")
                time.sleep(0.7)
            self.logger.debug("Waiting...")
            self.waitLoop()