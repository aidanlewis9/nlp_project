from stories import Stories


if __name__ == "__main__":
    stories = Stories()

    for story in stories.get_stories():
        print(story)
