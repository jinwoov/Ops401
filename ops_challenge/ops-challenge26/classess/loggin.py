import logging,os

class OneLineExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        return super().formatException(exc_info)

    def format(self, record):
        result = super().format(record)
        if record.exc_text:
            result = result.replace("\n", "")
        return result


# root = logging.getLogger()
# logging.basicConfig(filename="./error.log", level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')
# logging.debug("Debug Information")
# logging.warning("Warning information")
# logging.error("Error information")
# logging.critical("Critical information")
# formatter = OneLineExceptionFormatter(logging.BASIC_FORMAT)
# fh = logging.FileHandler("./error.log")
# fh.setLevel(os.environ.get("LOGLEVEL", "INFO"))
# fh.setFormatter(formatter)
# root.addHandler(fh)

