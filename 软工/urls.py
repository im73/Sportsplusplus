"""软工 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app_user.user import views as user_view
from player_data.persons import views as info_view
from app_user.operation import  views as op_view
from app_user.mymatch import views as mth_view

urlpatterns = [


    path('admin/', admin.site.urls),
    path('api/login',                           user_view.login),
    path('api/register',                        user_view.register),
    path('api/user',                            user_view.users),
    path('api/BackUser',                        user_view.BackUser),
    path('api/back_login',                      user_view.back_login),
    path('api/Changepassword',                  user_view.Changepassword),
    path('api/BackHome',                        user_view.BackHome),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path(r'api/GetTeamInfo',                                                        info_view.get_teaminfo),
    path(r'api/GetPlayerImage/<str:PlayerName>',                                    info_view.GetPlayerImage),
    path(r'api/GetTeamImage/<str:Teamname>',                                        info_view.GetTeamImage),
    path(r'api/GetPlayerInfo',                                                      info_view.get_playerinfo),
    path(r'api/GetPlayerCareer',                                                    info_view.get_playercareer),
    path(r'api/GetPlayerSummary',                                                   info_view.GetPlayerSummary),
    path(r'api/GetTeamSummary',                                                     info_view.GetMatchSummary),
    path(r'api/GetMatch',                                                           info_view.GetMatchInfo),
    path(r'api/GetSchedule',                                                        info_view.GetSchedule),
    path(r'api/BackSchedule',                                                       info_view.GetBackMatch),

    path('api/Subscribe',                       op_view.Sbscribe),
    path('api/TeamSubscribe',                   op_view.TeamSubscribe),
    path('api/Validate',                        op_view.Validate),

    path('api/MySchedule',                      mth_view.myschedule),
    path('api/MyMatch',                         mth_view.mymatch),
    path('api/PlayerInfo',                      mth_view.player),
    path('api/AllShedule',                      mth_view.AllSchedule),
    path('api/SubForGame',                      mth_view.Subforgame),
    path('api/BackGame',                        mth_view.back_schedule),
    path('api/GameInfo',                        mth_view.GetInfo),


]
