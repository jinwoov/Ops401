#!/usr/bin/env python3
# Script Name: Ops Challenge 12 - Network Security Tool with Scapy Part 1 of 3
# Author: Jin Kim
# Date of last revision: 10.20.2020
# Description of purpose: To analyze if the subnet is responsive to ICMP packets

#referenced doc: https://santanderglobaltech.com/en/guide-using-scapy-with-python/
# This is the main file that will be executed when the application is ran.
# Importing python library
from classes.scanner import *
from classes.icmp_scan import *
import os

# Declaring function
## Interface of this application to ask user what they want to do with this app.
def interface():
    os.system("clear")
    print("""


                          _     _           _       _ _   
                         | |   (_)         | |     (_) |  
     _ __ ___   ___   ___| |__  _ ___ _ __ | | ___  _| |_ 
    | '_ ' _ \ / _ \ / __| '_ \| / __| '_ \| |/ _ \| | __|
    | | | | | | (_) | (__| | | | \__ \ |_) | | (_) | | |_ 
    |_| |_| |_|\___/ \___|_| |_|_|___/ .__/|_|\___/|_|\__|
                                    | |                  
                                    |_|   
                                    by Jin Kim               

    Please enter what you would like to perform!!

    1) TCP Port Range Scanner
    2) TCP Port Range Scanner for specific port
    3) Scanning for ICMP ping Sweep Mode
    4) Exit

    """)
    userInput = input()
    if(userInput == "1"):
        scanner()
    elif(userInput == "2"):
        scannerPort()
    elif(userInput == "3"):
        scannerICMP()
    else:
        print("Thanks for using this application")
        exit(0)

# main
while True:
    interface()
# END