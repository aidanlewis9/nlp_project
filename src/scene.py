from collections import defaultdict


class Scene:
    def __init__(self):
        self.lines = list()
        self.dialogue = defaultdict(list)

    def add_line(self, line):
        self.lines.append(line)

    def add_dialogue(self, character, quote):
        self.dialogue[character].append(quote)
