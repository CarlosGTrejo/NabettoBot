from models.Connection import openConnection, fetchMessages, sendMessage, keepAlive
from models.Channel import joinChannel
from models.Data import gatherData, timer
from functions.Bet import Bet, majorityBet
from functions.Client import messageFormat
from time import perf_counter, sleep, time
from sched import scheduler
from math import ceil

def main():
    # Opening a new connection
    connection = openConnection()
    joinChannel(connection)

    # Necessary variables for critical functions
    alive = True # If true, the bot is alive
    start = None
    beginning_time = time() # mark a random point in time as the beginning point

    # Turn on the bot, begin fetching messages for analysis
    while alive:
        messages = fetchMessages(connection)

        for message in messages:
            print(messageFormat(message))

            if "Bet complete" in message:
                if not start:
                    start = timer() # <- All bet timestamps are relative to the first bet timestamp.
                    print(gatherData(message,0.000))
                    
                else:
                    ts: "Timestamp" = timer(start=start)
                    print(gatherData(message,ts))
                    
            elif "Betting has ended" in messages[0]:
                print("[+] Finished Gathering Data.")
            
            else:
                print(messageFormat(message))

            # Send out PONG message to twitch server to keep the bot alive
            time_difference: "Delta of beginning_time and time()" = round(abs(time() - beginning_time), 3)
            if (time_difference > 300):
                keepAlive(connection)
                beginning_time = time()


                
main()