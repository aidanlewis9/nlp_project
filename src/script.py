from segment import Segment
from utilities.read_file import read_file
from utilities.match import match
from utilities.is_empty import is_empty

from collections import defaultdict


class Script:
    def __init__(self, path, regex):
        self.PATH_SUFFIX = "script.txt"
        self.EMPTY_STRING = ""
        self.EXCLAMATION_POINT = '!'
        self.NEWLINE = '\n'
        self.QUOTE = '"'

        self.regex = regex
        self.path = path + self.PATH_SUFFIX

        self.segments = self.segment_script()
        self.dialogue = defaultdict(list)

    def segment_script(self):
        segments = list()
        segment = Segment()

        for line in read_file(self.path):
            if match(self.regex, line):
                segments.append(segment)
                segment = Segment()

            segment.add_line(line)

        return segments

    def get_segments(self):
        return self.segments

    def extract_dialogue(self):
        for segment in self.segments:
            lines = segment.get_lines()
            n = len(lines)

            # while i < 0:
            #     if lines[i].isupper() and not is_empty(lines[i + 1]) \
            #             and self.EXCLAMATION_POINT not in lines[i]:
            #         segment.add_dialogue(lines[i], lines[i + 1])


