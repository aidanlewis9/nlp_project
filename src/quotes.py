from character import Character

import json

CHARACTER_DATA_FILE = "/book.id.book"
PARENT_DIR = "../data/character/"
READ = 'r'


def get_path(current_dir):
    return PARENT_DIR + current_dir + CHARACTER_DATA_FILE


def read_json(story_name):
    characters = list()

    with open(get_path(story_name), 'r') as f:
        data = json.load(f)

        for character in data['characters']:
            new_character = Character(character['names'], character['speaking'])

            if new_character.is_relevant():
                characters.append(new_character)

    return characters


if __name__ == "__main__":
    story_name = "Jurassic_Park"
    read_json(story_name)
