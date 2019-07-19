from colorama import init, Fore, Back # Adds colors to the chat experience
from random import choice
from os import system
from traceback import format_exc

from models.Fetch import fetchSettings

def messageFormat(message): # Currently disabled due to unidentified error
    """This function reformat messages received from connection to a more readable form."""
    try:
        # colors = ['\x1b[34m', '\x1b[36m', '\x1b[32m', '\x1b[90m', '\x1b[94m', '\x1b[96m', '\x1b[95m', '\x1b[91m', '\x1b[97m', '\x1b[93m', '\x1b[35m'] # Some colors that will be randomly selected for chat display
        colors = [color for color in dir(Fore)[2:13]] # Colors that will be used: ['CYAN', 'GREEN', 'LIGHTBLACK_EX', 'LIGHTBLUE_EX', 'LIGHTCYAN_EX', 'LIGHTGREEN_EX', 'LIGHTMAGENTA_EX', 'LIGHTRED_EX', 'LIGHTWHITE_EX', 'LIGHTYELLOW_EX', 'MAGENTA']

        init(convert=True, autoreset=True) # To make coloring works with CMD
        split_point: "Point to split the message" = " PRIVMSG #" + fetchSettings().CHANNEL + " :"
        
        username = message.split(split_point)[0].split("!")[0].strip(":")
        formatted_message = message.split(split_point)[1]
    
        return choice(colors) + "%s: %s" %(username, formatted_message)

    except Exception as e:
        return Back.LIGHTWHITE_EX + Fore.LIGHTRED_EX + "Exception triggered! Message: {msg}\nException: {error}\nInfo: {info}".format(msg=message, error=e, info=format_exc())

def messageClear():
    system( "cls" )