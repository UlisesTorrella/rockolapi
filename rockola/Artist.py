from Song import Song

class Artist:
    albums = []
    def __init__(self, name):
        self.name = name

    def add_album(album):
        albums.push(album)

    def get_albums(self):
        return self.albums
    def __str__(self):
        return "Path: " + str(self.path) + "\nFileName: " + str(self.name) + "\nArtist: " + str(self.artist) + "\nAlbum: " + str(self.album) + "\nGenre: " + str(self.genre)

class Album:
    songs = []
    def __init__(self, name):
        self.name = name
        
    def add_song(song):
        songs.push(song)

    def get_songs(self):
        return songs
