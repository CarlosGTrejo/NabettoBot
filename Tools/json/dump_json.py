# This file dumps json file request to local storage

import json
import requests

def jsondump(url, filename):
    try:
        response = requests.get(str(url))
        data = json.loads(response.text)
        with open(filename + ".json", "w") as outfile:
            json.dump(data, outfile)
            print("DONE...\n")
        return
    except:
        print("Something wrong...")
        return

if __name__ == "__main__":
    try:
        while True:
            url = input("JSON URL: ")
            filename = input("File's name: ")
            jsondump(url, filename)
    except KeyboardInterrupt:
        pass