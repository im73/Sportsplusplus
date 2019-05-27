# -*- coding:utf-8 -*-
import pandas as pd
import math
import csv
import random
import numpy as np
import pymysql as MySQLdb
MySQLdb.install_as_MySQLdb()
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
dic_name = {
    '凯尔特人':'Boston Celtics',
    '76人':'Philadelphia 76ers',
    '勇士': 'Golden State Warriors',
    '雷霆': 'Oklahoma City Thunder',
    '活塞': 'Detroit Pistons',
    '篮网': 'Brooklyn Nets',
    '黄蜂': 'Charlotte Hornets',
    '雄鹿': 'Milwaukee Bucks',
    '步行者': 'Indiana Pacers',
    '灰熊': 'Memphis Grizzlies',
    '魔术': 'Orlando Magic',
    '热火': 'Miami Heat',
    '尼克斯': 'New York Knicks',
    '老鹰': 'Atlanta Hawks',
    '猛龙': 'Toronto Raptors',
    '骑士': 'Cleveland Cavaliers',
    '火箭': 'Houston Rockets',
    '鹈鹕': 'New Orleans Pelicans',
    '马刺': 'San Antonio Spurs',
    '森林狼': 'Minnesota Timberwolves',
    '国王': 'Sacramento Kings',
    '爵士': 'Utah Jazz',
    '太阳': 'Phoenix Suns',
    '独行侠': 'Dallas Mavericks',
    '快船': 'Los Angeles Clippers',
    '掘金': 'Denver Nuggets',
    '公牛': 'Chicago Bulls',
    '奇才': 'Washington Wizards',
    '开拓者': 'Portland Trail Blazers',
    '湖人': 'Los Angeles Lakers',
}
base_elo = 1600
team_elos = {}
team_stats = {}
X = []
y = []
k1 = 2100
k2 = 2500
Helo = 1100
# 计算每个球队的elo值
def calc_elo(win_team, lose_team):
    winner_rank = get_elo(win_team)
    loser_rank = get_elo(lose_team)

    rank_diff = winner_rank - loser_rank
    exp = (rank_diff  * -1) / 400
    odds = 1 / (1 + math.pow(10, exp))
    # 根据rank级别修改K值
#     if winner_rank < 2100:
#         k = 32
#     elif winner_rank >= 2100 and winner_rank < 2400:
#         k = 24
#     else:
#         k = 16
    if winner_rank < k1:
        k = 32
    elif winner_rank >= k1 and winner_rank < k2:
        k = 24
    else:
        k = 16
    new_winner_rank = round(winner_rank + (k * (1 - odds)))
    new_rank_diff = new_winner_rank - winner_rank
    new_loser_rank = loser_rank - new_rank_diff

    return new_winner_rank, new_loser_rank

# 根据每支队伍的Miscellaneous Opponent，Team统计数据csv文件进行初始化
def initialize_data(path):
    Mstat = pd.read_excel(path+"Miscellaneous Stats.xlsx",header = 1)
    Ostat = pd.read_excel(path+"Opponent Per Game Stats.xlsx")
    Tstat = pd.read_excel(path+"Team Per Game Stats.xlsx")
    new_Mstat = Mstat.drop(['Rk', 'Arena'], axis=1)
    new_Ostat = Ostat.drop(['Rk', 'G', 'MP'], axis=1)
    new_Tstat = Tstat.drop(['Rk', 'G', 'MP'], axis=1)

    team_stats1 = pd.merge(new_Mstat, new_Ostat, how='left', on='Team')
    team_stats1 = pd.merge(team_stats1, new_Tstat, how='left', on='Team')

    #team_stats1.loc[:,('Team')]=team_stats1.loc[:,('Team')] #test_dict_df.loc[:,'english']=[90,80,70,90,90,59]
    team_stats1.loc[:,('Team')] = [g.replace("*","") for g in team_stats1.loc[:,('Team')] ]####数据问题
    #print(team_stats1.loc[:,('Team')])
    return team_stats1.set_index('Team', inplace=False, drop=True)

def get_elo(team):
    try:
        return team_elos[team]
    except:
        # 当最初没有elo时，给每个队伍最初赋base_elo
        team_elos[team] = base_elo
        return team_elos[team]

