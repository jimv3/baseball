import pandas as pd
import random as rnd


class Game:
    def __init__(self):
        stats = pd.read_csv('../data/batters.csv', header=0)
        stats['1B'] = stats['H'] - (stats['2B'] + stats['3B'] + stats['HR'])
        stats['1B%'] = stats['1B'] / stats['H']
        stats['2B%'] = stats['2B'] / stats['H']
        stats['3B%'] = stats['3B'] / stats['H']
        stats['HR%'] = stats['HR'] / stats['H']
        stats['Opportunities'] = stats['AB'] + \
            stats['HBP'] + stats['BB'] + stats['SF']
        games_filter = stats['G'] > 5
        stats = stats.loc[games_filter]
        self._data = stats[['Player', 'Team', 'Pos', '1B%',
                            '2B%', '3B%', 'HR%', 'BB', 'HBP', 'SF', 'AVG', 'OBP']].copy()

    def list_teams(self):
        return sorted(list(self._data['Team'].unique()))

    def get_players(self, team):
        team_filter = self._data['Team'] == team.upper()
        return self._data.loc[team_filter]

    def at_bat(self, player):
        hit_or_onbase = rnd.random()
        if hit_or_onbase > (1 - player['AVG'].values[0]):
            type_of_hit = rnd.random()
            if type_of_hit > (1 - player['HR%'].values[0]):
                return 'HR'
            elif type_of_hit > (1 - player['3B%'].values[0]):
                return '3B'
            elif type_of_hit > (1 - player['2B%'].values[0]):
                return '2B'
            else:
                return '1B'
        elif hit_or_onbase > (1 - player['OBP'].values[0]):
            bb_hbp_sf = rnd.random()
            return 'WALK'
        else:
            return 'OUT'
