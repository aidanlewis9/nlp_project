from pprint import pprint

from analysis.ner import NER
from utilities.string import limit_whitespace

from collections import defaultdict, Counter
from nltk.tokenize.punkt import PunktSentenceTokenizer
import re


class Scene:
    def __init__(self):
        self.sentence_string = str()
        self.lines = list()
        self.full_text = ""

        self.words_spoken = Counter()
        self.speakers = dict()  # proportion of scene dialogue
        self.spoken_about = Counter()  # number of times spoken about

        self.dialogue = defaultdict(list)
        self.dialogue_text = ""

        self.sentences = list()
        self.named_entities = set()

    def add_line(self, line):
        self.full_text += line.strip() + " "
        self.lines.append(line)

    def add_dialogue(self, character, quote):
        # print(character)
        self.dialogue[limit_whitespace(character).title()].append(self.format_quote(quote))

    def format_quote(self, quote):
        return re.sub("[\(\[].*?[\)\]]", "", limit_whitespace(quote))

    def add_sentences(self, text):
        tokenizer = PunktSentenceTokenizer()
        self.sentences = tokenizer.tokenize(text)

    def concat_sentences(self, string):
        self.sentence_string += string

    def extract_named_entities(self):
        # doc = NER().run(self.dialogue_text)

        for character in self.dialogue:
            for quote in self.dialogue[character]:
                doc = NER().run(quote.strip())

                pprint([(X.text, X.label_) for X in doc.ents])


        # dialogue_text = self.dialogue.values()

        # pprint([(X.text, X.label_) for X in doc.ents])

