#!/usr/bin/env python
#Import Library
from ipaddress import IPv4Network
import sys
import socket
import random
import scapy
from scapy.all import sr1,IP,ICMP,TCP
#Declaration of variable
host = str(input("Enter your networ address with the CIDR block code: "))
addresses = IPv4Network(network)
host_count = 0
port_range = [21, 22, 23]
src_port = 22
dst_port = 22
response = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0)
###Function###
for dst_port in port_range:
    src_port = random.randint(1025,65534)
    if response is None:
        print("packet filtered")
    elif(response.haslayer(TCP)):
        if(response.getlayer(TCP).flags == 0x12): #port responding and open
            print("Port " + str(dst_port) + " is open")
        elif (response.getlayer(TCP).flag == 0x14):#port responding and closed
            print("Port " + str(dst_port) + " is closed")
        else:
            print("The port is filtered and dropped")#port is filtered and dropped silently
for host in addresses:
    if (host in (addresses.network_address, addresses.broadcast_address)):
        continue
    resp = sr1(
        IP(dst=str(host))/ICMP(),
        timeout=2,
        verbose=0,
    )
    if resp is None:
        print(f"{host} is down or not responding.")
    elif (
        int(resp.getlayer(ICMP).type)==3 and
        int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
    ):
        print(f"{host} is blocking ICMP.")
    else:
        print(f"{host} is responding.")
        host_count += 1
print(f"{host_count}/{addresses.num_addresses} hosts are online.")
#Main
#End