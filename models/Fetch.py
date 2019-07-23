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
    env_variables = {"PASS":getenv("BOTPASS"), "USER":getenv("BOTNAME")}
    with open(path+name, 'r') as settings:
        json_data = json.load(settings)
        settings = SimpleNamespace(**json_data)
    if list(env_variables.values()) == [None, None]:
        print("[-] OAuth Token and Username missing in environment variables\n    using settings.json...")
        if None in (settings.USER, settings.PASS):
            raise Exception("\x1b[107m\x1b[91m[-] OAuth Token and Username missing from env variables and settings.json\n    Please make sure the OAuth Token and Username are in settings.json or env variables.")

    elif not env_variables["PASS"]:
        print("[-] OAuth Token missing in environment variables\n    using settings.json...")
        settings.USER = env_variables["USER"]
    elif not env_variables["USER"]:
        print("[-] Username missing in environment variables\n    using settings.json...")
        settings.PASS = env_variables["PASS"]
    else:
        print("[+] OAuth Token and Username found in environment variables")

    return settings
