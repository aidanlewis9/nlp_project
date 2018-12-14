from stories.story_controller import StoryController


if __name__ == "__main__":
    story_controller = StoryController()

    story_controller.run_character_matching()
    story_controller.run_scene_matching()
    story_controller.run_ner_matching()

