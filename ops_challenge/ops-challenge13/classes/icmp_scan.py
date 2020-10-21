#!/usr/bin/env python3

import ipaddress,time
from scapy.all import *
from .colors import *

# Decalring variable
## lists that will be displayed after running the analysis
ip_successful = list()
ip_filtered = list()
ip_down = list()

## Clearing any lists
def start_fresh():
    ip_successful.clear()
    ip_down.clear()
    ip_filtered.clear()

## Scanning the subnet by sending ICMP packet
def scannerICMP():
    start_fresh()
    networkIP = input("Which subnet do you want to scan? ")
    while (not ("/") in networkIP):
        networkIP = input("Please enter correct subnet!! ")

    ip_list = ipaddress.ip_network(networkIP)
    hosts_count = 0

    for host in ip_list.hosts():
        print(f"Pinging {colors.fg.boldwhite}{host}{colors.reset} please wait....")
        time.sleep(.2)
        response = sr1(
            IP(dst=str(host))/ICMP(),
            timeout=3,
            verbose=0
        )
        if(response == None):
            print(f"Host is down and is                         {colors.fg.red}unresponsive {colors.reset}")
            ip_down.append(str(host))
        else:
            if (response[ICMP].type == 3):
                print(f"Host is actively blocking the ICMP traffic  {colors.fg.orange}filtered{colors.reset}")
                ip_filtered.append(str(host))
            elif(response[ICMP].type == 0):
                print(f"Host is                                     {colors.fg.green}responsive{colors.reset}")
                ip_successful.append(str(host))
    print_outcome(networkIP)

## After pinging is done this function is used to print all of the outcome
def print_outcome(networkIP):
    print(f"""

    ################################
    Analysis of subnet {networkIP}
    ################################
    """)
    print(f"""
    These hosts were {colors.fg.red}down{colors.reset}:
    {colors.fg.boldwhite}{ip_down}{colors.reset}
    """)
    print(f"""
    These hosts were {colors.fg.orange}blocking{colors.reset} ICMP packet:
    {colors.fg.boldwhite}{ip_filtered}{colors.reset}
    """)
    print(f"""
    These hosts were {colors.fg.green}successfully{colors.reset} receive/send ICMP packet:
    {colors.fg.boldwhite}{ip_successful}{colors.reset}
    """)
    input("Enter any key to continue")