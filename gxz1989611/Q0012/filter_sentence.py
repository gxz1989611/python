#!/bin/usr/env python
# -*- coding: utf-8 -*-

import os
import string

sentence = raw_input('输入句子用以审查过滤:')
sentence = string.strip(sentence)
original_sentence = sentence
if len(sentence) > 0:
    current_path = os.path.split(os.path.realpath(__file__))[0]
    filtered_file = os.path.join(current_path, 'filtered_words.txt')
    file = open(filtered_file, 'r')
    lines = file.readlines()
    flag = False
    for line in lines:
        line = line.replace('\n', '')
        if sentence.find(line) != -1:
            sentence = str(sentence).replace(line, '*'*len(line.decode('utf-8')))
    print 'original sentence: %s' % original_sentence
    print 'sensor sentence: %s' % sentence

