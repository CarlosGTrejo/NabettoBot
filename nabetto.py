from random import choice
from time import perf_counter, sleep, time
from traceback import format_exc
from winsound import Beep

from colorama import deinit, init

from functions.Bet import Bet, betExtract, majorityBet, sideWithMoreMoney
from functions.Client import messageClear, messageFormat
from models.Channel import joinChannel
from models.Connection import (fetchMessages, keepAlive, openConnection,
                               sendMessage)

sequence = (293,113), (293,113), (586,226), (440,226)

init(autoreset=True, convert=True)


def main():

    # Variables for betting
    bet_start = False
    bet_done = False
    bet_data = () # a Bet class list stores bet data collected and fetches itself to majorityBet
    timer_start = 0 # marked
    PONG = "PONG :tmi.twitch.tv\r\n".encode()

    # Opening a new connection
    connection = openConnection()
    joinChannel(connection)
    # keepAlive(connection)

    # Turn on the bot, begin fetching messages for analysis
    while True:
        messages = fetchMessages(connection)
        
        # Read each message     
        for message in messages:
            if (":tmi.twitch.tv" in message):
                print(f"\x1b[30m\x1b[103m\n[=] {message}\n")
                if ("PING" in message):
                    Beep(880, 135)
                    connection.send(PONG)
                    Beep(587, 135); print('\x1b[30m\x1b[106m\n\t[@] PONG Sent\t\n')
            if ("Bet complete" in message):
                if (bet_start == False): # Creates timestamp for the beginning of the betting session.
                    print("BETTING SESSION STARTED".center(60, '='))
                    bet_start = True
                    timer_start = time()

                # bet_info = betExtract(message,start=timer_start)
                # bet_data.append(Bet(*bet_info))
                # bet_data += Bet(*bet_info),

            else:
                print(f"{perf_counter():.3f}", messageFormat(message))

            # if (time() - timer_start > 180 and bet_start == True):
            #     sideWithMoreMoney(bet_data)
            #     print(majorityBet(bet_data, 10000))
            #     sleep(50)
            #     bet_done = True

            # elif ("Betting has ended" in message):
            #     bet_start = False
            #     bet_done = True
            #     print("[+] Finished Betting Session.")

            # # Send out PONG message to twitch server to keep the bot alive
            # if "PING" in message: # Send out a pong message every time there's a PING
            #     keepAlive(connection)

        # Temporary: Renew connection every hour and only do so when a betting session has not started yet
        # time_difference: "Deta of beginning_time and time()" = round(abs(connection_time - previous_connection_time), 3)
        # connection_time = time() - one_point_time 
        # if(bet_done == True): # Reset main after each bet session
        #     messageClear()

try:
    main()
except KeyboardInterrupt:
    print("\x1b[96m[.] Exitting...")
    deinit()
except Exception as e:
    for n in sequence: Beep(*n)
    print('\a',end='\r') # 3-Bell Sound Notification
    print(f"\x1b[107m\x1b[91m[!] Exception: {e}\nInfo: {format_exc()}")
