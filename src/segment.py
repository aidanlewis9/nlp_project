from collections import defaultdict


class Segment:
    def __init__(self):
        self.lines = list()
        self.dialogue = defaultdict(list)

    def add_line(self, line):
        self.lines.append(line)

    def add_dialogue(self, character, quote):
        self.dialogue[character].append(quote)

    def get_lines(self):
        return self.lines

    def get_dialogue(self):
        return self.dialogue
