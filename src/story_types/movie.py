from scenes.movie_scene import MovieScene
from story_types.story_type import StoryType
from utilities.file import read_file
from utilities.string import format_character, format_quote, match, is_empty


class Movie(StoryType):
    def __init__(self, path, regex):
        self.PATH_SUFFIX = "movie.txt"
        self.EMPTY_STRING = ""
        self.EXCLAMATION_POINT = '!'
        self.NEWLINE = '\n'
        self.QUOTE = '"'
        self.READ = 'r'

        StoryType.__init__(self, regex)
        self.path = path + self.PATH_SUFFIX
        self.size = 0

        self.create_scenes()
        self.extract_dialogue()

        self.sc.clean()
        self.cc.clean()

    def size(self):
        return len(open(self.path, self.READ).read())

    def create_scenes(self):
        scene = MovieScene()

        for line in read_file(self.path):
            if match(self.regex, line):
                self.sc.add(scene)
                scene = MovieScene()

            scene.add_line(line)
            self.size += len(line)

    def extract_dialogue(self):
        for scene in self.sc.scenes:
            lines = scene.lines
            n = len(lines) - 1
            i = 0

            while i < n:
                if lines[i].isupper() and not is_empty(lines[i + 1]) \
                        and self.EXCLAMATION_POINT not in lines[i]:
                    character = format_character(lines[i])
                    i += 1
                    quote = ""

                    while i < n and not is_empty(lines[i]):
                        quote += lines[i] + self.NEWLINE
                        i += 1

                    quote = format_quote(quote)

                    scene.add_dialogue(character, quote)
                    self.cc.add_quote(character, quote)

                i += 1



