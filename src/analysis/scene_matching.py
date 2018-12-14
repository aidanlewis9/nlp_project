from analysis.word_embeddings import get_cosine_similarity
from heapq import heappop, heappush


class SceneMatching:
    def __init__(self, story):
        self.book_scenes = story.book.get_scenes()
        self.movie_scenes = story.movie.get_scenes()

        self.scene_count = story.book.scene_count() + story.movie.scene_count()
        self.total_length = story.book.size + story.movie.size

    def build_pq(self):
        scores = list()

        for book_index, book_scene in enumerate(self.book_scenes):
            for movie_index, movie_scene in enumerate(self.movie_scenes):

                cos_sim = -1.0 * get_cosine_similarity((movie_scene.get_document(),
                                                        book_scene.get_document()))

                heappush(scores, (cos_sim, (book_index, movie_index)))

        return scores

    def is_empty(self, l):
        return len(l) == 0

    def run(self):
        scores = self.build_pq()

        n = len(self.book_scenes)
        total_score = 0

        visited_books = set()
        visited_movies = set()

        while not (len(visited_books) == n and len(visited_movies) == n):
            if self.is_empty(scores):
                break

            score, [book_index, movie_index] = heappop(scores)

            if book_index not in visited_books and movie_index not in visited_movies:

                book_scene_len = self.book_scenes[book_index].get_length()
                movie_scene_len = self.movie_scenes[movie_index].get_length()

                weight = (movie_scene_len + book_scene_len) / float(self.total_length)

                total_score += (-1.0 * score * weight)

                visited_books.add(book_index)
                visited_movies.add(movie_index)

        return total_score / float(self.scene_count)