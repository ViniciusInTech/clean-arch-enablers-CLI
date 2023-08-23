import re


def split_words(string):
    words = re.findall(r'[A-Z]?[a-z]+|[A-Z]+|[a-zA-Z0-9]+', string)
    return [word.lower() for word in words]
