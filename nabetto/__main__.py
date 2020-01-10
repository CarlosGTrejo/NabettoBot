from .modules import Client, createLogger
from .args import ARGS
from traceback import format_exc
import pkg_resources

def main():
    try:
        SHOW_MSGS = ARGS.verbose
        USER = ARGS.user
        PASS = ARGS.passwd
        DBUG_LVL = ARGS.loglvl
        LOG_FILE = ARGS.logpath
        APIKEY = ARGS.key

        #TODO: Use ARGS.__dict__ and iterate over the args, passing it to the modules that need them.

        bet_session_open = False

        logger = createLogger(DBUG_LVL, file=LOG_FILE)
        logs2file = True if LOG_FILE else False # Is Nabetto logging output to a file or the console?
        # if not logs2file: init(autoreset=True) # Only show colored text when it outputs to the console
        
        # Client Init
        client = Client(USER, PASS, logger=logger, logs2file=logs2file)

        while True:
            client.fetchMessages()

            for message in client.messages:
                client.CheckPINGPONG(message)

                # Check for bet messages
                if ("Bet complete" in message):
                    if not bet_session_open:
                        bet_session_open = True
                        logger.info(" BETTING SESSION STARTED ".center(70, "="))
                
                elif ("betting has ended" in message):
                    bet_session_open = False
                    logger.info(" BETTING SESSION ENDED ".center(70, '='))
                
                else:
                    if SHOW_MSGS: client.display(message)

    except KeyboardInterrupt:
        output = "[X] Exitting..."
        logger.info(output)
        
    except Exception as e:
        exception_message = f"[!] Exception: {e}\nInfo: {format_exc()}"
        logger.error(exception_message)
    
    # finally:
    #     print('\x1b[0m)
    #     deinit()

if __name__ == "__main__":
    main()