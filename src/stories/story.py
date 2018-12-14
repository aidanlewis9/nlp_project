from story_types.movie import Movie
from story_types.book import Book
from utilities.string import format_movie_name


class Story:
    def __init__(self, name, movie_regex, book_regex, title):
        self.ROOT_DIRECTORY = "../"
        self.DATA_PATH = self.ROOT_DIRECTORY + "data/test/"
        self.FORWARD_SLASH = "/"

        self.name = name
        path = self.get_path()

        # get movie
        self.movie = Movie(path, movie_regex)

        # get book
        self.book = Book(path, book_regex, title, self.movie.scene_count())

    def get_path(self):
        return self.DATA_PATH + format_movie_name(self.name) + self.FORWARD_SLASH
