import logging
import time
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler


## rotating logs
def rotating_log(filePath, size):
    logger = logging.getLogger("Rotaing log")
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(filePath, maxBytes=int(size), backupCount=5)
    userBlah = input("what message do you want?")

    logger.addHandler(handler)
    for i in range(20):
        logger.info(f"{userBlah} %s" % i)
        time.sleep(1.5)

