import re
from collections import Counter
from functools import reduce


def remove_punctuation(text_input):
    res = re.sub(r'[^\w\s]', '', text_input)
    return res.lower()

def word_exist(text_bag):
    grabber = dict(Counter(text_bag))
    boomer = map(lambda x: x, grabber.keys())
    return list(boomer)


def words_count(text_bag):
    grabber = dict(Counter(text_bag))
    boomer = map(lambda x, y: [x, y], grabber.keys(), grabber.values())
    return list(boomer)


def frequency_of_words(bagger,length):
    for item in bagger:
        item[1]=item[1]/length
    return bagger

def vector_space_model_scoring():
    score=0

    return score

