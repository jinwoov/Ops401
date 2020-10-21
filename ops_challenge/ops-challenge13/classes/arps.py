import scapy.all as s
from .scanner import *

## Class to contain all of the arp properties and methods.
class Arps:
        
    def __init__(self):
        self.subnet = self.askWhatGateWay()
        self.list_IP = list()

    def arpy(self):
        arp = s.ARP(pdst=self.subnet)
        bcast = "ff:ff:ff:ff:ff:ff"
        broadcast = s.Ether(dst=bcast)


        request_broadcast = broadcast / arp
        clients = s.srp(request_broadcast, timeout =3)[0]
        for element in clients:
            self.list_IP.append(element[1].psrc)
            print(element[1].psrc + "       " + element[1].hwsrc)
        input("Please enter any key to scan for available IP")
        self.checkPorts(self.list_IP)
        input("Please enter any key to continue")
        

    def checkPorts(self, ip_adds):
        dst_port = [21, 22, 80, 443]
        for ip in ip_adds:
            testing_vulnerability(str(ip), dst_port)
        

    def askWhatGateWay(self):
        return input("what subnet do you want to ARP? ")