from random import choice

from nabettobot.models.Connection import settings


def messageFormat(message) -> 'random_color + "username: message"': # Currently disabled due to unidentified error
    """This function reformat messages received from connection to a more readable form."""
    if any([P in message for P in ("PING", "PONG")]):
        return "\x1b[96mPING"
    else:
        colors = ('\x1b[36m', '\x1b[32m', '\x1b[90m', '\x1b[94m', '\x1b[96m', '\x1b[92m', '\x1b[95m', '\x1b[91m', '\x1b[97m', '\x1b[93m', '\x1b[35m')
        split_point: "Point to split the message" = " PRIVMSG #" + settings.CHANNEL + " :"
        username = message.split(split_point)[0].split("!")[0].strip(":")
        message_text = message.split(split_point)[1]

        return f"{choice(colors)}{username}: {message_text}"
