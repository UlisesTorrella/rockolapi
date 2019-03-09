class Blob:
    def __init__(self, song, rankings):
         self.song = song
         self.ranking = rankings


    def addVote(self, identifier):
        self.ranking.append(identifier)
