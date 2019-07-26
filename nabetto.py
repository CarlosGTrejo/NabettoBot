from sys import platform
from time import sleep
from traceback import format_exc

from colorama import deinit, init

if platform == "win32": from winsound import Beep

from nabettobot.__init__ import main

sequence = (293,200), (293,200), (586,400), (440,400)

try:
    init(autoreset=True)
    main()

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
