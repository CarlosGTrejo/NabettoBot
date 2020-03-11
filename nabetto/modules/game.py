import datetime

from cassiopeia import (Champion, Queue, Season, Summoner, apply_settings,
                        get_champion_mastery)
from datapipelines import common

# import nabetto.modules.utils as utils
# import nabetto.modules.web_scrape as web_scrape

import utils
from web_scrape import web_scrape

# SETTINGS -- Temporary usage
season = Season.season_9
queue = Queue.ranked_solo_fives
settings = utils.load_settings()
print(settings)
apply_settings(settings['Cassiopeia'])

RANK_TO_NUMBER = dict(
    Unranked=0,
    IronIV=1, IronIII=2, IronII=3, IronI=4,
    BronzeIV=5, BronzeIII=6, BronzeII=7, BronzeI=8,
    SilverIV=9, SilverIII=10, SilverII=11, SilverI=12,
    GoldIV=13, GoldIII=14, GoldII=15, GoldI=16,
    PlatinumIV=17, PlatinumIII=18, PlatinumII=19, PlatinumI=20,
    DiamondIV=21, DiamondIII=22, DiamondII=23, DiamondI=24,
    Master=25,
    Grandmaster=26,
    Challenger=27
)


class Stream:  # TODO: Check if a player is in a match using the player object.
    @classmethod
    def in_game(cls):
        """Checks if there is currently a game streaming on SaltyTeemo."""
        try:
            region, name = web_scrape()
            current_match = Summoner(
                name=name, region=region.upper()).current_match()
            return current_match.duration
        except common.NotFoundError:
            return datetime.timedelta(0)


class Player:
    # kwrags is used so that users don't have to remember the order
    def __init__(self, name, region, champion):
        """Stores player data. If one or more fields is not filled out,
        the constructor automatically sets default value(s) accordingly.
        _name is a mandatory """
        self.summoner = Summoner(name=name, region=region)
        self.champion = Champion(name=champion, region=region)
        self.region = region
        self.level = self.summoner.level
        self.rank = RANK_TO_NUMBER[str(self.summoner.ranks[queue]).replace(
            " ", "").replace("<", "").replace(">", "")]
        self.champ_mastery = self.champ_mastery = get_champion_mastery(
            champion=self.champion,
            summoner=self.summoner, region=self.region).points
        self.rank_wr = 0
        self.champ_wr = 0

    def __str__(self):
        return f"""Summoner: {self.summoner}
        Champion: {self.champion}
        Region: {self.region}
        Level: {self.level}
        Rank: {self.rank}
        Champion WR: {self.champ_wr}
        Champion mastery: {self.champ_mastery}
        Ranked WR: {self.rank_wr}"""

    def collect_rank_wr(self):
        summoner_soloq_entries = self.summoner.league_entries[queue]
        wins = summoner_soloq_entries.wins
        losses = summoner_soloq_entries.losses
        if wins+losses == 0:
            self.rank_wr = -1
        else:
            self.rank_wr = round((wins/(wins + losses) * 100), 1)

    def collect_champ_wr(self, ngames=5):
        """Returns player's win rate on a specific champ on SoloQ.
        -1 if that player does not exist."""
        if self.champ_mastery == 0:
            self.champ_wr = -1
        else:
            matches = self.summoner.match_history(
                seasons={season}, champions={self.champion})
            wins, losses = 0, 0
            for match in matches[:ngames]:
                if match.participants[self.summoner].stats.win:
                    wins += 1
                else:
                    losses += 1
            self.champ_wr = round((wins/(wins + losses) * 100), 1)

    def __getitem__(self, key):
        try:
            if str(key).isnumeric():
                return [*self.__dict__.values()][key]
            else:
                return getattr(self, key)
        except IndexError:
            raise


if __name__ == "__main__":
    print(ingame)
    if (ingame.seconds / 60) > 0 and (ingame.seconds / 60) < 5:
        print("True")
    else:
        print("False")
