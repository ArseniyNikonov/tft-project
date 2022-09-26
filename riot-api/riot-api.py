from riotwatcher import TftWatcher, ApiError
import pandas as pd

# golbal variables
api_key = 'RGAPI-43aa9d92-75d0-4f02-b560-8575b6d577d9'
watcher = TftWatcher(api_key)
my_region = 'EUN1'

me = watcher.summoner.by_name(my_region, 'Dandy Panda')
for key in me:
    print("{}:{}".format(key,me[key]))

my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
for key in my_ranked_stats[0]:
    print("{}:{}".format(key,my_ranked_stats[0][key]))

my_matches = watcher.match.by_puuid(my_region, me['puuid'])

last_match = my_matches[0]
match_detail = watcher.match.by_id(my_region, last_match)

print(match_detail)

