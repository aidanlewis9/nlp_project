from utilities.read_file import read_file
from utilities.match import match
from segment import Segment


class Book:
    def __init__(self, path, regex):
        self.PATH_SUFFIX = "book.txt"
        self.EMPTY_STRING = ""
        self.NEWLINE = '\n'

        self.segments = list()
        self.path = path + self.PATH_SUFFIX
        self.regex = regex

        self.segment_book()

    def segment_book(self):
        segment = Segment()

        for line in read_file(self.path):
            # print(line)
            if match(self.regex, line):
                print("matched:", line)
                self.segments.append(segment)
                segment = Segment()

            segment.add_line(line)
        for segment in self.segments:
            print('------------------------------------------------------')
            # print(segment.lines)
            print(segment)

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
