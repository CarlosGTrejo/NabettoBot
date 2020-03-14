import logging

logger = None


def createLogger(log_level: int, file: str = None) -> logging.Logger:
    """Sets up the logger and returns the logger object"""
    log_format = "%(levelname)s %(asctime)s - %(message)s"
    levels = {1: logging.DEBUG, 2: logging.INFO, 3: logging.WARNING, 4: logging.ERROR, 5: logging.CRITICAL}
    logging.basicConfig(filename=file,
                        level=levels[log_level],
                        format=log_format)
    return logging.getLogger()
