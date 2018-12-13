from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import math


class WordEmbeddings:
    def __init__(self, story):
        self.movie_characters = story.script.get_characters()
        self.book_characters = story.book.get_characters()

        self.total_quotes = story.script.quote_count() + story.book.quote_count()

    def get_weight(self, movie_count, book_count):
        return (movie_count + book_count) / float(self.total_quotes)

    def run(self):
        score = 0

        for movie_character in self.movie_characters:
            cos_sim = 0

            for book_character in self.book_characters:
                if movie_character in self.book_characters[book_character].names:
                    # make doc 2 - movie
                    movie_document = self.movie_characters[movie_character].get_document()

                    # make doc 1 - book
                    book_document = self.book_characters[book_character].get_document()

                    cos_sim = self.get_cosine_similarity((movie_document, book_document))

                    break

            character_weight = self.get_weight(self.movie_characters[movie_character].quote_count(),
                                               self.book_characters[book_character].quote_count())

            score += (cos_sim * character_weight)

        return score

    def get_cosine_similarity(self, documents):
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

        return cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)[0][-1]

        # angle_in_radians = math.acos(cos_sim)
        # print(math.degrees(angle_in_radians))


