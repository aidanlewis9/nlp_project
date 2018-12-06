from src.parseMovies.movie import Movie


class ParseMovies:
    def __init__(self):
        self.movie_regex_dict = {
            "Frankenstein": "((EXT|INT) -)", "Jurassic Park": "((EXT|INT|INT/EXT) )",
            "No Country for Old Men": "((EXT.|INT.|EXT./INT.) )", "Schindler's List": ".*(EXT.|INT.|EXT/INT.) ",
            "The Bourne Supremacy": "((EXT.|INT.|EXT./INT.|INT./EXT.) )", "The Shining": "((EXT.|INT.) )",
            "The Talented Mr. Ripley": "((EXT.|INT.|PROLOGUE: INT.|INT/EXTERIOR.))", "The Wizard of Oz": ".*(Int.|Ext.) "
        }

        self.movies = list()
        self.init_movies()

    def init_movies(self):
        for movie_title, regex in self.movie_regex_dict.items():
            movie = Movie(movie_title, regex)
            self.movies.append(movie)

    def get_movies(self):
        return self.movies

