from nba_api.stats.endpoints import CommonAllPlayers
import pandas as pd

seasons_list = [str(a) + "-" + str(b)[2:4] for (a,b) in zip(range(1997,2024), range(1998, 2025))]
all_players = pd.Series([])
for season in seasons_list:
    common_all_players = CommonAllPlayers(
        is_only_current_season = 1,
        league_id = '00',
        season =  season
    )
    players_list = common_all_players.get_data_frames()[0]['DISPLAY_FIRST_LAST']
    all_players = pd.concat([all_players, players_list])
unique_players = all_players.unique()

#dataset.txt
for player in unique_players:
    print(player)

#seasons.txt
for season in seasons_list:
  print(season)
