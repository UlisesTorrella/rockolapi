# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from interface import *

# Create your views here.
def home(request):
    return render(request, 'index.html', {})
def pushSong(request):
    if request.POST:
        #return HttpResponse(request.song);
        play_song(request.song);
        return HttpResponse('andando');
    else:
        return HttpResponse('no andando');
