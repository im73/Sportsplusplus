import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


class GetLiveGames(object):
    def __init__(self):
        self.dates = ''
        self.today_url = 'https://data.nba.net/10s/prod/v1/today.json'
        self.teams_url = 'https://data.nba.net/10s/prod/v2/2018/teams.json'
        self.scores_url = 'https://data.nba.net/10s/prod/v1/{}/scoreboard.json'
        self.players_url = 'http://data.nba.net/prod/v1/2018/players.json'
        self.player_profile = 'http://data.nba.net/prod/v1/2018/players/{}_profile.json'
        self.team_schedule = 'http://data.nba.net/prod/v1/2018/teams/{}/schedule.json'
        self.schedule = 'https://www.basketball-reference.com/leagues/NBA_2019_games-{}.html'
        self.id2name = {}

    def get_dates(self):
        today_data = requests.get(self.today_url).json()
        self.dates = today_data['links']['currentDate']

    def build_id2name(self):
        # teams = requests.get(self.teams_url).json()
        # teams = teams['league']['vegas']
        # for team in teams:
        #     self.id2name[team['teamId']] = team['fullName']
        #     print(team['teamId'] + " " + team['fullName'])
        with open('./id2name.txt') as f:
            id_names = f.readlines()
        for id_name in id_names:
            _id = id_name.split()[0]
            name = id_name.split(' ', 1)[1]
            name = name[:-1]
            self.id2name[_id] = name
        f.close()

    def get_schedule(self):
        # for team_id in self.id2name.keys():
        #     schedule = requests.get(self.team_schedule.format(team_id))
        #     print(schedule)
        months = ['october', 'november', 'december', 'january', 'february', 'march', 'april']
        df = []
        for month in months:
            text = requests.get(self.schedule.format(month)).text
            soup = BeautifulSoup(text, "lxml")
            table = soup.select('table')
            df.append(pd.concat(pd.read_html(table[0].prettify())))
        df = pd.concat(df)
        df.to_excel('./schedule-season2018.xlsx')

    def get_scores(self):
        self.get_dates()
        self.build_id2name()
        while True:
            games = requests.get(self.scores_url.format(self.dates)).json()['games']
            for game in games:
                print(self.id2name[game['hTeam']['teamId']] + " " + game['hTeam']['score'])
                print(self.id2name[game['vTeam']['teamId']] + " " + game['vTeam']['score'])
                print('----------------------')
            time.sleep(3)

    def get_active_players(self):
        active_players_data = {}
        players = requests.get(self.players_url).json()['league']['standard']
        active_players_data['active_players'] = players
        active_players_data = json.dumps(active_players_data, sort_keys=True, indent=8, separators=(',', ':'))
        with open('./active_players.json', 'w') as f:
            f.write(active_players_data)
        f.close()

    def get_teams(self):
        pass

    def get_player_profile(self):
        with open('./active_players.json') as f:
            active_players = json.load(f)
        active_players = active_players['active_players']
        # profile = {}
        for player in active_players:
            print(player['personId'])
            player_profile = requests.get(self.player_profile.format(player['personId'])).json()
            # profile[player['personId']] = player_profile
            player_profile = json.dumps(player_profile, sort_keys=True, indent=8, separators=(',', ':'))
            with open('./{}_profile.json'.format(player['personId']), 'w') as f:
                f.write(str(player_profile))
            f.close()


if __name__ == '__main__':
    glg = GetLiveGames()
    # glg.get_scores()
    # glg.get_active_players()
    # glg.get_schedule()
    glg.get_player_profile()
