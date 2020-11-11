import logging
import time
from logging.handlers import TimedRotatingFileHandler

## this is to track the time 
def rotating_time(filePath):
    logger = logging.getLogger("Rotating log")
    logger.setLevel(logging.INFO)
    timer = user_choice()
    # this is going to track it when the minute is over while logging. due to when="w"
    handler = TimedRotatingFileHandler(filePath,
                                        when =timer,
                                        interval=1,
                                        backupCount=5)

    logger.addHandler(handler)

    for i in range(6):
        logger.info("this is test log line")
        time.sleep(60)

def user_choice():
    print("""
    How often do you want to change log files?
    1. Seconds
    2. Minutes
    3. Hours
    4. Days
    """)

    userT = input()
    if(userT == "1"):
        return "s"
    elif(userT == "2"):
        return "m"
    elif(userT == "3"):
        return "h"
    else:
        return "d"