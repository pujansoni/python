"""Retreive and print words from a URL
Usage:
    python ex43.py <URL>
"""

import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from a URL

    Args:
        url: The URL of a UTF-8 document.

    Returns:
        A list of strings containing the words from
        the document.
    """
    story1 = urlopen(url)
    story_words1 = []
    for line in story1:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words1.append(word)
    story1.close()
    return story_words1

def print_items(items):
    """Print items one per line

    Args:
        An iterable series of printable items
    """
    for item in items:
        print(item)

def main(url):
    """Print each words from a text document from a url

    Args:
        url: The URL of a UTF-8 document.

    """
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    main(sys.argv[1])