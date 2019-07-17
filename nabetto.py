from time import time, sleep, perf_counter, process_time
from random import choice

from models.Connection import openConnection, fetchMessages, sendMessage, keepAlive
from models.Channel import joinChannel
from functions.Bet import Bet, betExtract, majorityBet, minorityBet, sideWithMoreMoney
from functions.Client import messageFormat, messageClear
from ocr.ocr import currentServer

current_balance = 0

def main():

    # Variables for betting
    global current_balance 
    current_balance = 0
    bet_start = False
    bet_done = False
    bet_data = [] # a Bet class list stores bet data collected and fetches itself to majorityBet
    timer_start = 0 # marked
    # @vgfan1996 - Bet complete for BLUE, 1000.
    # Opening a new connection
    connection = openConnection()
    joinChannel(connection)
    # alive = True # If true, the bot is alive

    # Turn on the bot, begin fetching messages for analysis
    while True:
        messages = fetchMessages(connection)
        
        # Read each message 
        for message in messages:

            # Begin a betting session when "Bet complete is first detected."
            if ("Bet complete" in message):
                if (bet_start == False): 
                    print("===========BETTING SESSION STARTED===========")
                    bet_start = True
                    timer_start = time()
                    betExtracted = betExtract(message)
                    bet_data.append(Bet(betExtracted[0], betExtracted[1], betExtracted[2]))
                    print((time() - timer_start), betExtracted)
                else:
                    betExtracted = betExtract(message)
                    bet_data.append(Bet(betExtracted[0], betExtracted[1], betExtracted[2]))
                    print((time() - timer_start), betExtracted)

            # Just print messages when there is no bet session
            elif (bet_start == False): 
                print(perf_counter(), message)
                if (perf_counter() % 7200 < 5): # Collect shrooms every 2 hours
                    sendMessage(connection, "!farm")

            if (time() - timer_start > 180 and bet_start == True):
                sideWithMoreMoney(bet_data)
                sendMessage(connection, majorityBet(bet_data, 10000))
                sleep(100) # Just to make sure don't do anything until a bet session is completed
                bet_done = True

            # elif ("Betting has ended" in message):
            #     bet_start = False
            #     bet_done = True
            #     print("[+] Finished Betting Session.")

            # Send out PONG message to twitch server to keep the bot alive
            if "PING" in message: # Send out a pong message every time there's a PING
                keepAlive(connection)

        if(bet_done == True): # Reset main after each bet session to refresh connection and everything
            messageClear()
            print("===========MESSAGE CLEARED===========")
            print("Current server:", currentServer())
            sideWithMoreMoney(bet_data)
            main()

            
                
main()