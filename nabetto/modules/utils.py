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


def build_entry(player):
    match = player.current_match()
    match_data = match.to_dict()
    entry = dict()
    entry['match_id'] = match_data['id']


def save_entry(match_id: int, participants: dict, winner=None):
    """Saves the player object attributes to a csv file"""
    if not isinstance(participants, dict):
        raise TypeError(f"Argument 'participants' must be of type 'dict' not {type(participants).__name__}")
    if not isinstance(match_id, int):
        raise TypeError(f"'match_id' must be int not {type(match_id)}")
    if match_id <= 0:
        raise ValueError("'match_id' cannot be less than or equal to 0")
    file_exists = isfile('data.csv')

    with open('data.csv', mode='a') as f:
        data_writer = csv.writer(f)
        if not file_exists:
            data_writer.writerow(['match_id', 'participants', 'winner'])
        data_writer.writerow([match_id, participants, winner])
