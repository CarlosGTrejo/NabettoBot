# This file collects player data based on specific needs

import json
import requests




# TEMPORARY DESIGN FOR PLAYER CLASS

class Player:
    def __init__(self, name = "", level = 0, rank = 0, wr = 0, main = ""):
        self.name = name
        self.level = level
        self.rank = rank
        self.wr = wr
        self.main = main


class PlayerData:

    
        

# TEMPORARY SOLUTION FOR RECEIVE API ANSWER

def get_matches(api_res, ngames):
    """Return specified number of matches from the"""
    return json.loads(api_res.text)["matches"]


# GET WINRATE OF THE LAST 20 GAMES

# def get_winrate(api_res, ngames):
#     matches = json.loads(api_res.text)["matches"]
#     for match in matches:
#         print(match["gameId"], "\n")

def winner(matchid, playername):
    """This function returns true of a specific player win a specific match, else it returns false"""
    pass






# FOR TROUBLESHOOTING
if __name__ == "__main__":
    pass




