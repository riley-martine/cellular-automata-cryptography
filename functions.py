#!/usr/bin/env python3

from collections import deque
from itertools import islice

def get_next_row(row, rule_dict):
    """prec: collections.deque composed of 1s and 0s
    postc: returns collections.deque with rules applied"""
    scan_row = deque(row) #scan every group of 3, zer0 padded

    #so we can do a [-2:0]
    scan_row.extendleft([0, 0])
    scan_row.extend([0, 0])

    next_row = deque()
    next_row_length = len(row) + 2

    for pos in range(next_row_length):
        local_three = ''.join(str(i) for i in list(islice(scan_row, pos, pos + 3)))
        next_row.append(rule_dict[local_three.ljust(3, '0')])
    return next_row

def get_rows(first_row, rule_dict, number_of_rows):
    row = first_row
    rows = [row]

    for _ in range(number_of_rows):
        row = get_next_row(row, rule_dict)
        rows.append(row)

    max_length = len(rows[-1])
    for index, row in enumerate(rows):
        rows[index] = ''.join(str(item) for item in row)

    rows = ['{row:0^{max_length}}'.format(row=row, max_length=max_length) for row in rows]

    return deque(rows)
    
def string_to_bin(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    as_int = [alphabet.index(char) for char in string]
    as_bin = ["{0:08b}".format(integer) for integer in as_int]
    return ''.join(as_bin)
