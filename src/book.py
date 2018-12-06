from utilities.read_file import read_file
from utilities.match import match


class Book:
    def __init__(self, path, regex):
        self.PATH_SUFFIX = "book.txt"
        self.EMPTY_STRING = ""
        self.NEWLINE = '\n'

        self.segments = list()
        self.path = path + self.PATH_SUFFIX
        self.regex = regex

    def segment_book(self):
        segment = self.EMPTY_STRING

        for line in read_file(self.path):
            if match(self.regex, line):
                self.segments.append(segment)
                segment = self.EMPTY_STRING

            segment += line + self.NEWLINE

    def get_segments(self):
        return self.segments

    # def extract_dialogue(self):
    #     dialogue = list()
    #
    #     for segment in self.segments:
    #         curr_quote = ""
    #         in_quote = False
    #
    #         for char in segment:
    #             if char == self.QUOTE:
    #                 in_quote = not in_quote
    #
    #             if in_quote:
    #                 curr_quote += char
