from sys import platform
from time import sleep
from traceback import format_exc
from colorama import deinit, init
from .models import Client, Bet

if platform == "win32": from winsound import Beep
sequence = (293,200), (293,200), (586,400), (440,400)

def main():
    init(autoreset=True)
    try:
        # Variables for betting
        bet_start = False

        # Opening a new connection
        client = Client()
        client.start()
        client.farm()

        # Turn on the bot, begin fetching messages for analysis
        while True:
            client.fetchMessages()

            # Read each message
            for message in client.messages:
                client.CheckPINGPONG(message)
                if ("Bet complete" in message):
                    if (bet_start == False): # Creates timestamp for the beginning of the betting session.
                        print(" BETTING SESSION STARTED ".center(70, '='))
                        bet_start = True
                        # timer_start = time()

                    Bet.extractBet(message)
                
                elif ("Betting has ended" in message):
                    print(" BETTING SESSION ENDED ".center(70,'='))
                    Bet.resetData()

                else:
                    client.display(message)

                # if (time() - timer_start > 180 and bet_start == True):
                #     sideWithMoreMoney(bet_data)
                #     print(majorityBet(bet_data, 10000))
                #     sleep(50)
                #     bet_done = True

                # elif ("Betting has ended" in message):
                #     bet_start = False
                #     bet_done = True
                #     print("[+] Finished Betting Session.")

    except KeyboardInterrupt:
        print("\x1b[96m[.] Exitting...")

    except Exception as e:
        if platform == 'win32':
            for note in sequence: Beep(*note) # Notify the user that an exception has happened using sound notification
        else:
            print('\a',end='\r'); sleep(.7); print('\a', end='\r') # Notify the user that an exception has happened using sound notification

        print(f"\x1b[107m\x1b[91m[!] Exception: {e}\nInfo: {format_exc()}")

    finally:
        deinit()

if __name__ == "__main__":
    main()