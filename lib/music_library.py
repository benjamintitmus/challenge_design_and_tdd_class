
class MusicLibrary():

    def __init__(self):
        self.library = []

    def add_track(self, track_name):
        self.library.append(track_name)

    def display_library(self):
        return self.library