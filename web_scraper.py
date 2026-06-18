import requests
from bs4 import BeautifulSoup
from serpapi import GoogleSearch

def get_url(sentence):
    """
    Fetches the most relevant search result URL using SerpAPI.
    :param sentence: Sentence to search
    :return: URL of the first search result or None
    """
    params = {
        "q": sentence,
        "api_key": "8749651bdce192f0ab6c48e79920bb5fac7036f9388936b5559264f937499aed",
        "num": 10  # Get only the first result
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    
    try:
        return results["organic_results"][0]["link"]
    except (KeyError, IndexError):
        return None

def get_text_from_url(url):
    """
    Extracts text content from a given URL.
    :param url: Webpage URL
    :return: Extracted text content
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return ' '.join([p.text for p in soup.find_all('p')])