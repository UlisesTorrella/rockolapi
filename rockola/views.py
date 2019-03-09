# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rockola.interface import *


SONGSFOLDER = "/home/ulises/Disk1/Projects/RockolaPi/Music"
listita = []
songs = scan_songs(SONGSFOLDER)
artists = {}
for song in songs:
    exist = False
    for key, value in artists.iteritems():
        if key == song.artist:
            exist = True
            value.append(song)
    if not exist:
        artists[song.artist] = [song]

print artists

def home(request):
    print artists.keys()
    return render(request, 'index.html', {'artists':artists.keys()})

def getSongs(request):
    artist = request.GET["artist"]
    return render(request, 'songs_list.html', {'songs':artists[artist]})

def pushSong(request):
    print "puto el que lee"
    if request.POST:
        #return HttpResponse(request.song);
        print request.POST['song']
        play_song(request.POST['song'])
        #Esto deberia ser algo asi supongo
        #  tmp = Globito(findSongByPath(request.POST.song),request.POST.macAdress);
        #  listita.append(tmp);
        return HttpResponse(200)
    else:
        return HttpResponse(400)
