import socket
from threading import Timer

from nabettobot.functions.Tools import debug
from nabettobot.models.Fetch import fetchSettings

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

def keepAlive(connection) -> "Thread Obj":
    """
    Keeps connection alive by sending 'PING' message to server.
    """
    PING = "PING :tmi.twitch.tv\r\n".encode()
    connection.send(PING)
    t = Timer(120, keepAlive, [connection])
    t.daemon = True; t.start()
    print("\x1b[107m\x1b[94m\n\t[*] PING Sent\t\n")

# TODO: Create reconnect function
# The reconnect function should go through the same process as connecting for the first time.
# https://dev.twitch.tv/docs/irc/guide/#re-connecting-to-twitch-irc

def fetchMessages(connection) -> "Message Stack":
    global buffer
    buffer = buffer + connection.recv(1024).decode()
    tmp = buffer.split("\n")
    buffer = tmp.pop()
    return tmp
@debug
def sendMessage(connection, msg):
    envelope = ("PRIVMSG #" + settings.CHANNEL + " :" + msg + "\r\n").encode()
    connection.send(envelope)
    print("Sent: " + msg)
