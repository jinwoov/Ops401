# Script Name: Ops Challenge 37
# Author: Jin Kim
# Date of last revision: 11/24/2020
# Description of purpose: Web application vulnerability check 2/3

## Library
from classes.banner_grab import *
from classes.cookies import *
from time import sleep

## Declare Function
def interface():
    try:
        bringforthcookiemonster()
        print("""
        1) Banner Grabbing
        2) Cookie Capture
        3) XSS Vulnerability Detection
        4) Exit
        """)
        user_answer = input("Whats your choice... ")

        if (user_answer == "1"):
            banner_grabbing()
        elif (user_answer == "2"):
            get_html()
        elif (user_answer == "3"):
            xss_detection()
        else:
            print("exiting.... ")
            sleep(1.5)
            exit(0)
    except Exception as msg:
        print(msg)
        exit(1)

## Main
if __name__ == "__main__":
    interface()
## End