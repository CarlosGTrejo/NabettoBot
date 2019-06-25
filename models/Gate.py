import socket
from models.Fetch import fetchSettings

settings = fetchSettings()

def openGate():
    gate = socket.socket()
    gate.connect((settings.HOST, settings.PORT))
    gate.send("PASS " + settings.PASS + "\r\n")
    gate.send("NICK " + settings.USER + "\r\n")
    gate.send("JOIN " + settings.CHANNEL + "\r\n")
    
    return gate

