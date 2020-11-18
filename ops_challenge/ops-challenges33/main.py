# Script Name: Ops Challenge 32
# Author: Jin Kim
# Date of last revision: 11/18/2020
# Description of purpose: Finding the file using user input part 3/3


# importing library
import sys
from time import sleep
from classes.search import *
from classes.hashes import *
from classes.virustotal import *

## Declare functions
def interface():
    print("""
    1. Find a file
    2. Get MD5 hash codes
    3. Scan on Virus Total
    4. Exit
    """)
    user_choice = input("Whats your choice? ")
    if(user_choice == "1"):
        search_file()
    elif (user_choice == "2"):
        get_hashcode()
    elif (user_choice == "3"):
        query_virusTotal()
    else:
        print("Exiting...")
        sleep(1)
        exit(0)

## Main
def main():
    interface()

if __name__ == "__main__":
    while(True):
        main()
## END