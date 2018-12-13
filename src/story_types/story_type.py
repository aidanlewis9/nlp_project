from characters.character_controller import CharacterController
from scenes.scene_controller import SceneController


class StoryType:
    def __init__(self, regex):
        self.regex = regex

        self.sc = SceneController()
        self.cc = CharacterController()

    def get_characters(self):
        return self.cc.characters

    def get_quotes(self, character):
        return self.cc.get_quotes(character)

    def scene_count(self):
        return len(self.sc.scenes)

    def quote_count(self):
        return self.cc.total_quotes

    def __str__(self):
        s = str()

        for character in self.get_characters():
            s += "Character: |{}|\nQuotes:\n".format(character)
            for i, quote in enumerate(self.get_quotes(character)):
                s += "{}. |{}|\n".format(i + 1, quote)
            s += "\n---------------------------------------------------------\n"

        return s
