from analysis.character_matching import CharacterMatching
from analysis.ner_matching import NERMatching
from analysis.scene_matching import SceneMatching 
from stories.story import Story


class StoryController:
    def __init__(self):
        self.titles = [
            # "Frankenstein",
            "Jurassic Park",
            # "No Country for Old Men",
            "Schindler's List",
            "The Bourne Supremacy",
            "The Shining",
            "The Talented Mr. Ripley",
            "The Wizard of Oz"
        ]

        self.movie_regexs = {
            "Frankenstein": "((EXT|INT) -)",
            "Jurassic Park": "((EXT|INT|INT/EXT) )",
            "No Country for Old Men": "((EXT.|INT.|EXT./INT.) )", "Schindler's List": ".*(EXT.|INT.|EXT/INT.) ",
            "The Bourne Supremacy": "((EXT.|INT.|EXT./INT.|INT./EXT.) )", "The Shining": "((EXT.|INT.) )",
            "The Talented Mr. Ripley": "((EXT.|INT.|PROLOGUE: INT.|INT/EXTERIOR.))", "The Wizard of Oz": ".*(Int.|Ext.) "
        }

        self.book_regexs = {
            "Frankenstein": "(Chapter \d)",
            "Jurassic Park": "(.* ITERATION)",
            "No Country for Old Men": "(Chapter$)",
            "Schindler's List": "((PROLOGUE|CHAPTER|EPILOGUE).*)",
            "The Bourne Supremacy": "(([0-9]|[0-9][0-9])$)",
            "The Shining": "(<< [0-9]* >>)",
            "The Talented Mr. Ripley": "(Chapter *)",
            "The Wizard of Oz": "([0-9]*\. *)"
        }

        self.stories = list()
        self.init_stories()

    def init_stories(self):
        for title in self.titles:
            story = Story(title, self.movie_regexs[title], self.book_regexs[title], title)
            self.stories.append(story)

    def run_character_matching(self):
        print("Character Matching")

        for story in self.stories:
            cm = CharacterMatching(story)
            score = cm.run()

            print("Movie: {} - Score: {}".format(story.name, score))

    def run_scene_matching(self):
        print("Scene Matching")

        for story in self.stories:
            sm = SceneMatching(story)
            score = sm.run()

            print("Movie: {} - Score: {}".format(story.name, score))

    def run_ner_matching(self):
        print("NER Matching")

        for story in self.stories:
            nm = NERMatching(story)
            score = nm.run()

            print("Movie: {} - Score: {}".format(story.name, score))
