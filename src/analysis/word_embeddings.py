from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_cosine_similarity(documents):
    # print(documents)
    # print(type(documents[0]), type(documents[1]))
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    # print(tfidf_matrix)
    # cos_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)[0][-1]
    cos_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)

    # print(cos_sim)
    return cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)[0][-1]
