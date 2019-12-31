# This file collects player data based on specific needs

from cassiopeia import *
from time import sleep

apply_settings(r".\\cass_settings.json")
set_riot_api_key("RGAPI-970e1256-dfb6-4ea7-bb9d-8c1bf478b1a0") 

RANK_TO_NUMBER = dict(
    Unranked = 0,
    IronIV = 1,
    IronIII = 2,
    IronII = 3,
    IronI = 4,
    BronzeIV = 5,
    BronzeIII = 6,
    BronzeII = 7,
    BronzeI = 8,
    SilverIV = 9,
    SilverIII = 10,
    SilverII = 11,
    SilverI = 12,
    GoldIV = 13
)

# TEMPORARY DESIGN FOR PLAYER CLASS
class Player:

    def __init__(self, name, region, champion, **kwargs): # kwrags is used so that users don't have to remember the order
        """Stores player data. If one or more fields is not filled out, 
        the constructor automatically sets default value(s) accordingly.
        _name is a mandatory """
        self._name = name
        self._region = region
        self._champion = champion
        self._level = kwargs['level'] if 'level' in kwargs else 0
        self._rank = kwargs['rank'] if 'rank' in kwargs else 0
        self._rank_wr = kwargs['rank_wr'] if 'rank_wr' in kwargs else 0
        self._champ_wr = kwargs['champ_wr'] if 'champ_wr' in kwargs else 0
        self._champ_mastery = kwargs['champ_mastery'] if 'champ_mastery' in kwargs else 0

    def level(self):
        """Returns the level of a player. 
        False if that player does not exist."""
        try:
            self._level = Summoner(name=self._name, region=self._region).level
        except:
            print("Unexpected error. The default value is set to {}".format(self._level))
        return self._level
    
    def rank(self):
        """Returns the SoloQ rank of a player."""
        try:
            self._rank = RANK_TO_NUMBER[str(Summoner(name=name, region=region).ranks[Queue.ranked_solo_fives]).replace(" ", "").replace("<", "").replace(">", "")]
        except:
            print("Unexpected error. The default value is set to {}".format(self._rank))
        return self._rank

    def rank_wr(self):
        """Returns the SoloQ rank win rate of a player. 
        -1 if that player does not exist.
        -2 if there is no SoloQ info."""
        try:
            summoner_soloq_entries = Summoner(name=name, region=region).league_entries[Queue.ranked_solo_fives]
            wins = summoner_soloq_entries.wins
            losses = summoner_soloq_entries.losses
            self._rank_wr = round((wins/(wins + losses) * 100), 1)
        except ZeroDivisionError:
            print("This person has not played any ranked SoloQ game yet. The default value is set to {}%".format(self._rank_wr))
        except:
            print("Unexpected error. The default value is set to {}%".format(self._rank_wr))

    def champ_wr(self):
        """Returns player's win rate on a specific champ on SoloQ. 
        -1 if that player does not exist.
        -2 if there is no SoloQ info for the specific champion."""
        try:
            summoner = Summoner(name=name, region=region)
            season = Season.season_9
            queue = Queue.ranked_solo_fives
            matches = summoner.match_history(seasons={season}, queues={queue}, champions={champion})
            wins, losses = 0, 0
            for match in matches:
                if match.participants[summoner].stats.win:
                    wins += 1
                else:
                    losses += 1
            self._rank_wr = round((wins/(wins + losses) * 100), 1)
        except ZeroDivisionError:
            print("This has not played any ranked SoloQ game with {}. The default value is set to {}%".format(self._champion, self._rank_wr))
        except:
            print("Unexpected error. The default value is set to {}%".format(self._champ_wr))
        return self._rank_wr

    def champ_mastery(self):
        """Returns player's mastery on a specific champ. 
        -1 if that player does not exist."""
        try:
            self._champ_mastery = get_champion_mastery(champion=Champion(name=self._champion , region=self._region), summoner=Summoner(name=self._name, region=self._region), region=self._region).points
        except:
            print("Unexpected error. The default value is set to {}%".format(self._champ_mastery))
        return self._champ_mastery
    



# FOR TROUBLESHOOTING
if __name__ == "__main__":
    # print(solowr("pliuwu", "NA"))
    print("Analyzing...")
    # print(champ_wr("pliuwu", "NA", 267))




