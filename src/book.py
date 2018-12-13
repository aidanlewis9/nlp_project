from utilities.file import read_file
from utilities.string import match
from scene import Scene
from parser import Parser
import math


class Book:
    def __init__(self, path, regex, title, num_script_scenes):
        self.PATH_SUFFIX = "book.txt"
        self.EMPTY_STRING = ""
        self.NEWLINE = '\n'
        self.QUOTE = '"'

        self.scenes = list()
        self.path = path + self.PATH_SUFFIX
        self.regex = regex
        self.parser = Parser(title)
        self.num_script_scenes = num_script_scenes
        self.sub_scenes = list() # this holds the more finely split chapter scenes

        self.all_scenes = list()
        self.valid_scenes = list()

        self.get_scenes()
        self.divide_book_scenes()

    def get_scenes(self):
        scene = Scene()

        for line in read_file(self.path):
            if match(self.regex, line):
                scene.add_sentences(scene.sentence_string)
                self.all_scenes.append(scene)
                scene = Scene()
            self.parser.parse_book(line, scene)


    def divide_book_scenes(self):
        if len(self.all_scenes) > self.num_script_scenes:
            self.handle_more_chapters_than_scenes()
        elif len(self.all_scenes) == self.num_script_scenes:
            self.sub_scenes = self.all_scenes
        else:
            self.handle_more_scenes_than_chapters()

        # for i, scene in enumerate(self.sub_scenes):
        #     print("SUBSCENE", i, "------------------------------" )
        #     for sentence in scene.sentences:
        #         print(sentence)

    def handle_more_scenes_than_chapters(self):
        sentence_counts = dict() # scene: count
        sentence_props = dict() # scene : proportion
        total_sentences = 0

        # store the number of sentences in each scene and the total number of sentences
        for scene in self.all_scenes:
            if len(scene.sentences) > 0:
                sentence_counts[scene] = len(scene.sentences)
                total_sentences += len(scene.sentences)

        # determine the proportion of sentences in each scene
        for scene, count in sentence_counts.items():
            sentence_props[scene] = count / float(total_sentences)

        # iterate through each scene (chapter) and its proportion
        switch = True
        total_scenes = 0
        for scene, prop in sentence_props.items():
            # determine how many scenes it needs to be split into
            num_scenes_to_split = math.floor(prop * self.num_script_scenes) if switch == True else math.ceil(prop * self.num_script_scenes)
            total_scenes += num_scenes_to_split
            if total_scenes - self.num_script_scenes == 1:
                num_scenes_to_split -= 1
            elif self.num_script_scenes - total_scenes == 1:
                num_scenes_to_split += 1

            # and how many sentences should be in each scene
            if num_scenes_to_split != 0:
                num_sentences_per_scene = math.ceil(len(scene.sentences) / num_scenes_to_split)
            else:
                self.sub_scenes[-1].sentences.append(scene.sentences)
                continue
            switch = not switch
            last_sent_num = 0

            # create each new scene and add the appropriate sentences to it
            for i in range(num_scenes_to_split):
                new_scene = Scene()
                new_scene.sentences = scene.sentences[last_sent_num:last_sent_num + num_sentences_per_scene]
                self.sub_scenes.append(new_scene)
                last_sent_num += num_sentences_per_scene

    def handle_more_chapters_than_scenes(self):
        self.sub_scenes = self.all_scenes
        total_scenes = len(self.sub_scenes)
        sentence_counts = dict()
        for scene in self.sub_scenes:
            sentence_counts[scene] = len(scene.sentences)

        for i in range(total_scenes - self.num_script_scenes):
            chapters_sorted_by_length = sorted(sentence_counts.items(), key=lambda kv: kv[1])
            scene_to_combine = chapters_sorted_by_length[0]
            self.combine_scenes(scene_to_combine, sentence_counts)

    def combine_scenes(self, scene_to_combine, sentence_counts):
        for i, scene in enumerate(self.sub_scenes):
            if scene == scene_to_combine[0] and i != 0:
                self.sub_scenes[i-1].add_to_scene(scene)
                sentence_counts[self.sub_scenes[i-1]] += len(scene.sentences)
                del sentence_counts[scene_to_combine[0]]
                del self.sub_scenes[i]
                break


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
