import csv
import logging
from os.path import isfile

logger = None


def createLogger(log_level: int, file: str = None) -> logging.Logger:
    """Sets up the logger and returns the logger object
    A log_level of 1 will show all messages
    If file is None then it will print the output to the console"""
    log_format = "%(levelname)s %(asctime)s - %(message)s"
    levels = {1: logging.DEBUG, 2: logging.INFO, 3: logging.WARNING, 4: logging.ERROR, 5: logging.CRITICAL}
    logging.basicConfig(filename=file,
                        level=levels[log_level],
                        format=log_format)
    return logging.getLogger()


def gather(red_team, blue_team, match_id: int, winner=None):
    """Saves the player object attributes to a csv file"""
    if type(red_team).__name__ != "Team" and type(blue_team).__name__ != "Team":
        raise TypeError("Arguments 'red_team' and 'blue_team' must be of type 'Team'")
    if not isinstance(match_id, int):
        raise TypeError(f"'match_id' must be int not {type(match_id)}")
    if match_id <= 0:
        raise ValueError("'match_id' cannot be less than or equal to 0")
    file_exists = isfile('data.csv')

    with open('data.csv', mode='a') as f:
        data_writer = csv.writer(f)
        if not file_exists:
            data_writer.writerow(['match_id', 'red', 'blue', 'winner'])
        data_writer.writerow([match_id, red_team, blue_team, winner])
