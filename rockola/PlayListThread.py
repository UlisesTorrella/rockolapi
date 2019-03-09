from threading import Thread
import Queue
import Interface

class PlayListThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        songs = Interface.scan_songs("/media/usb")
        while True:
            if Queue.hasNext():
                next_blob = Queue.getNext()
                next_song = next_blob.song
                Interface.play_song(next_song.path)
            else:
                Interface.play_random_song(songs)
