#!/bin/usr/env python
# -*- coding: utf-8 -*-

import os
import string

user_input = raw_input('输入关键词用以审查:')
user_input = string.strip(user_input)
if len(user_input) > 0:
    current_path = os.path.split(os.path.realpath(__file__))[0]
    filtered_file = os.path.join(current_path, 'filtered_words.txt')
    file = open(filtered_file, 'r')
    lines = file.readlines()
    flag = False
    for line in lines:
        if line.find(user_input) != -1:
            flag = True
            break
    if flag:
        print 'Freedom'
    else:
        print 'Human Rights'


