#!/usr/bin/python3
# Script Name: Ops Challenge 45
# Author: Jin Kim
# Date of last revision: 12/8/2020
# Description of purpose: See what kind of the vulnerability that target has!


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
    try:
        dictionary[user_input]()
    except Exception as msg:
        print(colors.fg.red, msg, colors.reset)
        pass

dictionary = {
    "1": main_banner,
    "2": main_port,
    "3": nmap_interface,
    "4": exit
}

while True:
    interface()
