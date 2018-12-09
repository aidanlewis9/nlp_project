from story_controller import StoryController


if __name__ == "__main__":
    stories = StoryController()

    for story in stories.stories:
        print(story)
