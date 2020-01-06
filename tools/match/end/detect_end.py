import requests
from cassiopeia import Summoner, set_riot_api_key

# SETTINGS
set_riot_api_key("RGAPI-3e25c681-3fee-44fe-81ac-c9a85e456151")

# CONVERT URL TO 
r = requests.get("https://gameinfo.saltyteemo.com")
r2 = requests.get(r.url).history
print(r2)
# URL = r2.url
# info = URL.split('/live/')[1].split('?')[0]
# region, name = info.split('/')

# # 
# summoner = Summoner(name=name, region=region.upper())
# print(summoner)