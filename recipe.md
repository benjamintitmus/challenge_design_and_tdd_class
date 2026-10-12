
# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicLibrary:
    # User-facing properties:
    #   name: string

    def __init__(self):

        pass # No code here yet

    def add_track(self, track_name):
        # Parameters:
        #   task: string representing a single track name
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the track name to the list.
        # Throws an exception if there's no track_name given.
        pass # No code here yet

    def display_library(self):
        # Returns:
        #   A list of all the tracks in the library
        # Side-effects:
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
music_library = MusicLibrary()
music_library.library
= [] # => Make sure an empty library is created

"""
Given a name and no task
#remind raises an exception
"""
music_library = MusicLibrary()
music_library.add_track("Enter Sandman") # Add Enter Sandman to the list."
['Enter Sandman']

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
music_library = MusicLibrary()
music_library.display_library()
['A list', 'of', 'tracks'] # => Should show all the added tracks.

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
