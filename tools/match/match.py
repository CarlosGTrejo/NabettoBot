import requests
from cassiopeia import Summoner, set_riot_api_key
from datapipelines import common

# SETTINGS
set_riot_api_key("RGAPI-8fbfcebe-c4d6-4ada-ad67-790724403a7d")


class Match:
    pass

def in_game():
    """Checks if there is currently a game streaming on SaltyTeemo."""
    try:
        URL = requests.get("https://gameinfo.saltyteemo.com").url
        region, name = URL.split('/live/')[1].split('?')[0].split('/')
        current_match = Summoner(name=name, region=region.upper()).current_match()
        print(current_match.duration)
    except common.NotFoundError:
        print("Stream is currently not in game.")
        return False
    return True



if __name__ == "__main__":
    print(in_game())