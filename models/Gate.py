import socket
from models.Fetch import fetchSettings

settings = fetchSettings()

def openGate() -> "Socket Obj":
    gate = socket.socket()
    gate.connect((settings.HOST, settings.PORT))
    CREDENTIALS = ("PASS " + settings.PASS + "\r\n"+\
                   "NICK " + settings.USER + "\r\n").encode()
                       
    CHANNEL     = ("JOIN " + settings.CHANNEL + "\r\n").encode()
    gate.send(CREDENTIALS)
    gate.send(CHANNEL)
    
    return gate

def sendMessage(gate, msg):
    envelope = ("PRIVMSG #" + settings.CHANNEL + " :" + msg + "\r\n").encode()
    gate.send(envelope)
    print("Sent: " + msg)