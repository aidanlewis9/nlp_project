import json
import math
import operator

from characters.character import Character
from scenes.book_scene import BookScene
from story_types.story_type import StoryType
from utilities.file import read_file
from utilities.string import match, format_movie_name, no_whitespace
from utilities.parser import Parser


class Book(StoryType):
    def __init__(self, path, regex, title, num_movie_scenes):
        self.CHARACTER_DATA_FILE = "/book.id.book"
        self.EMPTY_STRING = ""
        self.NEWLINE = '\n'
        self.PARENT_DIR = "../data/character/"
        self.PATH_SUFFIX = "book.txt"
        self.QUOTE = '"'
        self.READ = 'r'
        self.LIMIT = 20

        StoryType.__init__(self, regex)

        self.path = path + self.PATH_SUFFIX
        self.size = 0
        self.parser = Parser(title)
        self.num_movie_scenes = num_movie_scenes
        self.sub_scenes = list()  # this holds the more finely split chapter scenes
        self.all_quotes = dict()

        self.create_scenes()
        self.divide_book_scenes()

        self.read_json(title)

        self.cc.clean()

        self.match_quote_to_scene()

    def create_scenes(self):
        scene = BookScene()

        for line in read_file(self.path):
            if match(self.regex, line):
                scene.add_sentences(scene.sentence_string)
                self.sc.add(scene)

                scene = BookScene()
            self.parser.parse_book(line, scene)

            self.size += len(line)

    def divide_book_scenes(self):
        if len(self.sc.scenes) > self.num_movie_scenes:
            self.handle_more_chapters_than_scenes()
            self.sc.scenes[:] = self.sub_scenes[:]
        else:
            self.handle_more_scenes_than_chapters()
            self.sc.scenes[:] = self.sub_scenes[:]

    def handle_more_scenes_than_chapters(self):
        sentence_counts = dict()  # scene: count
        sentence_props = dict()  # scene : proportion
        total_sentences = 0

        # store the number of sentences in each scene and the total number of sentences
        for scene in self.sc.scenes:
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
            num_scenes_to_split = math.floor(prop * self.num_movie_scenes) if switch == True else math.ceil(prop * self.num_movie_scenes)
            total_scenes += num_scenes_to_split
            if total_scenes - self.num_movie_scenes == 1:
                num_scenes_to_split -= 1
            elif self.num_movie_scenes - total_scenes == 1:
                num_scenes_to_split += 1

            # and how many sentences should be in each scene
            if num_scenes_to_split != 0:
                num_sentences_per_scene = math.ceil(len(scene.sentences) / num_scenes_to_split)
            else:
                # self.sub_scenes[-1].sentences.append(scene.sentences)
                self.sub_scenes[-1].sentences.extend(scene.sentences)
                continue
            switch = not switch
            last_sent_num = 0

            # create each new scene and add the appropriate sentences to it
            for i in range(num_scenes_to_split):
                new_scene = BookScene()
                new_scene.sentences = scene.sentences[last_sent_num:last_sent_num + num_sentences_per_scene]
                self.sub_scenes.append(new_scene)
                last_sent_num += num_sentences_per_scene

    def handle_more_chapters_than_scenes(self):
        self.sub_scenes = self.sc.scenes
        total_scenes = len(self.sub_scenes)
        sentence_counts = dict()
        for scene in self.sub_scenes:
            sentence_counts[scene] = len(scene.sentences)

        for i in range(total_scenes - self.num_movie_scenes):
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

    def get_path(self, current_dir):
        return self.PARENT_DIR + current_dir + self.CHARACTER_DATA_FILE

    def get_character_name(self, names):
        names_dict = {name['n']: name['c'] for name in names}
        return max(names_dict.items(), key=operator.itemgetter(1))[0]

    def read_json(self, story_name):
        with open(self.get_path(format_movie_name(story_name)), self.READ) as f:
            data = json.load(f)

            for character in data['characters']:
                character_name = self.get_character_name(character['names'])
                new_character = Character()

                new_character.add_names(character['names'])
                new_character.add_quotes(character['speaking'])

                self.cc.add_character(character_name, new_character)


    def match_quote_to_scene(self):
        max_key = 100
        quote_count = 0
        bad = 0

        # 20 seems okay

        for character in self.get_characters():
            for quote in self.get_quotes(character):
                key = no_whitespace(quote) if len(no_whitespace(quote)) < self.LIMIT + 1 \
                    else no_whitespace(quote)[:self.LIMIT]

                if len(key) == self.LIMIT and key in self.all_quotes:
                    bad += 1

                self.all_quotes[key] = (character, quote)

                quote_count += 1

                if len(key) < max_key:
                    max_key = len(key)

        used_keys = set()

        for scene in self.get_scenes():

            text = no_whitespace(scene.get_text())

            used = [False for _ in range(len(text))]

            for word_length in range(self.LIMIT, 0, -1):
                for character_index in range(0, len(text) - word_length):
                    start = character_index
                    end = character_index + word_length

                    word = text[start:end]

                    been_used = False

                    if word in self.all_quotes:

                        for i in range(start, end):
                            if used[i]:
                                been_used = True
                                break

                        if not been_used:
                            for i in range(start, end):
                                used[i] = True

                            character, quote = self.all_quotes[word]
                            scene.add_dialogue(character, quote)
                            used_keys.add(word)