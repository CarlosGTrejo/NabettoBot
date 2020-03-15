import csv
import logging
from os.path import isfile
logger = None


def createLogger(log_level: int, file: str = None) -> logging.Logger:
    """Sets up the logger and returns the logger object"""
    log_format = "%(levelname)s %(asctime)s - %(message)s"
    levels = {1: logging.DEBUG, 2: logging.INFO, 3: logging.WARNING, 4: logging.ERROR, 5: logging.CRITICAL}
    logging.basicConfig(filename=file,
                        level=levels[log_level],
                        format=log_format)
    return logging.getLogger()


def gather(red_team, blue_team):
    """Saves the player object attributes to a csv file"""
    if not isfile('data.csv'):
        with open('data.csv', mode='a'):
            header = "red_team,blue_team,winner"
    else:
        with open('data.csv', mode='a') as f:
            data_writer = csv.writer(f)
            data_writer.writerow([red_team,blue_team])
