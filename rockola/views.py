# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html', {})
