from parse_movies import ParseMovies


if __name__ == "__main__":
    pm = ParseMovies()

    for m in pm.get_movies():
        for segment in m.get_script().get_segments():
            print(segment)
            print("\n\n\n------------------------------------------------------\n\n\n")

        print(len(m.get_script().get_segments()))

        break
