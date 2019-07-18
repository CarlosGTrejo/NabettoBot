import csv, logging
from io import StringIO

class CsvFormatter(logging.Formatter):
    def __init__(self):
        super().__init__()
        self.output = StringIO()
        self.writer = csv.writer(self.output)

    def format(self, record):
        self.datefmt = '%Y-%m-%d %H:%M:%S'
        self.writer.writerow([self.formatTime(record, self.datefmt)]+record.msg)

        data = self.output.getvalue()
        self.output.truncate(0)
        self.output.seek(0)
        return data.strip()

def LogData(function):
    """
    Extracts team, shroom amount, and timestamp data from a bet message.
    """
    logging.basicConfig(level=logging.DEBUG,filename="bets.csv")
    logger = logging.getLogger(__name__)
    logging.root.handlers[0].setFormatter(CsvFormatter())

    def wrapper(message):
        output = function(message)
        logging.info(output)
        return output
    return wrapper
