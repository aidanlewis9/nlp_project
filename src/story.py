from script import Script
from book import Book
from utilities.string import strip_nonalphanumeric


class Story:
    def __init__(self, name, script_regex, book_regex, title):
        self.ROOT_DIRECTORY = "../"
        self.DATA_PATH = self.ROOT_DIRECTORY + "data/test/"
        self.SPACE = ' '
        self.UNDERSCORE = '_'
        self.FORWARD_SLASH = "/"

        self.name = name
        path = self.get_path()

        # get script
        self.script = Script(path, script_regex)

        # get book
        self.book = Book(path, book_regex, title)

    def format_movie_name(self):
        return strip_nonalphanumeric(self.name).replace(self.SPACE, self.UNDERSCORE)

    def get_path(self):
        return self.DATA_PATH + self.format_movie_name() + self.FORWARD_SLASH
