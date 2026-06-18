import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

def get_sentences(text):
    """
    Tokenizes text into sentences.
    :param text: Input text
    :return: List of sentences
    """
    return sent_tokenize(text)