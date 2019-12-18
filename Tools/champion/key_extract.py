# This file returns key's champion from champion.json

import json
import requests

def kchamp(key, url):
    """This function returns the desired key's champion."""
    response = requests.get(url)
    data = json.loads(response.text)["data"].items() # List champions inside data
    for champ in data:
        if (champ[1]["key"] == key):
            print(champ[0] + "\n")
            return
    print("No match. Try again.\n")
    return

if __name__ == "__main__":
    try:
        url = input("API URL: ")
        while True:
            key = input("Key: ")
            kchamp(key, url)
    except KeyboardInterrupt:
        pass





