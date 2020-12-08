#!/usr/bin/python3
# Script Name: Ops Challenge 44
# Author: Jin Kim
# Date of last revision: 12/7/2020
# Description of purpose: See if the port is open


import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 3000
sockmod.settimeout(timeout)

hostip = input("What Ip address? ")
port = input("What Port? ")

def portScanner(portno):
    if sockmod.bind((hostip, int(portno))): \
        print("Port closed")
    else:
        print("Port open")

portScanner(port)