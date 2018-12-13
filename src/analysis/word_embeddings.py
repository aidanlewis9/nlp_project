

class WordEmbeddings:
    def __init__(self, story):
        self.movie_characters = story.script.get_characters()
        self.book_characters = story.book.get_characters()

    def run(self):
        for movie_character in self.movie_characters:
            has_match = False

            for book_character in self.book_characters:
                if movie_character in self.book_characters[book_character].names:
                    has_match = True

                    print("Yup: {}".format(movie_character))

            if not has_match:
                print("Nope: {}".format(movie_character))


