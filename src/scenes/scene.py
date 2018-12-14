class Scene:
    def __init__(self):
        self.dialogue = list()
        self.dialogue_count = 0

    def add_dialogue(self, character, quote):
        self.dialogue.append("{}: {}".format(character, quote))
        self.dialogue_count += 1

    def get_document(self):
        return " ".join(self.dialogue)

    def get_length(self):
        return len(self.get_document())