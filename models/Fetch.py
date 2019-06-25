"""
Retrieves variable values from settings.json and oauth key from environment variables if not present in settings.json
"""
import json
from types import SimpleNamespace
from os import getenv
from os.path import dirname,abspath

path = dirname(abspath(__file__)) + '\\'

def fetchSettings(name: "Json File"= "settings.json", path: "Json file parent folder path"=path) -> "attribute-based namespace obj":
    settings: dict() = {}
    with open(path+name, 'r') as settings:
        json_data = json.load(settings)
        settings = SimpleNamespace(**json_data)
    
    if not settings.PASS:
        print("[-] OAuth Token not present in settings.json, checking environment variables...")
        settings.PASS = getenv("BOTPASS")
        # checking env vars for password token
        assert getenv("BOTPASS"), "[-] No OAuth Token found, please visit https://twitchapps.com/tmi/ for a new token."
        print("[+] OAuth Token Found.")

    
    return settings
