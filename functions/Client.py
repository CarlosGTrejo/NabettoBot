from models.Fetch import fetchSettings


settings = fetchSettings()

def messageFormat(message):
    """This function reformat messages received from connection to a more readable form."""
    split_point: "Point to split the message" = "PRIVMSG #" + settings.CHANNEL
    username = message.split(split_point)[0].split("!")[0].strip(":")
    formatted_message = message.split(split_point)[1].split(":")[1]
    return "%s: %s" %(username, formatted_message)