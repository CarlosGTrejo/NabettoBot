import csv
import logging
from functools import wraps
from io import StringIO
from time import time


class CsvFormatter(logging.Formatter):
    def __init__(self):
        super().__init__()
        self.output = StringIO()
        self.writer = csv.writer(self.output)

    def format(self, record):
        self.datefmt = '%Y-%m-%d %H:%M:%S'
        self.writer.writerow((self.formatTime(record, self.datefmt),)+record.msg)

        data = self.output.getvalue()
        self.output.truncate(0)
        self.output.seek(0)
        return data.strip()

def logData(function):
    """
    Extracts team, shroom amount, and timestamp data from a bet message into bets.csv
    """
    logging.basicConfig(level=logging.DEBUG,filename="bets.csv")
    logger = logging.getLogger(__name__)
    logging.root.handlers[0].setFormatter(CsvFormatter())
    
    @wraps(function)
    def wrapper(message,start):
        output = function(message)
        logging.info(output)
        print((time()-start),output,sep='\t')
        return output
    return wrapper

def debug(function):
    """
    Displays what function ran, what arguments were passed, the output, and exceptions
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        args_list   = [repr(arg) for arg in args]
        kwargs_list = [f"{k}={v!r}" for k,v in kwargs.items()]
        signature = ", ".join(args_list + kwargs_list)           # 3
        print(f"\x1b[30m\x1b[102mCalling {function.__name__}({signature})")
        output = function(*args, **kwargs)
        print(f"\x1b[30m\x1b[102m{function.__name__!r} returned {output!r}")
        return output
    return wrapper
