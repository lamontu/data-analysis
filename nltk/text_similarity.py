# _*_ coding: utf-8 _*_

import nltk
from nltk import FreqDist
from scipy import spatial


corpus = 'this is my sentence  this is my life  this is the day'
tokens = nltk.word_tokenize(corpus)
print("tokens:")
print(tokens)

fdist = FreqDist(tokens)

standard_freq_vector = fdist.most_common(50)
size = len(standard_freq_vector)
print("standard_freq_vector:")
print(standard_freq_vector)


def position_lookup(v):
    res = {}
    counter = 0
    for word in v:
        res[word[0]] = counter
        counter += 1
    return res


standard_position_dict = position_lookup(standard_freq_vector)
print("standard_position_dict:")
print(standard_position_dict)


def freq_vector(sentence, size, standard_position_dict):
    freq_vector = [0] * size
    tokens = nltk.word_tokenize(sentence)
    for word in tokens:
        try:
            freq_vector[standard_position_dict[word]] += 1
        except KeyError:
            continue
    return freq_vector


sentence1 = 'this is cool'
sentence2 = 'this is my life'

freq_vector1 = freq_vector(sentence1, size, standard_position_dict)
freq_vector2 = freq_vector(sentence2, size, standard_position_dict)

dist = spatial.distance.cosine(freq_vector1, freq_vector2)
print("distance:")
print(dist)
simi = 1 - dist
print("similarity:")
print(simi)
