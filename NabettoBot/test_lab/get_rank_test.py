import socket, configparser, requests


class RiotAPI:
    """
    SN: Summoner Name
    SID: Summoner ID
    """
    API_methods = dict(
        summoner_by_name= 'summoner/v4/summoners/by-name',
        league_by_summonerID= 'league/v4/entries/by-summoner'
    )
    API_regions = dict(
        na  = 'na1',
        euw = 'euw1',
        eune= 'eun1',
        oce = 'oc1',
        lan = 'la1',
        las = 'la2',
        kr  = 'kr',
        jp  = 'jp1',
        br  = 'br1',
        tr  = 'tr1',
        ru  = 'ru'
    )
    @classmethod
    def __init__(cls, api_key):
        cls.api_key = api_key

    @classmethod
    def request(cls, **kwargs) -> dict:
        params = {'API KEY': cls.api_key}
        params.update(kwargs)

        region = params.get('region', 'na') # Update region value to actual API region value
        params['region'] = cls.API_regions[region]

        response = requests.get(f"https://{params['region']}.api.riotgames.com/lol/{params['method']}/{params['args']}?api_key={params['API KEY']}")
        return response.json()

    @staticmethod
    def GETGameInfo() -> tuple:
        """Returns a player's name and the region for the current saltyteemo game stream

        Example:
        RiotAPI.GETGameInfo() -> ('na', 'Kato2')
        """
        r = requests.get("https://gameinfo.saltyteemo.com")
        URL = r.url
        info = URL.split('/live/')[1].split('?')[0]
        region, SN = info.split('/')
        return (region, SN)

    @classmethod
    def GETSummonerIDbyName(cls, region, SN:"Summoner Name") -> str:
        """Returns the Summoner ID for a given Summoner name (player name).

        Args:
        region -- The player's region ID.
        SN     -- The player's name.

        Example:
        RiotAPI.GETSummonerIDbyName('na', Kato2) -> 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        """
        response = cls.request(method=cls.API_methods['summoner_by_name'], region=region, args=SN)
        return response['id']

    @classmethod
    def GETWinLossPercent(cls, region, SID:"Summoner ID") -> float:
        """Returns the Win/Loss percentage for the given summoner ID (SID).
        The SID can be retrived using RiotAPI.GETSummonerIDbyName("Player")

        Args:
        region -- The player's region ID.
        SID    -- The Summoners Encrypted ID (SID)

        Example:
        RiotAPI.GETWinLossPercent('na', 'SIDSIDSIDSID') -> 59.34
        """
        response = cls.request(method=cls.API_methods['league_by_summonerID'],\
                                region=region,\
                                args=SID).pop()
        wins, losses = response['wins'], response['losses']
        WL: "Win Loss percentage" = (wins/(wins+losses))*100
        return round(WL, 2)

    @classmethod
    def GETRank(cls, region, SID:"Summoner ID") -> "{TIER} {RANK}":
        """Returns the "Rank" (Tier Rank) for the given Summoner ID

        Args:
        region -- The player's region ID.
        SID    -- The player's encrypted Summoner ID.

        Example:
        RiotAPI.GetRank('na', 'SIDSIDSIDSID') -> 'IRON II'
        """

        response = cls.request(method=cls.API_methods['league_by_summonerID'],\
                                region=region,\
                                args=SID).pop()
        tier, rank = response['tier'], response['rank']
        return f"{tier} {rank}"


if __name__ == "__main__":
    riotapi = RiotAPI(r"ID")
    sn = input("Welcome to scuffed OP.GG!\nEnter summoner name: ")
    region = input("Please enter the region: ")
    get_summoner_id = riotapi.GETSummonerIDbyName(region, sn)
    get_rank = riotapi.GETRank(region, get_summoner_id)
    print(get_rank)