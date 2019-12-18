# This file returns chosen info from champion.json

import json
import requests

def ckey(datatype, champion, url):
    """This function returns the desired champion's key."""
    response = requests.get(str(url))
    data = json.loads(response.text)["data"].items() # List champions inside data
    for champ in data:
        if ("".join(champion.split(" ")) == champ[0] ):
            print(champ[0] + ":", champ[1][datatype], "\n")
            return
    print("No match. Try again.\n")
    return

if __name__ == "__main__":
    try:
        url = input("API CALL URL: ")
        while True:
            champion = input("Champion: ")
            datatype = input("Datatype: ")
            ckey(datatype, champion, url)
    except KeyboardInterrupt:
        pass





