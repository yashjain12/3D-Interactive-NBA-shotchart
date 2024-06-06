import numpy as np
import pandas as pd

from nba_api.stats.static import players
from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.endpoints import playercareerstats

def shotchart(player_name, szn):
    playerList = players.get_players()
    player_dict = [player for player in playerList if player['full_name'].lower() == player_name.lower()][0]

    careerstats = playercareerstats.PlayerCareerStats(player_id = player_dict['id'])
    careerstats = careerstats.get_data_frames()[0]
    team_id = careerstats[careerstats['SEASON_ID'] == szn]['TEAM_ID']
    team_name = careerstats[careerstats['SEASON_ID'] == szn]['TEAM_ABBREVIATION']
    #create try/exception here to check if int(team_id) and int(player_id) actually work
    shotchartlist = shotchartdetail.ShotChartDetail(team_id=int(team_id), 
                                                    player_id=int(player_dict['id']), 
                                                    season_type_all_star='Regular Season', 
                                                    season_nullable=szn,
                                                    context_measure_simple="FGA").get_data_frames()

    player_shots = shotchartlist[0]
    player_shots = player_shots[(abs(player_shots['LOC_X']) > 0.2) & (abs(player_shots['LOC_Y']) > 0.2)]
    player_shots['hypotenuse'] = (player_shots['LOC_X']**2 + player_shots['LOC_Y']**2)**(1/2)
    player_shots['LOC_X'] = player_shots['LOC_X'] * player_shots['SHOT_DISTANCE'] / player_shots['hypotenuse']
    player_shots['LOC_Y'] = player_shots['LOC_Y'] * player_shots['SHOT_DISTANCE'] / player_shots['hypotenuse']
    return player_shots[['LOC_X', 'LOC_Y', 'SHOT_MADE_FLAG']]