from .modules import Client, createLogger
from .modules import utils
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
        if ARGS.save_creds: utils.save_settings()
        
        bet_session_open = False

        # === Initialize logger ===
        utils.logger = createLogger(DBUG_LVL, file=LOG_FILE)
        
        # Client Init
        client = Client(USER, PASS)

        while True:
            client.fetchMessages()

            for message in client.messages:
                client.CheckPINGPONG(message)

                # Check for bet messages
                if ("Bet complete" in message):
                    if not bet_session_open:
                        bet_session_open = True
                        utils.logger.info(" BETTING SESSION STARTED ".center(70, "="))
                
                elif ("betting has ended" in message):
                    bet_session_open = False
                    utils.logger.info(" BETTING SESSION ENDED ".center(70, '='))
                
                else:
                    if SHOW_MSGS: client.display(message)

    except KeyboardInterrupt:
        output = "[X] Exitting..."
        utils.logger.info(output)
        
    except Exception as e:
        exception_message = f"[!] Exception: {e}\nInfo: {format_exc()}"
        utils.logger.error(exception_message)
    
    # finally:
    #     print('\x1b[0m)
    #     deinit()

if __name__ == "__main__":
    main()