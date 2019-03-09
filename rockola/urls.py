from django.conf.urls import url
from django.contrib import admin
import rockola.views as views

urlpatterns = [
    url(r'', views.home),
]
