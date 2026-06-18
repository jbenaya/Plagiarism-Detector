from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_similarity(text1, text2):
    """
    Computes cosine similarity between two texts.
    :param text1: First text
    :param text2: Second text
    :return: Similarity score
    """
    vectorizer = CountVectorizer().fit_transform([text1, text2])
    similarity_matrix = cosine_similarity(vectorizer)
    return similarity_matrix[0][1]

def compute_similarities(texts, filenames):
    """
    Computes similarity scores for multiple texts.
    :param texts: List of text contents
    :param filenames: Corresponding list of filenames
    :return: List of tuples (File 1, File 2, Similarity Score)
    """
    similarities = []
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            similarity = get_similarity(texts[i], texts[j])
            similarities.append((filenames[i], filenames[j], similarity))
    return similarities