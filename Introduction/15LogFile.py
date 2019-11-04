import logging

logging.basicConfig(filename = "/Users/vsnaik/Downloads/test.log",
                    format = "%(asctime)s: %(levelname)s: %(message)s",
                    datefmt = "%m/%d/%Y %I:%M:%S %p")

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is a debug message")
logger.info("This is a info message")
logger.warning("This is a warning message")
logger.error("This is a error message")
logger.critical("This is a critical message")