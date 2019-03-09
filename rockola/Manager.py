import Queue
from Blob import Blob
import Interface

def play():
    songs = Interface.scan_songs()
    while True:
        if Queue.hasNext():
            next_blob = Queue.getNext()
            next_song = next_blob.song
            Interface.play_song(next_song.path)
        else:
            Interface.play_random_song(songs)