# This file collects player data based on specific needs

from cassiopeia import Summoner, Queue, Season, Champion, apply_settings, set_riot_api_key, get_champion_mastery
from time import sleep

# SETTINGS
apply_settings(r".\\cass_settings.json")
set_riot_api_key("RGAPI-3e25c681-3fee-44fe-81ac-c9a85e456151")
season = Season.season_9
queue = Queue.ranked_solo_fives

# CONSTANTS
RANK_TO_NUMBER = dict(
    Unranked = 0,
    IronIV = 1, IronIII = 2, IronII = 3, IronI = 4,
    BronzeIV = 5, BronzeIII = 6, BronzeII = 7, BronzeI = 8,
    SilverIV = 9, SilverIII = 10, SilverII = 11, SilverI = 12,
    GoldIV = 13, GoldIII = 14, GoldII = 15, GoldI = 16,
    PlatinumIV = 17, PlatinumIII = 18, PlatinumII = 19, PlatinumI = 20,
    DiamondIV = 21, DiamondIII = 22, DiamondII = 23, DiamondI = 24,
    Master = 25,
    Grandmaster = 26,
    Challenger = 27
)

# TEMPORARY DESIGN FOR PLAYER CLASS
class Player:
    
    def __init__(self, name, region, champion, **kwargs): # kwrags is used so that users don't have to remember the order
        """Stores player data. If one or more fields is not filled out, 
        the constructor automatically sets default value(s) accordingly.
        _name is a mandatory """
        self._summoner = Summoner(name=name, region=region)
        self._champion = Champion(name=champion, region=region)
        self._region = region
        self._level = kwargs['level'] if 'level' in kwargs else 0
        self._rank = kwargs['rank'] if 'rank' in kwargs else 0
        self._rank_wr = kwargs['rank_wr'] if 'rank_wr' in kwargs else 0
        self._champ_wr = kwargs['champ_wr'] if 'champ_wr' in kwargs else 0
        self._champ_mastery = kwargs['champ_mastery'] if 'champ_mastery' in kwargs else 0

    def level(self):
        """Returns the level of a player. 
        False if that player does not exist."""
        try:
            self._level = self._summoner.level
        except:
            print("Unexpected error. The default value is set to {}.".format(self._level))
        return self._level
    
    def rank(self):
        """Returns the SoloQ rank of a player."""
        try:
            self._rank = RANK_TO_NUMBER[str(self._summoner.ranks[Queue.ranked_solo_fives]).replace(" ", "").replace("<", "").replace(">", "")]
        except:
            print("Unexpected error. The default value is set to {}.".format(self._rank))
        return self._rank

    def rank_wr(self):
        """Returns the SoloQ rank win rate of a player. 
        -1 if that player does not exist.
        -2 if there is no SoloQ info."""
        try:
            summoner_soloq_entries = self._summoner.league_entries[Queue.ranked_solo_fives]
            wins = summoner_soloq_entries.wins
            losses = summoner_soloq_entries.losses
            self._rank_wr = round((wins/(wins + losses) * 100), 1)
        except ZeroDivisionError:
            print("This person has not played any ranked SoloQ game yet. The default value is set to {}%".format(self._rank_wr))
        except:
            print("Unexpected error. The default value is set to {}%".format(self._rank_wr))
        return self._rank_wr

    def champ_wr(self, ngames=5):
        """Returns player's win rate on a specific champ on SoloQ. 
        -1 if that player does not exist.
        -2 if there is no SoloQ info for the specific champion."""
        try:
            matches = self._summoner.match_history(seasons={season}, queues={queue}, champions={self._champion})
            wins, losses = 0, 0
            for match in matches[:ngames]:
                if match.participants[self._summoner].stats.win:
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
            self._champ_mastery = get_champion_mastery(champion=self._champion, summoner=self._summoner, region=self._region).points
        except:
            print("Unexpected error. The default value is set to {}%".format(self._champ_mastery))
        return self._champ_mastery
    

# FOR TROUBLESHOOTING
# if __name__ == "__main__":
#     players = [Player("pliuwu", "NA", "Nami"), Player("jinlongr", "NA", "Akali"), Player("ifukcinghateminh", "EUW", "Wukong")]
#     for player in players:
#         print(player.champ_mastery())




