# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rockola.interface import *

def home(request):
    songs = scan_songs("music/basicsongs")
    print songs
    return render(request, 'index.html', {'songs':songs})

def pushSong(request):
    print "puto el que lee"
    if request.POST:
        print request.POST['song']
        play_song("../" + request.POST['song']);
        return HttpResponse('andando');
    else:
        return HttpResponse('no andando');
