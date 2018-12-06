from utilities.read_file import read_file
from utilities.match import match


class Book:
    def __init__(self, path):
        self.PATH_SUFFIX = "book.txt"
        self.EMPTY_STRING = ""
        self.NEWLINE = '\n'

        self.segments = list()
        self.path = path + self.PATH_SUFFIX

    def segment_script(self):
        segments = list()
        segment = self.EMPTY_STRING

        for line in read_file(self.path):
            if match(self.regex, line):
                segments.append(segment)
                segment = self.EMPTY_STRING

            segment += line + self.NEWLINE

        return segments[1:]

    def get_segments(self):
        return self.segments
