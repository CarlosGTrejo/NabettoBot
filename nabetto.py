from models.Connection import openConnection, fetchMessages, sendMessage, keepAlive
from models.Channel import joinChannel
# from models.Data import gatherData, timer
from models.Bet import Bet, majorityBet
from time import perf_counter, sleep

connection = openConnection()
joinChannel(connection)
alive = True
start = None

while alive:
    messages = fetchMessages(connection)

    for line in messages:
        # if "Bet complete" in line:
        #     if not start:
        #         start = timer() # <- All bet timestamps are relative to the first bet timestamp.
        #         print(gatherData(line,0.000))
                
        #     else:
        #         ts: "Timestamp" = timer(start=start)
        #         print(gatherData(line,ts))
                
        # elif "Betting has ended" in line:
        #     print("[+] Finished Gathering Data.")
        #     alive = False
        print(line)