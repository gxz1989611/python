#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
保存lst到mysql
"""

import MySQLdb

import Q0001.generate_coupon as gc


def saveToMysql(lst):
    db = MySQLdb.connect(host="localhost", port=3307, user="root", passwd="123123", db="test")
    db.autocommit(True)
    cursor = db.cursor()
    for coupon in lst:
        insertSql = 'insert into coupon (coupon) value("%s")' % coupon
        print insertSql
        cursor.execute(insertSql)

    db.close()


if __name__ == '__main__':
    lst = gc.generate(10)
    if len(lst) > 0:
        saveToMysql(lst)
