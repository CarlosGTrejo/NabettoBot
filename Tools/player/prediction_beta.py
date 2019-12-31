
import cassiopeia as cass

cass.set_riot_api_key("RGAPI-c8e115b0-c98b-4ec6-9b9d-53dcbe11d6bb")

print("WELCOME TO SCUFFED WINRATE CHECKER:")
try:
    while True:
        name = input("Enter your summoner name: ")
        region = input("Enter your region in caps (ex. North America = NA): ")
        print("Analyzing...")
        
        current_summoner = cass.Summoner(name=name, region=region) # One of the summoner
        season = cass.Season.season_9 # Indicate the season
        queue = current_summoner.current_match().queue # Get type of queue
        current_match_participants = current_summoner.current_match().participants # Get all participants from that match
        
        
        for participant in current_match_participants:
            participant_champion = participant.champion
            print(participant_champion)
            matches = participant.summoner.match_history(seasons={season}, queues={queue}, champions={participant_champion})
            win_counter, lose_counter = 0, 0
            wr = 0
            if len(matches) < 5:
                if len(matches) == 0:
                    pass
                else:
                    for match in matches:
                        if match.participants[participant.summoner].stats.win:
                            win_counter += 1
                        else:
                            lose_counter += 1
            else:
                for match in matches[:5]:
                    if match.participants[participant.summoner].stats.win:
                        win_counter += 1
                    else:
                        lose_counter += 1
            try:
                wr =  win_counter / (win_counter + lose_counter) * 100            
            except ZeroDivisionError:
                wr = 0
            try:    
                print("\n\nOkay, %s current SOLOQ rank is %s.\nThe current ranked winrate is %s%% based on the last %s ranked games with %s (%s win(s) and %s lose(s)).\n\n" % (participant.summoner.name, participant.summoner.ranks[cass.Queue.ranked_solo_fives], wr, win_counter + lose_counter, participant_champion.name, win_counter, lose_counter))
            except KeyError:
                print("\n\nOkay, %s current SOLOQ rank is %s.\nThe current ranked winrate is %s%% based on the last %s ranked games with %s (%s win(s) and %s lose(s)).\n\n" % (participant.summoner.name, "Unranked", wr, win_counter + lose_counter, participant_champion.name, win_counter, lose_counter))
except KeyboardInterrupt:
    print("Program exit...")
