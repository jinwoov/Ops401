#!/usr/bin/env python3

# Script Name: Ops Challenge 1
# Author: Jin Kim
# Date of last revision: 10/06/2020
# Description of purpose: To be able to send ICMP packet across all of the platform

## Importing Library
import datetime, time, platform, os
from pythonping import ping

## Variable
file = open("./pingLog.txt", "a")
operatingSys = platform.platform()

## Function
### Main interface that user will see when they first open the application
def mainInterface():
    print("""
    #======================#
    #   Ping InterWEB      #
    #    by Jin Kim        #
    #======================#
    """)

### Prompts user with what site you want to ping
def askUser():
    userOutput = input("Which IP do you want to ping? ")
    return userOutput

### Pinging the server using the user's input and running it in the infinite loop
def pingServer(answer):
    print()
    while(True):
        afterPing = ping(answer, timeout=1, verbose=False)
        print(afterPing)
        print()
        if(afterPing.success() == True):
            print(f"At {time.ctime()}, Network Active to {answer}")
            file.writelines(f"At {time.ctime()}, Network Active to {answer} \n")
        else:
            print(f"At {time.ctime()}, Network Inactive to {answer}")
            file.writelines(f"At {time.ctime()}, Network Inactive to {answer} \n")
        time.sleep(2)

## Pinging the server on Linux OS, the previous function wasn't working and this is alternative to the Linux OS
def pingLinuxServer(answer):
    while(True):
        response = os.system("ping -c 1 " + answer)
        print()
        if(response == 0):
            print(f"At {time.ctime()}, Network Active to {answer}")
            file.writelines(f"At {time.ctime()}, Network Active to {answer} \n")
        else:
            print(f"At {time.ctime()}, Network Inactive to {answer}")
            file.writelines(f"At {time.ctime()}, Network Inactive to {answer} \n")
        time.sleep(2)


## Main
mainInterface()
answer = askUser()
if(operatingSys.__contains__("Linux")):
    pingLinuxServer(answer)
else:
    pingServer(answer)

## END