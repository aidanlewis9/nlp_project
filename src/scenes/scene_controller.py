from itertools import filterfalse


class SceneController:
    def __init__(self):
        self.THRESHOLD = 5

        self.scenes = list()

    def add(self, scene):
        self.scenes.append(scene)

    def clean(self):
        self.scenes[:] = filterfalse(lambda scene: scene.is_necessary(), self.scenes)
