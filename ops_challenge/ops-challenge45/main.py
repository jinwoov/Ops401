#!/usr/bin/python3
# Script Name: Ops Challenge 44
# Author: Jin Kim
# Date of last revision: 12/7/2020
# Description of purpose: See if the port is open


from classes.port_scanner import *
from classes.banner_grab import *
from classes.nmap_scan import *



def interface():
    print("""
    
    1) Banner Grabber
    2) Port Scanner 
    3) NMAP Scanner
    4) Exit
    
    """)
    
    user_input = input("Choice?..... ")

    dictionary[user_input]()

dictionary = {
    "1": main_banner,
    "2": main_port,
    "3": nmap_interface,
    "4": exit
}

while True:
    interface()
