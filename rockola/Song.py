class Song:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def __str__(self):
        return "Path: " + self.path + "\nFileName: " + self.name
