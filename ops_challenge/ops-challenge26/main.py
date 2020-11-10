# from classess.loggin import *
import logging
from previous_ops.main import *

# Script Name: Ops Challenge 26
# Author: Jin Kim
# Date of last revision: 11/9/2020
# Description of purpose: Logging any error that was raised by recent function call.

## Declare Variables
# root = logging.getLogger()
logging.basicConfig(filename="./error.log", level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')
logging.basicConfig(filename="./info.log", level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

## Logging functions are in the /classess/loggin.py


## Main
try:
    interface()
    logging.info("Info information")
except Exception as msg:
    logging.ERROR(msg)
    exit(1)