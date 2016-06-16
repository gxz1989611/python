#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
输入count,生成指定count数量的coupon
"""
import uuid


def generate(count):
    if not isinstance(count, int) or count < 0:
        print "请输入大于零的数字"
    else:
        lst = []
        for i in range(count):
            lst.append(str(uuid.uuid1()))
        return lst


if __name__ == '__main__':
    generate(10)
