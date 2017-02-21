# _*_ coding: utf-8 _*_

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.classify import NaiveBayesClassifier


def preprocess(s):
    tokenized_words = word_tokenize(s)
    filtered_words = [word for word in tokenized_words
                      if word not in stopwords.words('english')] 
    return {word: True for word in filtered_words}


pos_sentences = []
pos_data = []
with open('rt-polaritydata/rt-polarity.pos', encoding='latin-1') as f:
    for line in f:
        pos_sentences.append(line)
        pos_data.append([preprocess(line), 'pos'])

neg_sentences = []
neg_data = []
with open('rt-polaritydata/rt-polarity.neg', encoding='latin-1') as f:
    for line in f:
        neg_sentences.append(line)
        neg_data.append([preprocess(line), 'neg'])


training_data = pos_data[:4000] + neg_data[:4000]
testing_data = pos_data[4000:] + neg_data[4000:]

model = NaiveBayesClassifier.train(training_data)

print(model.classify(preprocess('this is a good movie')))
print(model.classify(preprocess('this is a bad movie')))
print(model.classify(preprocess('this is an amazing movie')))
print(model.classify(preprocess('this is a simple movie')))
print(model.classify(preprocess('it is very difficult to understand this movie')))

print("## Test pos_sentences:")
for sentence in pos_sentences[5000:5010]:
    print(model.classify(preprocess(sentence)))

print("## Test neg_sentences:")
for sentence in neg_sentences[5000:5010]:
    print(model.classify(preprocess(sentence)))
