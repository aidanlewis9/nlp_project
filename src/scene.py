from collections import defaultdict
from nltk.tokenize.punkt import PunktSentenceTokenizer

class Scene:
    def __init__(self):
        self.sentence_string = str()
        self.lines = list()
        self.dialogue = defaultdict(list)
        self.sentences = list()

    def add_line(self, line):
        self.lines.append(line)

    def add_dialogue(self, character, quote):
        self.dialogue[character].append(quote)

    def add_sentences(self, text):
        tokenizer = PunktSentenceTokenizer()
        self.sentences = tokenizer.tokenize(text)

    def concat_sentences(self, string):
        self.sentence_string += string
