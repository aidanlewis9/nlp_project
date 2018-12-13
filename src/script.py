from scene import Scene
from utilities.file import read_file
from utilities.string import match, is_empty


class Script:
    def __init__(self, path, regex):
        self.PATH_SUFFIX = "script.txt"
        self.EMPTY_STRING = ""
        self.EXCLAMATION_POINT = '!'
        self.NEWLINE = '\n'
        self.QUOTE = '"'

        self.regex = regex
        self.path = path + self.PATH_SUFFIX

        self.all_scenes = list()
        self.valid_scenes = list()

        self.get_scenes()
        self.extract_dialogue()

    def get_scenes(self):
        scene = Scene()

        for line in read_file(self.path):
            if match(self.regex, line):
                self.all_scenes.append(scene)
                scene = Scene()

            scene.add_line(line)

    def extract_dialogue(self):
        for scene in self.all_scenes:
            lines = scene.lines
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

                    scene.add_dialogue(character, dialogue)

                i += 1

            if scene.is_scene():
                self.valid_scenes.append(scene)



