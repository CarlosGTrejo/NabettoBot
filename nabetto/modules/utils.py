import logging, json
from re import compile
rKey = compile(r'^RGAPI-([A-z]|[\d]){8}-(([A-z]|[\d]){4}-){3}([A-z]|[\d]){14}')
logger = None

def createLogger(loglvl:int, file:str=None) -> logging.Logger:
    """Sets up the logger and returns the logger object"""
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    levels = {1: logging.DEBUG, 2: logging.INFO, 3: logging.WARNING, 4: logging.ERROR, 5: logging.CRITICAL}
    logging.basicConfig(filename=file,
                        level=levels[loglvl],
                        format=LOG_FORMAT)
    return logging.getLogger()

def load_settings() -> dict:
    """Returns the settings that were stored in the _.json file"""
    with open('_.json', 'r') as settings:
        return json.load(settings)

def save_settings(d: dict) -> bool:
    """Saves a dictionary (d) object with the settings
    configurations into the _.json file.
    Returns True if saved successfully, else False
    
    >>> settings = {
    ...     "api_key": "RGAPI-aaabbb11-ccc3-44dd-ee55-ff66ff77ff88ff",
    ...     "print_calls": False,
    ...     "print_key": False
    ...     }
    >>>
    >>> save_settings(settings)"""

    # TODO: Get rid of this garbage, the verification of the key will be done in the ARGS module
    # Verify Structure
    if set(settings.keys()) == {'print_calls', 'print_key', 'api_key'}:
        tests = (
            type(settings['api_key']) is str,
            type(settings['print_calls']) is bool,
            type(settings['print_key']) is bool
        )
        if all(tests):
            # Now check if the key is the structure: RGAPI-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxxx
            if rKey.fullmatch(settings['api_key']):
                # TODO: Finish the saving feature
                with open('.\\_.json', 'w'):
                    settings = {}
    
    return False
