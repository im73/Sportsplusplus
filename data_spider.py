import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
import datetime

from pandas import DataFrame

from storedata import history_in_database
from openpyxl import load_workbook
import datetime
class DataSpider(object):

    def __init__(self):
        self.dates = ''
        self.today_url = 'https://data.nba.net/10s/prod/v1/today.json'
        self.teams_url = 'https://data.nba.net/10s/prod/v2/2018/teams.json'
        self.scores_url = 'https://data.nba.net/10s/prod/v1/{}/scoreboard.json'
        self.players_url = 'http://data.nba.net/prod/v1/2018/players.json'
        self.players_url_hupu = 'https://nba.hupu.com/players/{}'
        self.players_profile = 'http://data.nba.net/prod/v1/2018/players/{}_profile.json'
        self.players_rating_2k = 'https://www.2kratings.com/nba2k19-team/{}'
        self.teams_schedule = 'http://data.nba.net/prod/v1/2018/teams/{}/schedule.json'
        self.teams_schedule_hupu = 'https://nba.hupu.com/schedule/{}'
        self.teams_roster = 'http://data.nba.net/prod/v1/2018/teams/{}/roster.json'
        self.teams_info_hupu = 'https://nba.hupu.com/teams/{}'
        self.schedule = 'https://www.basketball-reference.com/leagues/NBA_2019_games-{}.html'
        self.ranking_hupu = 'https://nba.hupu.com/standings'
        self.games_info_hupu = 'https://nba.hupu.com/games/{}'
        self.ranking_history = 'http://www.espn.com/nba/standings/_/season/{}'
        self.teams_history_roster = 'http://data.nba.net/prod/v1/{}/teams/{}/roster.json'
        self.teams_hupu = 'https://nba.hupu.com/teams'
        self.teams_history_member_realgm_root = 'https://basketball.realgm.com/nba/players/2019'
        self.id2name = {}
        self.en2cn = {}

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

    def get_team_schedule_hupu(self):
        with open('./id2name.txt') as f:
            teams_name = f.readlines()
            f.close()
        for name in teams_name:
            name = name.split()[-1].lower()
            text = requests.get(self.teams_schedule_hupu.format(name)).text
            soup = BeautifulSoup(text, "lxml")
            table = soup.select('table')
            df = pd.concat(pd.read_html(table[0].prettify()))
            df.to_excel('./team_schedule/{}.xlsx'.format(name))

    def get_ranking_hupu(self):
        text = requests.get(self.ranking_hupu).text
        soup = BeautifulSoup(text, "lxml")
        table = soup.select('table')
        df = pd.concat(pd.read_html(table.prettify()))
        df.to_excel('./team_standings.xlsx')

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

    def get_teams_members_hupu(self):
        with open('./id2name.txt') as f:
            teams_name = f.readlines()
            f.close()
        for name in teams_name:
            name = name.split()[-1].lower()
            team_member = {name: []}
            text = requests.get(self.players_url_hupu.format(name)).text
            soup = BeautifulSoup(text, "lxml")
            player_list = soup.find_all(attrs={'class': 'left'})
            for player in player_list:
                player_link = player.find_all('a')
                if player_link:
                    player_name = player_link[0].string
                    player_link = player_link[0].get('href')
                    player_id = player_link.split('-')[1].split('.')[0]
                    team_member[name].append({'player_id': player_id, 'player_name': player_name})
            team_member = json.dumps(team_member, sort_keys=True, indent=8,
                                     separators=(',', ':'), ensure_ascii=False)
            with open('./team_member/{}.json'.format(name), 'w', encoding='utf-8') as _f:
                _f.write(str(team_member))
                _f.close()

    def get_teams_info_hupu(self):
        with open('./id2name.txt') as f:
            teams_name = f.readlines()
            f.close()
        for name in teams_name:
            name = name.split()[-1].lower()
            text = requests.get(self.teams_info_hupu.format(name)).text
            soup = BeautifulSoup(text, "lxml")
            team_info = {name: {'技术统计': {}}}
            items = soup.find_all(attrs={'class': 'border'})[1:]
            for item in items:
                key = item.find(attrs={'class': 'a'}).string[1:]
                value = item.find(attrs={'class': 'b'}).find('b').string
                rank = item.find(attrs={'class': 'c'}).string
                team_info[name]['技术统计'][key] = {'数值': value, '排名': rank}
            more_info = soup.find(attrs={'class': 'content'})
            intro = more_info.find(attrs={'class': 'txt'}).string
            team_info[name]['介绍'] = intro[1:-1]
            ps = more_info.find_all('p')
            for p in ps:
                if not p.find('a'):
                    key = p.string.split('：')[0]
                    if key == '主场' or p.find('a'):
                        continue
                    value = p.string.split('：')[1]
                    team_info[name][key] = value
            team_info = json.dumps(team_info, sort_keys=True, indent=8, separators=(',', ':'), ensure_ascii=False)
            with open('./team_info/{}.json'.format(name), 'w', encoding='utf-8') as _f:
                _f.write(str(team_info))
                _f.close()

    def get_players_career_hupu(self):
        with open('./id2name.txt') as f:
            teams_name = f.readlines()
            f.close()
            for name in teams_name:
                name = name.split()[-1].lower()
                # print(self.players_url_hupu.format(name))
                text = requests.get(self.players_url_hupu.format(name)).text
                soup = BeautifulSoup(text, "lxml")
                # table = soup.select('table')
                # table = pd.concat(pd.read_html(table[0].prettify()))
                # table.to_excel('./teams/{}_players.xlsx'.format(name))
                lists = soup.find_all(attrs={'class': 'left'})
                for item in lists:
                    player_link = item.find_all('a')
                    if player_link:
                        player_link = player_link[0].get('href')
                        player_name_id = player_link.split('/')[-1].split('.')[0]
                        # print(player_name_id)
                        if not os.path.exists("./player_career_json/" + player_name_id):
                            os.mkdir("./player_career_json/" + player_name_id)
                        player_info = requests.get(player_link).text
                        player_soup = BeautifulSoup(player_info, "lxml")
                        tables = player_soup.select('table')
                        # is_playoff = False
                        for table in tables:
                            table_name = table.find('tr').find('td').string
                            if not table_name:
                                table_name = table.find('tr').find('b').string
                            if table_name == '1' or table_name == '排名' or \
                                    table_name[0].isdigit() or table_name == '赛季':
                                continue
                            # if table_name == '赛季' and not is_playoff:
                            #     table_name = '生涯常规赛'
                            #     is_playoff = True
                            # elif table_name == '赛季' and is_playoff:
                            #     table_name = '生涯季后赛'
                            table = pd.concat(pd.read_html(table.prettify()))
                            out = table.to_json(force_ascii=False)
                            out = json.loads(out)
                            format_out = {}
                            try:
                                for key, value in out.items():
                                    format_out[value["1"]] = value["2"]
                                format_out = json.dumps(format_out, sort_keys=True, indent=8,
                                                        separators=(',', ':'), ensure_ascii=False)
                                with open('./player_career_json/{}/{}.json'.format(player_name_id, table_name),
                                          'w', encoding='utf-8') as _f:
                                    _f.write(format_out)
                                print('./player_career_json/{}_{}.json'.format(player_name_id, table_name))
                            except:
                                continue

    def get_active_players_profile_hupu(self):
        with open('./id2name.txt') as f:
            teams_name = f.readlines()
            f.close()
            for name in teams_name:
                name = name.split()[-1].lower()
                text = requests.get(self.players_url_hupu.format(name)).text
                soup = BeautifulSoup(text, "lxml")
                lists = soup.find_all(attrs={'class': 'left'})
                for item in lists:
                    player_link = item.find_all('a')
                    if player_link:
                        player_link = player_link[0].get('href')
                        player_name_id = player_link.split('/')[-1].split('.')[0]
                        if not os.path.exists("./player_profile_json/" + player_name_id):
                            os.mkdir("./player_profile_json/" + player_name_id)
                        player_info = requests.get(player_link).text
                        player_soup = BeautifulSoup(player_info, "lxml")
                        content = player_soup.find(attrs={'class': 'content_a'})
                        img_link = content.find('img').get('src')
                        # print(img_link)
                        with open('./player_profile_json/{}/portrait.png'.format(player_name_id), 'wb') as _f:
                            img = requests.get(img_link).content
                            _f.write(img)
                            _f.close()
                        profile_info = content.find_all('p')
                        info = {'中文名': player_soup.find('title').string.split('|')[0][1:],
                                '英文名': player_soup.find('title').string.split('|')[1],
                                '序号': player_name_id.split('-')[1]}
                        for p in profile_info:
                            if p.string:
                                info[p.string.split('：')[0]] = p.string.split('：')[1]
                            else:
                                info['球队'] = p.find('a').string
                        info = json.dumps(info, sort_keys=True, indent=8, separators=(',', ':'), ensure_ascii=False)
                        with open('./player_profile_json/{}/profile.json'.format(player_name_id),
                                  'w', encoding='utf-8') as _f:
                            _f.write(str(info))
                            f.close()
                        print(player_name_id)

    def get_teams_roster(self):
        with open('./id2name.txt') as f:
            teams_id = [id_n_name.split()[0] for id_n_name in f.readlines()]
        f.close()
        for team_id in teams_id:
            print(team_id)
            team_roster = requests.get(self.teams_roster.format(team_id)).json()
            team_roster = json.dumps(team_roster, sort_keys=True, indent=8, separators=(',', ':'))
            with open('./{}_roster.json'.format(team_id), 'w') as f:
                f.write(str(team_roster))
            f.close()

    def get_player_profile(self):
        with open('./active_players.json') as f:
            active_players = json.load(f)
        f.close()
        active_players = active_players['active_players']
        for player in active_players:
            print(player['personId'])
            player_profile = requests.get(self.players_profile.format(player['personId'])).json()
            player_profile = json.dumps(player_profile, sort_keys=True, indent=8, separators=(',', ':'))
            with open('./{}_profile.json'.format(player['personId']), 'w') as f:
                f.write(str(player_profile))
            f.close()

    def get_player_rating(self):
        with open('./id2name.txt') as f:
            items = f.readlines()
            for item in items:
                name_list = item.split()[1:]
                team_name = "" + name_list[0].lower()
                for element in name_list[1:]:
                    team_name += "-" + element.lower()
                print(team_name)
                text = requests.get(self.players_rating_2k.format(team_name)).text
                soup = BeautifulSoup(text, "lxml")
                table = soup.select('table')
                df = pd.concat(pd.read_html(table[0].prettify()))
                df.to_excel('./player_rating/{}.xlsx'.format(team_name))

    @staticmethod
    def get_date_set(begin_date, end_date):
        dates = []
        dt = datetime.datetime.strptime(begin_date, '%Y-%m-%d')
        date = begin_date
        while date <= end_date:
            dates.append(date)
            dt = dt + datetime.timedelta(1)
            date = dt.strftime('%Y-%m-%d')
        return dates

    @staticmethod
    def table2json(table):
        table = pd.concat(pd.read_html(table.prettify()))
        out = table.to_json(force_ascii=False)
        out = json.loads(out)
        return out

    @staticmethod
    def form_format(out):
        pass

    def get_history_games_info_hupu(self):
        today_date = str(datetime.date.today())
        time=datetime.datetime.now()

        date_set = self.get_date_set((time-datetime.timedelta(days=1)).strftime("%Y-%m-%d"), time.strftime("%Y-%m-%d"))
        print(date_set)
        for date in date_set:
            text = requests.get(self.games_info_hupu.format(date)).text
            soup = BeautifulSoup(text, "lxml")
            games = soup.find_all(attrs={'class': 'border_a'})
            for game in games:
                state = game.find(attrs={'class': 'team_vs_b'}).find(attrs={'class': 'b'}).string[1:]
                print(state)
                if state != '已结束' or date == today_date:
                    continue
                game = game.find(attrs={'class': 'table_choose clearfix'}).find(attrs={'class': 'd'}).get('href')
                game_id = game.split('/')[-1]
                if not os.path.exists('./history_games(date)/{}-{}'.format(date, game_id)):
                    os.mkdir('./history_games(date)/{}-{}'.format(date, game_id))
                game_text = requests.get(game).text
                game_soup = BeautifulSoup(game_text, "lxml")
                sum_table = game_soup.find(attrs={'class': 'itinerary_table'})
                sum_table = pd.concat(pd.read_html(sum_table.prettify()))
                sum_table.to_excel('./history_games(date)/{}-{}/summary.xlsx'.format(date, game_id))
                away_table = game_soup.find(attrs={'id': 'J_away_content'})
                away_table = pd.concat(pd.read_html(away_table.prettify()))
                away_table.to_excel('./history_games(date)/{}-{}/away_table.xlsx'.format(date, game_id))
                home_table = game_soup.find(attrs={'id': 'J_home_content'})
                home_table = pd.concat(pd.read_html(home_table.prettify()))
                home_table.to_excel('./history_games(date)/{}-{}/home_table.xlsx'.format(date, game_id))
                print(date + " " + game_id)

    @staticmethod
    def name_transform():
        with open('./en2cn.txt') as f:
            content = f.readlines()
            f.close()
        en2cn = {}
        for line in content:
            en_name = line.split(' ')[0] + ".xlsx"
            cn_name = line.split(' ')[1][:-1] + ".xlsx"
            en2cn[en_name] = cn_name
        root_path = './player_rating/'
        files = os.listdir(root_path)
        for file in files:
            cn_name = en2cn[file]
            os.rename(root_path + file, root_path + cn_name)
            print(root_path + cn_name)

    def build_en2cn(self):
        with open('./en2cn.txt') as f:
            content = f.readlines()
            f.close()
        for line in content:
            en_name = line.split(' ')[0]
            cn_name = line.split(' ')[1][:-1]
            self.en2cn[en_name] = cn_name

    def get_cn_name(self, en_name):
        return self.en2cn[en_name]

    def get_history_team_roster(self):
        self.build_en2cn()
        with open('./id2name.txt') as f:
            teams_id_name = f.readlines()
            f.close()
        with open('./active_players.json') as f:
            active_players = json.load(f)
            f.close()
        active_players = active_players['active_players']
        id2name = {}
        for player in active_players:
            if len(player['temporaryDisplayName'].split()) >= 2:
                name = player['temporaryDisplayName'].split()[1] + " " + player['temporaryDisplayName'].split()[0]
            else:
                name = player['temporaryDisplayName']
            id2name[player['personId']] = name
        for id_name in teams_id_name:
            _id = id_name.split()[0]
            team_name = id_name.split(' ', 1)[1][:-1].lower()
            team_name = team_name.split()[0] + '-' + team_name.split()[1]
            team_name = self.get_cn_name(team_name)
            print(team_name)
            sum_team = {}
            for year in range(2013, 2019):
                url = self.teams_history_roster.format(year, _id)
                roster = requests.get(url).json()
                roster = json.dumps(roster, sort_keys=True, indent=8, separators=(',', ':'))
                roster = roster['league']
                players = []
                for player in roster:
                    if id2name[player['personId']]:
                        players.append(id2name[player['personId']])
                    else:
                        players.append("Mr.Unknown")
                sum_team[year] = players
            sum_team = json.dumps(sum_team, sort_keys=True, indent=8, separators=(',', ':'))
            with open('./team_roster/{}.json'.format(team_name)) as f:
                f.write(str(sum_team))
                f.close()

    def get_history_team_member_realgm(self):
        self.build_en2cn()
        team_link = 'https://basketball.realgm.com/nba/players/{}/{}'
        text = requests.get(self.teams_history_member_realgm_root).text
        soup = BeautifulSoup(text, "lxml")
        all_select = soup.find_all(attrs={'class': 'page-nav-option clearfix'})
        for select in all_select:
            label = select.find('label')
            if label and label.string == 'Team:':
                options = select.find_all('option')
                for option in options:
                    if option.string == 'Entire NBA':
                        continue
                    team_index = option.get('value').split('/', 4)[4]
                    for season in range(2013, 2019):
                        year = season + 1
                        history_member_text = requests.get(team_link.format(year, team_index)).text
                        history_member_soup = BeautifulSoup(history_member_text, "lxml")
                        table = history_member_soup.select('table')
                        df = pd.concat(pd.read_html(table[0].prettify()))
                        team_name = self.get_cn_name(option.string.replace(' ', '-').lower())
                        if not os.path.exists('./history_member/{}'.format(team_name)):
                            os.mkdir('./history_member/{}'.format(team_name))
                        df.to_excel('./history_member/{}/{}.xlsx'.format(team_name, season))
                        print('./history_member/{}/{}'.format(team_name, season))

    def get_teams_img(self):
        text = requests.get(self.teams_hupu).text
        soup = BeautifulSoup(text, "lxml")
        six_divisions = soup.find_all(attrs={'class': 'team'})
        for division in six_divisions:
            division_teams_boxes = division.find_all(attrs={'class': 'box'})
            for box in division_teams_boxes:
                img_link = box.find('img').get('src')
                team_name = box.find('h2').string
                print(img_link)
                img = requests.get(img_link).content
                with open('./teams_img/{}.png'.format(team_name), 'wb') as f:
                    f.write(img)
                    f.close()
    def get_future_game_info_hupu(self):
        time=datetime.datetime.now()
        date_set = self.get_date_set(time.strftime("%Y-%m-%d"),(time+datetime.timedelta(days=5)).strftime("%Y-%m-%d") )
        print(date_set)
        for date in date_set:
            text = requests.get(self.games_info_hupu.format(date)).text
            soup = BeautifulSoup(text, "lxml")
            games = soup.find_all(attrs={'class': 'border_a'})
            for game in games:
                state = game.find(attrs={'class': 'team_vs_b'}).find(attrs={'class': 'b'}).string
                if not state:
                    state = '未开始'
                if state != '未开始':
                    print("ERROR")
                    break
                game = game.find(attrs={'class': 'table_choose clearfix'}).find(attrs={'class': 'd'}).get('href')
                game_id = game.split('/')[-1]
                if not os.path.exists('./history_games(date)/{}-{}'.format(date, game_id)):
                    os.mkdir('./history_games(date)/{}-{}'.format(date, game_id))
                game_text = requests.get(game).text
                game_soup = BeautifulSoup(game_text, "lxml")
                team_a = game_soup.find(attrs={'class': 'team_a'}).find(attrs={'class': 'message'}).find('a').string
                team_b = game_soup.find(attrs={'class': 'team_b'}).find(attrs={'class': 'message'}).find('a').string
                output = {'0': ['', team_a, team_b],
                          '1': ['一', '', ''],
                          '2': ['二', '', ''],
                          '3': ['三', '', ''],
                          '4': ['四', '', ''],
                          '5': ['总分', '', '']}
                df = DataFrame(output)
                df.to_excel('./history_games(date)/{}-{}/summary.xlsx'.format(date, game_id))
                print(date + " " + game_id)

    def get_playing_game_info_hupu(self):
        today_date = str(datetime.date.today())
        print(today_date)
        text = requests.get(self.games_info_hupu.format(today_date)).text
        soup = BeautifulSoup(text, "lxml")
        games = soup.find_all(attrs={'class': 'border_a'})
        game_number = len(games)
        over_games = set()
        for game in games:
            state = game.find(attrs={'class': 'team_vs_b'}).find(attrs={'class': 'b'}).string[1:]
            if not state:
                state = "未开始"
            if state == '已结束':
                game = game.find(attrs={'class': 'table_choose clearfix'}).find(attrs={'class': 'd'}).get('href')
                game_id = game.split('/')[-1]
                if os.path.exists('./history_games(date)/{}-{}-playing'.format(today_date, game_id)):
                    os.rename('./history_games(date)/{}-{}-playing'.format(today_date, game_id),
                          './history_games(date)/{}-{}'.format(today_date, game_id))
                over_games.add(game_id)
                if len(over_games) == game_number:
                    break
            elif state != '已结束' and state != '未开始':
                # the game is playing
                game = game.find(attrs={'class': 'table_choose clearfix'}).find(attrs={'class': 'd'}).get('href')
                game_id = game.split('/')[-1]
                if not os.path.exists('./history_games(date)/{}-{}-playing'.format(today_date, game_id)):
                    os.mkdir('./history_games(date)/{}-{}-playing'.format(today_date, game_id))
                game_text = requests.get(game).text
                game_soup = BeautifulSoup(game_text, "lxml")
                sum_table = game_soup.find(attrs={'class': 'itinerary_table'})
                if sum_table:
                    sum_table = pd.concat(pd.read_html(sum_table.prettify()))
                    sum_table.to_excel('./history_games(date)/{}-{}-playing/summary.xlsx'.format(today_date, game_id))
                    away_table = game_soup.find(attrs={'id': 'J_away_content'})
                    away_table = pd.concat(pd.read_html(away_table.prettify()))
                    away_table.to_excel('./history_games(date)/{}-{}-playing/away_table.xlsx'.format(today_date, game_id))
                    home_table = game_soup.find(attrs={'id': 'J_home_content'})
                    home_table = pd.concat(pd.read_html(home_table.prettify()))
                    home_table.to_excel('./history_games(date)/{}-{}-playing/home_table.xlsx'.format(today_date, game_id))
                else:
                    team_a = game_soup.find(attrs={'class': 'team_a'}).find(attrs={'class': 'message'}).find('a').string
                    team_b = game_soup.find(attrs={'class': 'team_b'}).find(attrs={'class': 'message'}).find('a').string
                    output = {'0': ['', team_a, team_b],
                          '1': ['一', '', ''],
                          '2': ['二', '', ''],
                          '3': ['三', '', ''],
                          '4': ['四', '', ''],
                          '5': ['总分', '', '']}
                    df = DataFrame(output)
                    df.to_excel('./history_games(date)/{}-{}-playing/summary.xlsx'.format(today_date, game_id))
                print(today_date + " " + game_id)



# if __name__ == '__main__':
#     ds = DataSpider()
    # ds.get_scores()
    # ds.get_active_players()
    # ds.get_schedule()
    # ds.get_player_profile()
    # ds.get_teams_roster()
    # ds.get_players_career_hupu()
    # ds.get_active_players_profile_hupu()
    # ds.get_teams_members_hupu()
    # ds.get_teams_info_hupu()
    # ds.get_player_rating()
    # ds.get_team_schedule_hupu()
    # ds.get_ranking_hupu()
    # ds.get_history_games_info_hupu()
    # ds.name_transform()
    # ds.get_history_team_roster()
    # ds.get_teams_img()
    # ds.get_history_team_member_realgm()
