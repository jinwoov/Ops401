import logging
import time
from logging.handlers import TimedRotatingFileHandler

## this is to track the time 
def rotating_time(filePath, time):
    logger = logging.getLogger("Rotating log")
    logger.setLevel(logging.INFO)

    # this is going to track it when the minute is over while logging. due to when="w"
    handler = TimedRotatingFileHandler(filePath,
                                        when ="m",
                                        interval=1,
                                        backupCount=5)

    logger.addHandler(handler)

    for i in range(6):
        logger.info("this is test log line")
        time.sleep(int(time))

