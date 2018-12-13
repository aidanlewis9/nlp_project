from collections import defaultdict

from characters.character import Character


class CharacterController:
    def __init__(self):
        self.characters = defaultdict(Character)
        self.total_quotes = 0

    def get_quotes(self, character):
        return self.characters[character].quotes

    def add_quote(self, character, quote):
        self.characters[character].add_quote(quote)
        self.total_quotes += 1

    def add_character(self, character_name, character):
        self.characters[character_name] = character
        self.total_quotes += len(character.quotes)

    def clean(self):
        for character in list(self.characters.keys()):
            if not self.characters[character].is_necessary():
                del self.characters[character]