def  build_dataSet(all_data):
    #print("Building data set..")###把主场队伍放前面
    cnt = 0
    for index, row in all_data.iterrows():
        if row['Date'] == "Playoffs":##数据问题
            continue
        team1_elo,team2_elo = 0,0
        if row['PTS'] < row['PTS.1']:
            Wteam = row['Home/Neutral']
            Lteam = row['Visitor/Neutral']
            team1_elo += Helo
        else:
            Lteam = row['Home/Neutral']
            Wteam = row['Visitor/Neutral']
            team2_elo += Helo

        #获取最初的elo或是每个队伍最初的elo值
        team1_elo += get_elo(Wteam)
        team2_elo += get_elo(Lteam)

        # 给主场比赛的队伍加上100的elo值
        # if row['WLoc'] == 'H':
        #     team1_elo += 100
        # else:
        #     team2_elo += 100

        # 把elo当为评价每个队伍的第一个特征值
        team1_features = [team1_elo]
        team2_features = [team2_elo]

        # 添加我们从basketball reference.com获得的每个队伍的统计信息
        #print(Wteam)
        try:
            for key, value in team_stats.loc[Wteam].iteritems():
                team1_features.append(value)
            for key, value in team_stats.loc[Lteam].iteritems():
                team2_features.append(value)
        except KeyError as e:
            print(Wteam)
            print(Lteam)
            print(row)
        # 保证左右两边特征的分布
        if cnt == 1:
            X.append(team1_features + team2_features)
            y.append(0)
        else:
            X.append(team2_features + team1_features)
            y.append(1)
        cnt ^= 1
        # 根据这场比赛的数据更新队伍的elo值
        new_winner_rank, new_loser_rank = calc_elo(Wteam, Lteam)
        team_elos[Wteam] = new_winner_rank
        team_elos[Lteam] = new_loser_rank

    return np.nan_to_num(X), np.array(y)

def build_newdata():

    cnt = 0
    X,y = [],[]
    #print(team_stats)
    db = MySQLdb.connect("114.116.156.240", "root", "Buaa2019!", "app", charset='utf8' )
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    sql = "SELECT * FROM persons_match"
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        #print(row)
        if row[1] not in dic_name or row[2] not in dic_name:
            continue
        team1_elo,team2_elo = 0,0
        if int(row[4]) > int(row[9]):#前面的是主队
            Wteam = dic_name[row[1]]
            Lteam = dic_name[row[2]]
            team1_elo += Helo
        else:
            Wteam = dic_name[row[2]]
            Lteam = dic_name[row[1]]
            team2_elo += Helo
        team1_elo += get_elo(Wteam)
        team2_elo += get_elo(Lteam)
        # 把elo当为评价每个队伍的第一个特征值
        team1_features = [team1_elo]
        team2_features = [team2_elo]
        #print(Wteam)
        try:
            for key, value in team_stats.loc[Wteam].iteritems():
                team1_features.append(value)
            for key, value in team_stats.loc[Lteam].iteritems():
                team2_features.append(value)
        except KeyError as e:
            print(Wteam)
            print(Lteam)
            print(row)
        # 将两支队伍的特征值随机的分配在每场比赛数据的左右两侧
        # 并将对应的0/1赋给y值
        #if random.random() > 0.5:
        if cnt == 1:
            X.append(team1_features + team2_features)
            y.append(0)
        else:
            X.append(team2_features + team1_features)
            y.append(1)
            cnt ^= 1
        # 根据这场比赛的数据更新队伍的elo值
        new_winner_rank, new_loser_rank = calc_elo(Wteam, Lteam)
        team_elos[Wteam] = new_winner_rank
        team_elos[Lteam] = new_loser_rank

    # 关闭数据库连接
    db.close()
    return np.nan_to_num(X), np.array(y)

def predict_winner(team_1, team_2, model):
    team_1 = dic_name[team_1]
    team_2 = dic_name[team_2]
    features = []

    # team 1，客场队伍
    features.append(get_elo(team_1))
    for key, value in team_stats.loc[team_1].iteritems():
        features.append(value)

    # team 2，主场队伍
    features.append(get_elo(team_2) + Helo)
    for key, value in team_stats.loc[team_2].iteritems():
        features.append(value)

    features = np.nan_to_num(features)
    return model.predict_proba([features])

def pre_train():
    path = 'predict/ai_data'
    folder = "data"
    tx,ty = [],[]
    X,y = [],[]
    global team_stats
    for year in range(2018,2019):#2013,2019
        #print(year)
        #team_elos = {}#可以试着不清空
        team_stats = initialize_data(path+"/season_summary/"+str(year)+"/")
        result_data = pd.read_excel(path +'/season_schedule_result/'+str(year)+".xlsx")
        X, y = build_dataSet(result_data)
        tx.extend(X)
        ty.extend(y)
    X, y = build_newdata()
    tx.extend(X)
    ty.extend(y)

    model = LogisticRegression()
    #print(len(tx))
    #print(len(ty))
    model.fit(tx, ty)
    return model

if __name__ == '__main__':
    model = pre_train()
    pred = predict_winner("雄鹿", "凯尔特人", model)#后者主场
    print(pred[0][0])
    # #利用10折交叉验证计算训练正确率
    # print("Doing cross-validation..")
    # print(cross_val_score(model, tx, ty, cv = 10, scoring='accuracy', n_jobs=-1).mean())
