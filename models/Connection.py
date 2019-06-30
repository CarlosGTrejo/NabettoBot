import socket
from models.Fetch import fetchSettings

settings = fetchSettings()
buffer = ""

def openConnection() -> "Socket Obj":
    sock = socket.socket()
    sock.connect((settings.HOST, settings.PORT))
    CREDENTIALS = ("PASS " + settings.PASS + "\r\n"+\
                   "NICK " + settings.USER + "\r\n").encode()
                       
    CHANNEL     = ("JOIN #"+ settings.CHANNEL + "\r\n").encode()
    sock.send(CREDENTIALS)
    sock.send(CHANNEL)
    
    return sock

def sendMessage(connection, msg):
    envelope = ("PRIVMSG #" + settings.CHANNEL + " :" + msg + "\r\n").encode()
    connection.send(envelope)
    print("Sent: " + msg)

def fetchMessages(connection) -> "Message Stack":
    global buffer
    buffer = buffer + connection.recv(1024).decode()
    tmp = buffer.split("\n")
    buffer = tmp.pop()

    return tmp