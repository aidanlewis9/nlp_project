from nltk.tokenize.punkt import PunktSentenceTokenizer

from scenes.scene import Scene


class BookScene(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.sentence_string = str()
        self.sentences = list()

    def add_to_scene(self, scene):
        self.sentences.extend(scene.sentences)

    def add_sentences(self, text):
        tokenizer = PunktSentenceTokenizer()
        self.sentences = tokenizer.tokenize(text)

    def concat_sentences(self, string):
        self.sentence_string += string

    def get_text(self):
        return " ".join(self.sentences)
