# location.py

class Location:
    def __init__(self, name):
        self.name = name
        self.connected_locations = []
        self.characters_present = []
        self.clues = []

    def connect_location(self, location):
        if location not in self.connected_locations:
            self.connected_locations.append(location)
            location.connected_locations.append(self)

    def add_character(self, character):
        if character not in self.characters_present:
            self.characters_present.append(character)
            character.location = self

    def remove_character(self, character):
        if character in self.characters_present:
            self.characters_present.remove(character)
            character.location = None

    def add_clue(self, clue):
        self.clues.append(clue)