from threading import Thread

from rockola.Interface import *

import Queue


class PlayListThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        print "here im 1"
        #songs = scan_songs("/media/usb")
        print "here im 2"
        while True:
            if Queue.hasNext():
                print "Hay next"
                next_blob = Queue.getNext()
                next_song = next_blob.song
                play_song(next_song.path)
            else:
                print "Moriremos todos!!!!"
                play_random_song("/media/usb/Alarm01.wav")