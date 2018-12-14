from scenes.scene import Scene


class MovieScene(Scene):
    def __init__(self):
        Scene.__init__(self)

        self.THRESHOLD = 5

        self.text = str()
        self.lines = list()

    def add_line(self, line):
        self.text += line
        self.lines.append(line)

    def is_necessary(self):
        return self.dialogue_count > self.THRESHOLD

    def get_text(self):
        return self.text
