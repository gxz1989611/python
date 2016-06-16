#!/bin/usr/env python
# -*- coding: utf-8 -*-
"""
保存lst到redis
"""

import redis

import Q0001.generate_coupon as gc


def saveToRedis(lst):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    for idx, coupon in enumerate(lst):
        r.set('coupon_' + str(idx), coupon)


if __name__ == '__main__':
    lst = gc.generate(10)
    if len(lst) > 0:
        saveToRedis(lst)
