#!/usr/bin/env python
"""Secret handshake between two parties.
Based on a class 4 1D cellular automata."""

from collections import deque
from itertools import islice
import rules

STARTING_ROW = deque([1])
RULES = rules.RuleList(30).rules

def get_next_row(row):
    """prec: collections.deque composed of 1s and 0s
    postc: returns collections.deque with rules applied"""
    next_row_length = len(row) + 2
    scan_row = deque(row) #scan every group of 3, zer0 padded

    scan_row.extendleft([0, 0])
    scan_row.extend([0, 0])

    next_row = deque()

    #print(scan_row)
    for pos in range(next_row_length):

        #print(''.join(str(i) for i in list(
        #    islice(scan_row,pos,pos+3))).ljust(3,'0'))
        local_three = ''.join(str(i) for i in list(islice(scan_row, pos, pos + 3)))
        next_row.append(RULES[local_three.ljust(3, '0')])

    return next_row


row = deque([1])
rows = [row]
for _ in range(100):
    row = get_next_row(row)
    rows.append(row)

max_length = len(rows[-1])
new_rows = []
for row in rows:
    new_rows.append(''.join(str(item) for item in row).replace('1', '░').replace('0', '█'))

new_rows = ['{row:^{max_length}}'.format(row=row, max_length=max_length) for row in new_rows]
for row in new_rows:
    print(row)
