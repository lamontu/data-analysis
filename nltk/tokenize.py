# _*_ coding: utf-8 _*_

import re
import nltk

emoticons_str = """
    (?:
        [:=;]  # eyes
        [oO\-]?  # nose
        [D\)\]\(\[/\\OpP]  # mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @somebody
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # topics
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',
    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # number
    r"(?:[a-z][a-z'\-_]+[a-z])",  # word containing "'", "-", "_"
    r'(?:[\w_]+)',  # other
    r'(?:\S)'  # other
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

tweet = 'RT @angelababy: love you baby! :D http://ah.love #168cm'
print(preprocess(tweet))
