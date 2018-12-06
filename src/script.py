from segment import Segment
from utilities.read_file import read_file
from utilities.match import match
from utilities.is_empty import is_empty


class Script:
    def __init__(self, path, regex):
        self.PATH_SUFFIX = "script.txt"
        self.EMPTY_STRING = ""
        self.EXCLAMATION_POINT = '!'
        self.NEWLINE = '\n'
        self.QUOTE = '"'

        self.regex = regex
        self.path = path + self.PATH_SUFFIX

        self.segments = list()

        self.segment_script()
        self.extract_dialogue()

    def segment_script(self):
        segment = Segment()

        for line in read_file(self.path):
            if match(self.regex, line):
                self.segments.append(segment)
                segment = Segment()

            segment.add_line(line)

    def extract_dialogue(self):
        for segment in self.segments:
            lines = segment.get_lines()
            n = len(lines) - 1
            i = 0

            while i < n:
                if lines[i].isupper() and not is_empty(lines[i + 1]) \
                        and self.EXCLAMATION_POINT not in lines[i]:
                    character = lines[i]
                    i += 1
                    dialogue = ""

                    while i < n and not is_empty(lines[i]):
                        dialogue += lines[i] + self.NEWLINE
                        i += 1

                    segment.add_dialogue(character, dialogue)

                i += 1

    def get_segments(self):
        return self.segments



