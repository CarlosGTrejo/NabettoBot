import datetime

from cassiopeia import Summoner, Queue, Season, Champion, get_champion_mastery, apply_settings
from datapipelines import common

import nabetto.modules.utils as utils
import nabetto.modules.web_scrape as web_scrape

default_settings = {
    "RiotAPI": {
        "api_key": "RIOT_API_KEY"
    },
    "logging": {
        "print_calls": False,
        "print_riot_api_key": False
    }
}

apply_settings(default_settings)

# SETTINGS -- Temporary usage
season = Season.season_9
queue = Queue.ranked_solo_fives

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


class Team:
    def __init__(self, color, *args):
        pass


class Stream:  # TODO: Check if a player is in a match using the player object.

    region, name = None, None

    @classmethod
    def init(cls, region, name):
        cls.region = region.upper()
        cls.name = name

    @classmethod
    def in_game(cls):
        """Checks if there is currently a game streaming on SaltyTeemo."""
        try:
            current_match = Summoner(
                name=cls.name, region=cls.region).current_match()
            return current_match.duration
        except common.NotFoundError:
            return datetime.timedelta(0)

    @classmethod
    def check_queue(cls):
        return Summoner(name=cls.name, region=cls.region).current_match().queue

    @classmethod
    def get_participant_data(cls):
        """Return all participant data."""

        participants_data = []
        participants = Summoner(
            name=cls.name, region=cls.region).current_match().participants
        for participant in participants:
            participant_name = participant.summoner.name
            participant_champ = participant.champion.name
            participants_data.append(
                Player(participant_name, cls.region, participant_champ))

        return participants_data

class Player:
    # kwargs is used so that users don't have to remember the order
    def __init__(self, name, region, champion):
        """Stores player data. If one or more fields is not filled out, 
        the constructor automatically sets default value(s) accordingly.
        name is a mandatory
        instance variables:
        summoner
        champion
        region
        level
        rank
        champ_mastery
        rank_wr
        champ_wr"""
        self.summoner = Summoner(name=name, region=region)
        self.champion = Champion(name=champion, region=region)
        self.region = region
        self.level = self.summoner.level
        self.rank = RANK_TO_NUMBER[str(self.summoner.ranks[queue]).replace(
            " ", "").replace("<", "").replace(">", "")]
        self.champ_mastery = get_champion_mastery(champion=self.champion,
                                                  summoner=self.summoner,
                                                  region=self.region).points

    def __str__(self):
        return f"""Summoner: {self.summoner}
        Champion: {self.champion}
        Region: {self.region}
        Level: {self.level}
        Rank: {self.rank}
        Champion WR: {self.champ_wr}
        Champion mastery: {self.champ_mastery}
        Ranked WR: {self.rank_wr}"""

    @property
    def rank_wr(self):
        summoner_soloq_entries = self.summoner.league_entries[queue]
        wins = summoner_soloq_entries.wins
        losses = summoner_soloq_entries.losses
        if wins + losses == 0:
            print(
                "This person has not played any ranked SoloQ game yet. The default value is set to -1")
            return -1
        else:
            return round((wins / (wins + losses) * 100), 1)

    @property
    def champ_wr(self):
        """Returns player's win rate on a specific champ on SoloQ.
        -1 if that player does not exist."""
        if self.champ_mastery == 0:
            return -1
        else:
            matches = self.summoner.match_history(
                seasons={season}, champions={self.champion})
            wins, losses = 0, 0
            for match in matches[:5]:
                if match.participants[self.summoner].stats.win:
                    wins += 1
                else:
                    losses += 1
            return round((wins / (wins + losses) * 100), 1)

    def __getitem__(self, key):
        try:
            if str(key).isnumeric():
                return [*self.__dict__.values()][key]
            else:
                return getattr(self, key)
        except Exception as e:
            utils.logger.error(e)


if __name__ == "__main__":
    if Stream.in_game() > datetime.time(0, 5, 0):
        utils.logger.debug("True")
    else:
        utils.logger.debug("False")
