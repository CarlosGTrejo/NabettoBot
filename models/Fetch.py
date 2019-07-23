"""
Retrieves variable values from settings.json and oauth key from environment variables if not present in settings.json
"""
import json
from os import getenv
from os.path import abspath, dirname
from types import SimpleNamespace

path = dirname(abspath(__file__)) + '/'

def fetchSettings(name: "Json File"= "settings.json", path: "Json file parent folder path"=path) -> "settings obj":
    """
    Gets settings from settings.json and returns a settings object that contains the setting name as an attribute.
    Accessing the value of a setting from the settings obj is as simple as:
    settings_obj.SETTING_NAME
    """
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
