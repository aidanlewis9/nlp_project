from utilities.file import read_file
from utilities.string import match
from scene import Scene
from parser import Parser


class Book:
    def __init__(self, path, regex, title):
        self.PATH_SUFFIX = "book.txt"
        self.EMPTY_STRING = ""
        self.NEWLINE = '\n'
        self.QUOTE = '"'

        self.scenes = list()
        self.path = path + self.PATH_SUFFIX
        self.regex = regex
        self.parser = Parser(title)

        self.all_scenes = list()
        self.valid_scenes = list()

        self.get_scenes()

    def get_scenes(self):
        scene = Scene()
        for line in read_file(self.path):
            if match(self.regex, line):
                scene.add_sentences(scene.sentence_string)
                self.all_scenes.append(scene)
                scene = Scene()
            self.parser.parse_book(line, scene)

        # for scene in self.all_scenes:
        #     print('------------------------------------------------------')
        #     # print(scene.lines)
        #     print(scene)

    def extract_dialogue(self):
        for scene in self.all_scenes:
            curr_quote = self.EMPTY_STRING
            in_quote = False

            for line in scene.lines:
                for char in line:
                    if char == self.QUOTE and not in_quote:
                        print("START", char)
                        in_quote = True
                    elif char == self.QUOTE and in_quote:
                        print("END")
                        scene.add_dialogue(None, curr_quote)
                        curr_quote = self.EMPTY_STRING
                        in_quote = False

                    if in_quote:
                        print(char)
                        curr_quote += char
                    else:
                        print()

            if scene.is_scene():
                self.valid_scenes.append(scene)
