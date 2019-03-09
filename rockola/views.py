# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from rockola.Blob import Blob
from rockola.Globito import Globo
from rockola.Interface import *
from rockola.Queue import addBlob

play_list = []

def home(request):
    songs = scan_songs("/media/usb")
    print songs
    return render(request, 'index.html', {'songs':songs})

def pushSong(request):
    print "puto el que lee"
    if request.POST:
        #return HttpResponse(request.song);
        #play_song(request.POST['song'])
        #Esto deberia ser algo asi supongo
        globo = Blob(request.POST['song'],[1])
        addBlob(globo)
        return HttpResponse(200)
    else:
        return HttpResponse(400)

