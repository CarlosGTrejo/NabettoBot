from colorama import init, Fore # Adds colors to the chat experience
from random import choice

from models.Fetch import fetchSettings


def messageFormat(message):
    """This function reformat messages received from connection to a more readable form."""
    colors = ['\x1b[34m', '\x1b[36m', '\x1b[32m', '\x1b[90m', '\x1b[94m', '\x1b[96m', '\x1b[95m', '\x1b[91m', '\x1b[97m', '\x1b[93m', '\x1b[35m'] # Some colors that will be randomly selected for chat display
    init(convert=True) # To make coloring works with CMD
   
    try:
        split_point: "Point to split the message" = "PRIVMSG #" + fetchSettings().CHANNEL + " :"
        username = message.split(split_point)[0].split("!")[0].strip(":")
        formatted_message = message.split(split_point)[1]
        return choice(colors) + "%s: %s" %(username, formatted_message)
    except: # Just in case the message is not in a conventional format
        return "Exception triggered:", message