#!/usr/bin/env python
"""For testing block elementing of data."""

import os
import rules
from collections import deque
from functions import get_rows


def blockify(rows):
    """Takes a list of strings of 1s and 0s and returns blocked version."""

    # Pad to height/len divisible by 4
    columns_to_pad = len(rows[0]) % 4
    rows_to_pad = len(rows) % 4

    for _ in range(columns_to_pad):
        for i in range(len(rows)):
            rows[i] += '0'

    for _ in range(rows_to_pad):
        rows.extendleft(['0' * len(rows[0])])

    rows = list(rows)  # for easier slicing

    # Grab each four square
    blocked_rows = []

    for i in range(0, len(rows), 2):  # For every other row
        row = rows[i]
        add_row = ''
        for n in range(0, len(row), 2):
            add_row += (rules.BLOCK_RULE_LIST[(rows[i]
                                               [n:n + 2], rows[i + 1][n:n + 2])])

        blocked_rows.append(add_row)

    return blocked_rows


def print_automata(first_row, rule_dict, max_height, max_width):
    number_of_rows = int(min(((max_width - len(first_row)) / 2), max_height))
    rows = get_rows(first_row, rule_dict, number_of_rows)

    # Make readable
    rows = blockify(rows)
    for row in rows:
        print(row)


terminal_rows, terminal_columns = os.popen('stty size', 'r').read().split()
# terminal_rows = (int(terminal_rows) // 4) * 4
# terminal_columns = (int(terminal_columns) // 4) * 4
# print(terminal_rows)


RULES = rules.RuleList(30).rules
print_automata(deque(list('11010011100010100101101')), RULES, (int(terminal_rows) - 16)
               * 4, (int(terminal_columns) - 16) * 4)
