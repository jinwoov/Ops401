#!/usr/bin/env python3

# Script Name: Ops Challenge 2
# Author: Jin Kim
# Date of last revision: 10/07/2020
# Description of purpose: Sending a email to the admin if there is change in the host computer.

## Importing Library
import smtplib, time
from getpass import getpass
from pythonping import ping
from email.message import EmailMessage


# DECLARE VAIRABLE
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
msg = EmailMessage()
server.ehlo()
## opening up a log to log the event
file = open("hostComputer.txt", "a")

# DECLARE FUNCTION
## logging into the email
def loginToEmail():
    uName = input("What's your gmail username? ")
    passwords = getpass()
    try:
        server.login(uName, passwords)
        msg['From'] = uName
    except:
        print("Please Enter Correct Authentication Information")
        exit(1)

## Taking input for receiver's email?
def toWho():
    msg["Subject"] = "This is for ops-challenge 2"
    msg["To"] = input("Admin Email? ")

# Pinging the IP address
def startPing():
    pingHost = input("What is the IP address for host computer? ")
    statusHost = False
    previousStatus = False
    while(True):
        afterPing = ping(pingHost, verbose=False)
        if(afterPing.success()):
            outcome = outcomeOfPing("DOWN to UP", pingHost)
            statusHost = True
        else:
            outcome = outcomeOfPing("UP to Down")
            startPing = False
        if(previousStatus != statusHost):
            writeToText(f"{outcome}\n")
            server.send_message(msg)
            previousStatus = statusHost
        time.sleep(3)

## Taking the outcome of ping and setting/displaying it accordingly
def outcomeOfPing(stats, pingHost):
    outcome = f"{time.ctime()}, Host status changed from {stats} for {pingHost}"
    msg.set_content(outcome)
    print(outcome)
    return outcome

## Writing it to the text file
def writeToText(msg):
    file.writelines(msg)

## Main function
def main():
    loginToEmail()
    toWho()
    startPing()
    server.quit()
    file.close()

# MAIN

if __name__ == "__main__":
    main()

# END