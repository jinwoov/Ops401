#!/usr/bin/env python3
# Script Name: Ops Challenge 11 - Network Security Tool with Scapy Part 1 of 3
# Author: Jin Kim
# Date of last revision: 10/19/2020
# Description of purpose: Encrypt and decrypt the folder recursively.

#referenced doc: https://santanderglobaltech.com/en/guide-using-scapy-with-python/
# This is the main file that will be executed when the application is ran.
# Importing python library
from classes.scanner import *

# Declaring function
def interface():
    print("""


                          _     _           _       _ _   
                         | |   (_)         | |     (_) |  
     _ __ ___   ___   ___| |__  _ ___ _ __ | | ___  _| |_ 
    | '_ ' _ \ / _ \ / __| '_ \| / __| '_ \| |/ _ \| | __|
    | | | | | | (_) | (__| | | | \__ \ |_) | | (_) | | |_ 
    |_| |_| |_|\___/ \___|_| |_|_|___/ .__/|_|\___/|_|\__|
                                    | |                  
                                    |_|                  

    Please enter what you would like to perform!!

    1) Scanning for vulnerability
    2) Exit

    """)
    userInput = input()
    if(userInput == "1"):
        scanner()
    else:
        print("Thanks for using this application")
        exit(0)

# main
while True:
    interface()
# END