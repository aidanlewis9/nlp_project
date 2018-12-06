from src.utilities.read_file import read_file
from src.utilities.match import match


class Script:
    def __init__(self, path, regex):
        self.PATH_SUFFIX = "script.txt"
        self.EMPTY_STRING = ""
        self.NEWLINE = '\n'

        self.regex = regex
        self.path = path + self.PATH_SUFFIX

        self.segments = self.segment_script()

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
