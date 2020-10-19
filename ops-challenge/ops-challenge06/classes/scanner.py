import sys
from scapy.all import ICMP, IP, sr1, TCP
from .randoms import *

# Using the scanner to find any vulnerable ports
def scanner():
    try:
        host = input("what ip do you want to scan? (default will be scanme.nmap.org)")
        if(host == None or host == ""):
            host = "scanme.nmap.org"
        port_range = 22
        dst_port = [21, 22, 80, 443]
        for po in dst_port:
            src_port = randomize()
            response = sr1(IP(dst=host)/TCP(sport=src_port,dport=po,flags="S"),timeout=1,verbose=0)
            print(f"The source port was from {src_port} to {host}:{po}")
            if(str(type(response)) == "<class 'NoneType'>"):
                print("Port is filtered and is silently dropped")
            elif(str(response).__contains__("x14")):
                print("Port is closed")
            elif(str(response).__contains__("x12")):
                print("Port is open ")
                pass
            input("Enter any key to continue")
    except:
        print("please run this in sudo mode!!")
        exit(1)
