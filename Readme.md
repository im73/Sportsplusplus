# Sportsplusplus
## 项目说明
这是北航2019年软工项目——Sportsplusplus(一个看NBA比赛的平台)
整个项目分为以下三个部分：

- 安卓端——提供一个看NBA球队比赛比分信息，球队球员信息等平台
- [网页端](https://github.com/im73/Sportsplusplus_frontend)——主要用于后台人员分析用户的活跃度，球队的关注度
- [后端](https://github.com/im73/Sportsplusplus)——所有的数据逻辑都由后端提供。包括爬虫和后台api部分


## 配置说明
安卓端使用原生android,版本是8.0.

网页端使用的是React

后端使用的是Django

数据库使用的是mysql5.7

后端部署是通过 ngix + uwsgi 

## 后端说明

Crawler 文件夹下面的是爬虫部分的代码，爬取NBA比赛及对于球员的所有信息并存储到数据库之中。app_user 文件夹下面的包括用户的基本信息，关注信息，注册等。media文件夹下面是球员球队的照片。player_data下面是球队球员信息的后台逻辑。predict部分使用的是决策树来预测两个队伍的胜率。forum 已经废弃。

## usage

> python manage.py runserver
