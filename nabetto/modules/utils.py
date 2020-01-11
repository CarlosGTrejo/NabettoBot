import logging

def createLogger(loglvl:int, file:str=None) -> logging.Logger:
    """Sets up the logger and returns the logger object"""
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    levels = {1: logging.DEBUG, 2: logging.INFO, 3: logging.WARNING, 4: logging.ERROR, 5: logging.CRITICAL}
    logging.basicConfig(filename=file,
                        level=levels[loglvl],
                        format=LOG_FORMAT)
    return logging.getLogger()

logger = None