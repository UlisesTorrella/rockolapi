import os
from Song import *
import pygame


def scan_songs(path):
    songs = []
    for root, directories, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)
            song = Song(filename, path)
            songs.append(song)
    return songs


def play_song(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
