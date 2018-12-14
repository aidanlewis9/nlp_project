from analysis.word_embeddings import get_cosine_similarity


class CharacterMatching:
    def __init__(self, story):
        self.movie_characters = story.movie.get_characters()
        self.book_characters = story.book.get_characters()

        self.total_quotes = story.movie.quote_count() + story.book.quote_count()

    def get_weight(self, movie_count, book_count):
        return (movie_count + book_count) / float(self.total_quotes)

    def run(self):
        score = 0

        for movie_character in self.movie_characters:

            for book_character in self.book_characters:
                if movie_character in self.book_characters[book_character].names:
                    # make doc 1 - movie
                    movie_document = self.movie_characters[movie_character].get_document()

                    # make doc 2 - book
                    book_document = self.book_characters[book_character].get_document()

                    cos_sim = get_cosine_similarity((movie_document, book_document))

                    character_weight = self.get_weight(self.movie_characters[movie_character].quote_count(),
                                                       self.book_characters[book_character].quote_count())

                    score += (cos_sim * character_weight)

                    break

        return score


