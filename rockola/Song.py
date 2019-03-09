class Song:
    def __init__(self, name, path, artist, album, genre):
        self.name = name
        self.path = path
        self.artist = artist
        self.album = album
        self.genre = genre

    def __str__(self):
        return "Path: " + str(self.path) + "\nFileName: " + str(self.name) + "\nArtist: " + str(self.artist) + "\nAlbum: " + str(self.album) + "\nGenre: " + str(self.genre)
