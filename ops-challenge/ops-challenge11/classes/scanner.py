import sys,time
from scapy.all import ICMP, IP, sr1, TCP
from .randoms import *

# Using the scanner to find any vulnerable ports
def scanner():
    try:
        host = ask_host()
        port_range = 22
        dst_port = [21, 22, 80, 443]
        testing_vulnerability(host, dst_port)
    except:
        print("please run this in sudo mode!!")
        exit(1)

# Scanning for any vulnerability (Reused)
def testing_vulnerability(host, destPort):
    for po in destPort:
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
        time.sleep(1.5)
    input("Enter any key to continue")

## Promting user if they want to continue to put more ports
def userPrompt():
    output = input("Anymore port? (y/n) ")
    if(output.lower() == "y"):
        return True
    else:
        return False

## Scanning to see which port they want to scan
def scannerPort():
    try:
        host = ask_host()
        dst_port = []
        dst_port.append(int(input("What port do you want to scan? ")))
        currentOutput = userPrompt()

        while(currentOutput == True):
            dst_port.append(int(input("What port do you want to scan? ")))
            currentOutput = userPrompt()
        
        testing_vulnerability(host, dst_port)
    except:
        print("You typed wrong input!!")
        exit()

## Function to check what site/IP address that user wants to scan!
def ask_host():
    host = input("what ip do you want to scan? (default will be scanme.nmap.org)")
    if(host == None or host == ""):
        host = "scanme.nmap.org"
    return host