
from lib.music_library import *

def test_for_empty_library():
    music_library = MusicLibrary()
    result = music_library.library
    assert result == []

def test_for_adding_a_track():
    music_library = MusicLibrary()
    music_library.add_track("Enter Sandman")
    result = music_library.library
    assert result == ["Enter Sandman"]

def test_library_displays():
    music_library = MusicLibrary()
    music_library.add_track("Enter Sandman")
    music_library.add_track("Nothing Else Matters")
    music_library.add_track("Harvester of Sorrow")
    result = music_library.display_library()
    assert result == ["Enter Sandman", "Nothing Else Matters", "Harvester of Sorrow"]