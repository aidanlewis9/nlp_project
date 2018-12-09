from story_controller import StoryController


if __name__ == "__main__":
    story_controller = StoryController()

    for story in story_controller.stories:
        print(story)
