# coding: utf-8
from chapter6.nlp_utils import get_each_sentences

sentence_list = get_each_sentences("nlp.txt")
for sentence in sentence_list:
    print(sentence)
