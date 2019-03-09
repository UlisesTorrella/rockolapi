from django.conf.urls import url
from django.contrib import admin
import rockola.views as views

urlpatterns = [
    url(r'^$', views.home),
    url(r'/push_song', views.pushSong,name='pushSong'),
    url(r'/get_songs', views.getSongs,name='getSongs'),
]
