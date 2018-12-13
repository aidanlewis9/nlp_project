from pprint import pprint

from analysis.ner import NER

from collections import defaultdict
from nltk.tokenize.punkt import PunktSentenceTokenizer


class Scene:
    def __init__(self):
        self.THRESHOLD = 5

        self.sentence_string = str()
        self.lines = list()
        self.full_text = ""

        self.dialogue = defaultdict(list)
        self.dialogue_text = ""
        self.dialogue_count = 0

        self.sentences = list()
        self.named_entities = set()

    def add_line(self, line):
        self.full_text += line.strip() + " "
        self.lines.append(line)

    def add_dialogue(self, character, quote):
        self.dialogue[character].append(quote)
        self.dialogue_count += 1

    def add_to_scene(self, scene):
        self.sentences.extend(scene.sentences)

    def add_sentences(self, text):
        tokenizer = PunktSentenceTokenizer()
        self.sentences = tokenizer.tokenize(text)

    def concat_sentences(self, string):
        self.sentence_string += string

    def is_valid(self):
        return self.dialogue_count > self.THRESHOLD

    def extract_named_entities(self):
        for character in self.dialogue:
            for quote in self.dialogue[character]:
                doc = NER().run(quote.strip())

                pprint([(X.text, X.label_) for X in doc.ents])
