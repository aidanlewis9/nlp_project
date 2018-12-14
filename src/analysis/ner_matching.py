from analysis.ner import NER
from analysis.word_embeddings import get_cosine_similarity
from utilities.string import limit_whitespace


class NERMatching:
    def __init__(self, story):
        self.SPACE = " "

        self.book_scenes = story.book.get_scenes()
        self.movie_scenes = story.movie.get_scenes()

    def create_documents(self, scenes):
        doc = str()

        for scene in scenes:
            text = limit_whitespace(scene.get_text())
            entities = " ".join([entity.text.lower() for entity in NER().run(text).ents])
            doc += self.SPACE + entities

        return doc

    def run(self):
        book_doc = self.create_documents(self.book_scenes)
        movie_doc = self.create_documents(self.movie_scenes)

        return get_cosine_similarity((movie_doc, book_doc))
