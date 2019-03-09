# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rockola.interface import *

listita = []

def home(request):
    songs = scan_songs("music/basicsongs")
    print songs
    return render(request, 'index.html', {'songs':songs})

def pushSong(request):
    print "puto el que lee"
    if request.POST:
        #return HttpResponse(request.song);
        play_song(request.POST['song'])
        #Esto deberia ser algo asi supongo
        #  tmp = Globito(findSongByPath(request.POST.song),request.POST.macAdress);
        #  listita.append(tmp);
        return HttpResponse(200)
    else:
        return HttpResponse(400)
