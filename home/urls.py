from django.contrib import admin
from django.http import request
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.login, name= 'login'),
    path("home", views.index, name= 'home'),
    path("library", views.library , name="library"),
    path("community", views.community , name="community"),
    path("advanceSearch", views.advanceSearch , name="advanceSearch"),
    path("signup", views.signup , name="signup"),
    path("login", views.login , name="login"),
    path("addgame", views.addgame, name="addgame"),
    path("game/<str:name>/", views.game, name="game"),
    path("game/<str:name>/tournaments", views.tournaments, name="tournaments"),
    path("game/<str:name>/proplayers", views.proPlayers, name="proplayers"),
    path("game/<str:name>/proteams", views.proTeams, name="proteams"),
    path("game/<str:name>/developers", views.developers, name="developers"),
    path("game/<str:name>/news", views.news, name="news"),
    path("game/<str:name>/updates", views.updates, name="updates"),
    path("game/<str:name>/awards", views.awards, name="awards"),
]