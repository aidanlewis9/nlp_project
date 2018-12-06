from script import Script
from book import Book

import re


class Story:
    def __init__(self, name, script_regex, book_regex):
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
        self.book = Book(path, book_regex)

    def strip_nonalphanumeric(self):
        regex = "([^\s\w]|_)+"
        return re.compile(regex).sub('', self.name)

    def format_movie_name(self):
        return self.strip_nonalphanumeric().replace(self.SPACE, self.UNDERSCORE)

    def get_path(self):
        return self.DATA_PATH + self.format_movie_name() + self.FORWARD_SLASH

    def get_script(self):
        return self.script

