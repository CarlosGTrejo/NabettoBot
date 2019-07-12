from time import time
from random import choice

from models.Connection import openConnection, fetchMessages, sendMessage, keepAlive
from models.Channel import joinChannel
# from models.Data import betExtract
from functions.Bet import Bet, betExtract, majorityBet
from functions.Client import messageFormat


def main():
    # Opening a new connection
    connection = openConnection()
    joinChannel(connection)

    # Necessary variables for critical functions
    alive = True # If true, the bot is alive
    start = False
    already_bet = False
    beginning_time = time() # mark a random point in time as the beginning point
    bet_data = [] # a Bet class list stores bet data collected and fetches itself to majorityBet

    # Turn on the bot, begin fetching messages for analysis
    while alive:
        messages = fetchMessages(connection)

        for message in messages:
            if ("Bet complete" in message):
                if (start == False):
                    start = True
                    temp = betExtract(connection)
                    bet_data.append(Bet(temp[0], temp[1], temp[2]))
                else:
                    temp = betExtract(connection)
                    bet_data.append(Bet(temp[0], temp[1], temp[2]))
                    
            elif ("Betting has ended" in message):
                start = False
                print("[+] Finished Betting Session.")
            
            else:
                print(messageFormat(message))

            # Send out PONG message to twitch server to keep the bot alive
            time_difference: "Delta of beginning_time and time()" = round(abs(time() - beginning_time), 3)
            if (time_difference > 300): # Send out a pong message every 300 seconds
                keepAlive(connection)
                beginning_time = time()



main()