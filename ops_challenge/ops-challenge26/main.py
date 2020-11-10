from classess.loggin import *
from previous_ops.main import *

# Script Name: Ops Challenge 26
# Author: Jin Kim
# Date of last revision: 11/9/2020
# Description of purpose: Logging any error that was raised by recent function call.



## Logging functions are in the /classess/loggin.py


## Main
try:
    interface()
except Exception as msg:
    logging.exception(msg)
    exit(1)