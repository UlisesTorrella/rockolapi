# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rockola.interface import *

# Create your views here.
def home(request):
    songs = scan_songs("music/basicsongs")
    print songs
    return render(request, 'index.html', {'songs':songs})
