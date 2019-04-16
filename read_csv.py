# -*- coding:utf-8 -*-
"""
Author:duan
Date:2019/4/15 19:55
"""
import csv
import os

import xlrd

filename = 'data.xlsx'


def read_file(file):
    type = os.path.splitext(file)[1]
    xy = []
    if type == '.xlsx':
        data = xlrd.open_workbook(filename)
        table = data.sheet_by_index(0)
        for i in range(0, table.ncols):
            temp = {}
            temp[table.col_values(i)[0]] = table.col_values(i)[1:]
            xy.append(temp)
    elif type == 'csv':
        pass
    elif type == 'txt':
        pass
    return xy


if __name__ == '__main__':
    xy = read_file(filename)
    print(xy)
