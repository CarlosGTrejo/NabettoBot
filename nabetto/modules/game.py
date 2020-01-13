import requests
from cassiopeia import Summoner, Queue, Season, Champion, get_champion_mastery
from datapipelines import common
import nabetto.modules.utils as utils

season = Season.season_9
queue = Queue.ranked_solo_fives

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

class Match: # TODO: Check if a player is in a match using the player object.
    @staticmethod
    def in_game():
        """Checks if there is currently a game streaming on SaltyTeemo."""
        try:
            URL = requests.get("https://gameinfo.saltyteemo.com").url
            region, name = URL.split('/live/')[1].split('?')[0].split('/')
            current_match = Summoner(name=name, region=region.upper()).current_match()
            return current_match.duration
        except common.NotFoundError:
            utils.logger.debug("Stream is currently not in game.")
            return -1
        

class Player:
    
    def __init__(self, name, region, champion, **kwargs): # kwrags is used so that users don't have to remember the order
        """Stores player data. If one or more fields is not filled out, 
        the constructor automatically sets default value(s) accordingly.
        _name is a mandatory """
        self._summoner = Summoner(name=name, region=region)
        self._champion = Champion(name=champion, region=region)
        self._region = region
        self._level = kwargs['level'] if 'level' in kwargs else self._summoner.level
        self._rank = kwargs['rank'] if 'rank' in kwargs else RANK_TO_NUMBER[str(self._summoner.ranks[queue]).replace(" ", "").replace("<", "").replace(">", "")]
        self._rank_wr = kwargs['rank_wr'] if 'rank_wr' in kwargs else -1
        self._champ_wr = kwargs['champ_wr'] if 'champ_wr' in kwargs else -1
        self._champ_mastery = kwargs['champ_mastery'] if 'champ_mastery' in kwargs else 0

    def level(self):
        """Returns the level of a player. 
        False if that player does not exist."""
        return self._level
 
    
    def rank(self):
        """Returns the SoloQ rank of a player."""
        return self._rank

    def rank_wr(self):
        """Returns the SoloQ rank win rate of a player. 
        -1 if that player does not exist.
        -2 if there is no SoloQ info."""
        summoner_soloq_entries = self._summoner.league_entries[queue]
        wins = summoner_soloq_entries.wins
        losses = summoner_soloq_entries.losses
        self._rank_wr = round((wins/(wins + losses) * 100), 1)
            
        if wins+losses == 0: print("This person has not played any ranked SoloQ game yet. The default value is set to -1")

    def champ_wr(self, ngames=5):
        """Returns player's win rate on a specific champ on SoloQ. 
        -1 if that player does not exist.
        -2 if there is no SoloQ info for the specific champion."""
        try:
            matches = self._summoner.match_history(seasons={season}, champions={self._champion})
            wins, losses = 0, 0
            for match in matches[:ngames]:
                if match.participants[self._summoner].stats.win: wins += 1
                else: losses += 1

            if wins+losses == 0: print("This person has not played any ranked SoloQ game yet. The default value is set to -1")
            else: self._rank_wr = round((wins/(wins + losses) * 100), 1)

        except:
            print("Unexpected error. The default value is set to {}%".format(self._champ_wr))
        return self._rank_wr

    def champ_mastery(self):
        """Returns player's mastery on a specific champ. 
        -1 if that player does not exist."""
        try:
            self._champ_mastery = get_champion_mastery(champion=self._champion, summoner=self._summoner, region=self._region).points
        except:
            utils.logger.error("Unexpected error. The default value is set to {}.".format(self._champ_mastery))
        return self._champ_mastery
