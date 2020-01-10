import socket
from threading import Timer
from time import perf_counter
from random import choice
from datetime import timedelta

class Client:
    """Client is used to send and retrieve messages from the SaltyTeemo Twitch chat."""

    def __init__(self, USER, PASS, logger=None, logs2file=False):
        TOKEN =   bytes("PASS " + PASS.strip() + "\r\n", 'utf-8')
        NICK =    bytes("NICK " + USER + "\r\n", 'utf-8')
        CHANNEL = bytes("JOIN #saltyteemo\r\n", 'utf-8')
        self.logger = logger
        self.logs2file = logs2file #TODO: Use this to determine whether to print colored output or monochrome
        self.sock = socket.socket()
        self.messages = []
        self.buffer = ""

        # Open Connection
        self.sock.connect(("irc.twitch.tv", 6667))
        self.sock.send(TOKEN); self.sock.send(NICK) # log in
        self.sock.send(CHANNEL) # Request to join Saltyteemo


        Loading = True
        while Loading:
            self.buffer += self.sock.recv(1024).decode()
            tmp = self.buffer.split("\n")
            self.buffer = tmp.pop()

            for line in tmp:
                self.logger.debug(f'(i) {line}')

                if ("End of /NAMES list" in line):
                    self.logger.info(" [+] Successfully joined channel. ".center(70,'='))
                    self.buffer = ""
                    Loading = False


    def fetchMessages(self) -> None:
        """Messages are retrieved from the server and stored inside the Client.messages attribute

        To access messages do:
        Client.messages
        """
        self.buffer += self.sock.recv(1024).decode()
        tmp = self.buffer.split("\n")
        self.buffer = tmp.pop()
        self.messages = tmp

    def sendMessage(self, msg:str) -> None:
        """Sends a message to the server"""
        envelope = ("PRIVMSG #saltyteemo :" + msg + "\r\n").encode()
        self.sock.send(envelope)
        self.logger.info(f'Sent: {msg}')

    def farm(self):
        """Dedicates a thread to automatically gather shrooms every 2 hours."""
        FARM = ("PRIVMSG #saltyteemo :!farm\r\n").encode()
        self.sock.send(FARM)
        farm_thread = Timer(3600, self.farm, [self])
        farm_thread.daemon = True; farm_thread.start()
        self.logger.info("(i) Farmed mushrooms\t\n".center(31,'\t'))

    def CheckPINGPONG(self,msg):
        """Replies to PING messages with proper PONG"""
        if (":tmi.twitch.tv" in msg) and ("PING" in msg):
            self.logger.debug("\n  [O] Ping Received\t\n".center(28,'\t'))
            self.sock.send("PONG :tmi.twitch.tv\r\n".encode())
            self.logger.debug("\n  [@] PONG Sent\t\t\n".center(25,'\t'))
    
    def display(self,msg) -> None:
        """Prints colorful messages and formats them in human readable format"""
        self.logger.debug(f'display({msg})')
        if (":tmi.twitch.tv" in msg) and ("PING" in msg):
            return None
        colors = ('36m', '32m', '90m', '94m', '96m', '92m', '95m', '91m', '97m', '93m', '35m')
        split_point = " PRIVMSG #saltyteemo :"
        username = msg.split(split_point)[0].split("!")[0].strip(":")
        text = msg.split(split_point)[1]
        self.logger.info(f"{timedelta(seconds=int(perf_counter()))} {username}: {text}")
