import cassiopeia as cass

cass.set_riot_api_key("RGAPI-a8d2fb22-b294-4e02-a0f9-d0ab9005b20e")

print("WELCOME TO SCUFFED WINRATE CHECKER:")
try:
    while True:
        name = input("Enter your summoner name: ")
        region = input("Enter your region in caps (ex. North America = NA): ")
        champion_name = input("Enter your champion name (spelling count!): ")
        print("Analyzing...")

        season = cass.Season.season_9
        queue = cass.Queue.ranked_solo_fives
        champion = cass.Champion(region=region, name="Morgana")
        current_summoner = cass.Summoner(name=name, region=region)
        matches = current_summoner.match_history(seasons={season}, queues={queue}, champions={champion})
        win_counter, lose_counter = 0, 0
        wr = 0
        
        if len(matches) < 20:
            if len(matches) == 0:
                pass
            else:
                for match in matches:
                    if match.participants[current_summoner].stats.win:
                        win_counter += 1
                    else:
                        lose_counter += 1
        else:
            for match in matches[:20]:
                if match.participants[current_summoner].stats.win:
                    win_counter += 1
                else:
                    lose_counter += 1
        try:
            wr =  win_counter / (win_counter + lose_counter) * 100            
        except ZeroDivisionError:
            wr = 0

        print("\n\nOkay %s, your current SOLOQ rank is %s.\nYour current ranked winrate is %s%% based on the last 20 ranked games with %s win(s) and %s lose(s).\nYou can keep going or exit by Ctrl + C.\n\n" % (current_summoner.name, current_summoner.ranks[cass.Queue.ranked_solo_fives], wr, win_counter, lose_counter))
except KeyboardInterrupt:
    print("Program exit...")
