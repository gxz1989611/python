#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

current_path = os.path.split(os.path.abspath(__file__))[0]
sample_file = os.path.join(current_path, 'sample.txt')

word_count = 0

with open(sample_file, 'r') as f:
    for line in f.readlines():
        word_count += len(line.split())

print 'sample.txt word count: %i' % word_count
