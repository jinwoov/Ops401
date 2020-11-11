# Script Name: Ops Challenge 27
# Author: Jin Kim
# Date of last revision: 11/190/2020
# Description of purpose: Logging any error that was raised by recent function call part 2.

# Import library
import logging
from classes.rotating_log import *
from classes.rotating_time import *

# Declare variables
logging.basicConfig(filename="./log.log", level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')
logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
log_file= "test.log"
time_log="timed_test.log"

# Declare functions
## Interface that will collect all of the functions into a menu button.
def interface():
    print("""
    1. Rotating Log
    2. Rotating Time Log
    3. Exit
    """)
    userInput = input("What option do you want to choose? ")
    
    if (userInput == "1"):
        user_size = taking_inputs("What size do you want to save for each file? ")
        rotating_log(log_file, user_size)
    elif (userInput == "2"):
        user_time = taking_inputs("How long do you want to wait until you create a new log file? ")
        rotating_time(log_file, user_time)
    elif (userInput == "3"):
        print("Thank you !")
        exit(0)
    else:
        raise Exception("Wrong Choice! ")

## asking the message according to user's choice
def taking_inputs(stg):
    return input(stg)


# main
## try/catch block
try:
    interface()
except Exception as msg:
    logging.error(msg)
    
# END