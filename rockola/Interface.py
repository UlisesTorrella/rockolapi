import os
from Song import *
import pygame
from eyed3 import id3
import random


def scan_songs(path):
    songs = []
    for root, directories, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)
            tag = id3.Tag()
            tag.parse(path)
            album = tag.album
            artist = tag.artist
            title = tag.title
            genre = tag.genre
            song = Song(title, path, artist, album, genre)
            songs.append(song)
    return songs


def play_random_song(songs):
    selected = random.randint(1, len(songs))
    play_song(songs[selected].path)


def play_song(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue