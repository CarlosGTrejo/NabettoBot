from .functions.Tools import logBet
import socket, configparser
from os.path import abspath, dirname
from os import getenv
from threading import Timer
from time import perf_counter
from random import choice
from datetime import timedelta

class Settings:
    """Retrieves these settings from settings.ini:
    BOTNAME
    BOTPASS
    CHANNEL
    """
    path = dirname(abspath(__file__)) + '\\'
    @classmethod
    def __init__(cls):
        parser = configparser.ConfigParser()
        parser.read(f'{cls.path}settings.ini')              # Get settings file
        settings_ini = parser['Settings']
        for option, val in settings_ini.items(): # Load settings
            setattr(cls, option.upper(), val if val else getenv(option.upper()))
                                                 # Check settings
        for option in ("BOTNAME", "BOTPASS", "CHANNEL"):
            if not getattr(cls, option.upper()):
                print(f"[-] You need to specify a value for {option}")
                print('-'*70)
                input("Press Enter to exit"); exit()


class Bet:
    """The class stores all basic information collected from each betting session."""

    Settings()

    __static_data__: "Holds the total bet amount for each team" = {"blue":0, "red":0}

    def __init__(self, user, team, bet_amount): # Constructor
        self.user: "Person that placed the bet" = user
        self.team: "Team the person bet on" = team
        self.bet_amount: "Amount person bet" = int(bet_amount)

        self.__static_data__[self.team] += self.bet_amount # Adding bet amount to the appropriate team.

    @staticmethod
    def resetData() -> None:
        """Resets the data variable to {blue:0, red:0} for the next betting session"""
        Bet.__static_data__.update(blue=0, red=0) # Resetting the data variable.

    @classmethod
    def extractBet(cls,message: "A betting request message") -> "Bet Object":
        """Extracts bet data from a message and updates the __static_data__ variable based on the chosen team"""
        split_point: "Where the message is split" = "PRIVMSG #" + Settings.CHANNEL + " :"
        # Extract username
        username = message.split(split_point)[1].split("@")[1].split(" - ")[0]
        # Extract team
        team = "BLUE" if "blue" in message else "RED"
        # Extract amount
        amount = int(message.split('-').pop().split('.').pop(0).split(', ')[1])
        bet_info = (username, team, amount)
        # TODO:
        logBet(bet_info)

        return cls(*bet_info)

    @staticmethod
    def betWithMajority(current_amount: "The current amount of money you hold") -> "!(team) str(current_amount * 0.1)":
        """Returns a bet command based on the team that holds the highest bet"""
        return f"!{max(Bet.__static_data__, key=Bet.__static_data__.get)} {int(current_amount * 0.1)}"



class Client:
    """Client is used to send and retrieve messages"""
    Settings()
    PONG = "PONG :tmi.twitch.tv\r\n".encode()
    def __init__(self):
        self.sock = socket.socket()
        self.buffer = ""
        self.messages = []
    
    def start(self): # Open Connection and start loading
        """Starts the client by opening the connection to irc.twitch.tv:6667
        and retrieves the /NAMES list"""
        buffer = ""
        # Opening connection
        self.sock.connect(("irc.twitch.tv", 6667))
        CREDENTIALS = ("PASS " + Settings.BOTPASS + "\r\n" \
                      +"NICK " + Settings.BOTNAME + "\r\n").encode()
        CHANNEL     = ("JOIN #"+ Settings.CHANNEL + "\r\n").encode()
        self.sock.send(CREDENTIALS); self.sock.send(CHANNEL)

        Loading = True
        while Loading:
            buffer = buffer + self.sock.recv(1024).decode()
            tmp = buffer.split("\n")
            buffer = tmp.pop()

            for line in tmp:
                print('(i)',line)

                if ("End of /NAMES list" in line):
                    print('-'*70,"\n[+] Successfully joined channel.\n")
                    Loading = False
    
    def fetchMessages(self) -> "Client.messages":
        """Messages are retrieved from the server and placed into a "messages" instance variable"""
        self.buffer += self.sock.recv(1024).decode()
        tmp = self.buffer.split("\n")
        self.buffer = tmp.pop()
        self.messages = tmp

    def sendMessage(self, msg:str) -> "Prints: Sent: {msg}":
        """Sends a message to the server"""
        envelope = ("PRIVMSG #" + Settings.CHANNEL + " :" + msg + "\r\n").encode()
        self.sock.send(envelope)
        print("Sent: " + msg)
    
    def farm(self):
        """Dedicates a thread to automatically gather shrooms every 2 hours."""
        self.sock.send("!farm".encode())
        farm_thread = Timer(3600, self.farm, [self])
        print('\x1b[97m\x1b[104m'+"\n  (i) Farmed mushrooms\t\n".center(31,'\t'))

    def CheckPINGPONG(self,msg):
        """Replies to PING messages with proper PONG"""
        if (":tmi.twitch.tv" in msg) and ("PING" in msg):
            print("\x1b[30m\x1b[103m"+"\n  [O] Ping Received\t\n".center(28,'\t'))
            self.sock.send(self.PONG)
            print("\x1b[30m\x1b[106m"+"\n  [@] PONG Sent\t\t\n".center(25,'\t'))
    
    @staticmethod
    def display(msg):
        """displays colorful messages"""
        if (":tmi.twitch.tv" in msg) and ("PING" in msg):
            return None
        colors = ('36m', '32m', '90m', '94m', '96m', '92m', '95m', '91m', '97m', '93m', '35m')
        split_point = " PRIVMSG #" + Settings.CHANNEL + " :"
        username = msg.split(split_point)[0].split("!")[0].strip(":")
        text = msg.split(split_point)[1]
        print(timedelta(seconds=int(perf_counter())),\
            f"\x1b[{choice(colors)}{username}: {text}")