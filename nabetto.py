from time import time, sleep, perf_counter
from random import choice

from models.Connection import openConnection, fetchMessages, sendMessage, keepAlive
from models.Channel import joinChannel
# from models.Data import betExtract
from functions.Bet import Bet, betExtract, majorityBet, sideWithMoreMoney
from functions.Client import messageFormat, messageClear


def main():

    # Variables for betting
    current_balance = 0
    bet_start = False
    bet_done = False
    bet_data = () # a Bet class list stores bet data collected and fetches itself to majorityBet
    timer_start = 0 # marked

    # Opening a new connection
    connection = openConnection()
    joinChannel(connection)
    alive = True # If true, the bot is alive

    # Turn on the bot, begin fetching messages for analysis
    while True:
        messages = fetchMessages(connection)
        
        # Read each message 
        for message in messages:
            if ("Bet complete" in message):
                if (bet_start == False): # Creates timestamp for the beginning of the betting session.
                    print("BETTING SESSION STARTED".center(60, '='))
                    bet_start = True
                    timer_start = time()

                bet_info = betExtract(message,start=timer_start)
                # bet_data.append(Bet(*bet_info))
                bet_data += Bet(*bet_info),

            else:
                print(perf_counter(), message)

            if (time() - timer_start > 180 and bet_start == True):
                sideWithMoreMoney(bet_data)
                sendMessage(connection, majorityBet(bet_data, 10000))
                sleep(50)
                bet_done = True

            # elif ("Betting has ended" in message):
            #     bet_start = False
            #     bet_done = True
            #     print("[+] Finished Betting Session.")

            # Send out PONG message to twitch server to keep the bot alive
            if "PING" in message: # Send out a pong message every time there's a PING
                keepAlive(connection)

        # Temporary: Renew connection every hour and only do so when a betting session has not started yet
        # time_difference: "Deta of beginning_time and time()" = round(abs(connection_time - previous_connection_time), 3)
        # connection_time = time() - one_point_time 
        if(bet_done == True): # Reset main after each bet session
            messageClear()
            main()
main()