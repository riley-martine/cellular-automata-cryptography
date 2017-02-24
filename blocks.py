#!/usr/bin/env python
"""Prints largest rule 30 cellular automata terminal will fit."""

import os
from cellautocommon import get_rows


BLOCK_RULE_LIST = {
    ('00', '00'): u' ',
    ('00', '01'): u'▗',
    ('00', '10'): u'▖',
    ('00', '11'): u'▄',
    ('01', '00'): u'▝',
    ('01', '01'): u'▐',
    ('01', '10'): u'▞',
    ('01', '11'): u'▟',
    ('10', '00'): u'▘',
    ('10', '01'): u'▚',
    ('10', '10'): u'▌',
    ('10', '11'): u'▙',
    ('11', '00'): u'▀',
    ('11', '01'): u'▜',
    ('11', '10'): u'▛',
    ('11', '11'): u'█',
}


def blockify(rows):
    """Takes a list of strings of 1s and 0s and returns blocked version."""
    # Pad to height/len divisible by 2
    columns_to_pad = len(rows[0]) % 2
    rows_to_pad = len(rows) % 2

    for _ in range(columns_to_pad):
        for i, row in enumerate(rows):
            rows[i] += '0'

    for _ in range(rows_to_pad):
        rows = ['0' * len(rows[0])].extend(rows)

    # Grab each four square
    blocked_rows = []

    for i in range(0, len(rows), 2):  # For every other row
        row = rows[i]
        add_row = ''
        for j in range(0, len(row), 2):
            add_row += (BLOCK_RULE_LIST[(rows[i]
                                         [j:j + 2], rows[i + 1][j:j + 2])])

        blocked_rows.append(add_row)

    return blocked_rows


def print_automaton(first_row: str, rule: int) -> None:
    """Print 1D automata with first row $first_row, rule $rule.
       Dimensions are determined by the size of the terminal.
       Prints largest that will fit using unicode block characters.
    """
    # Get maximum size
    terminal_rows, terminal_columns = os.popen('stty size', 'r').read().split()
    max_height = (int(terminal_rows) - 2) * 2 # Don't touch these.
    max_width = (int(terminal_columns) - len(first_row)) * 2
    number_of_rows = int(min(((max_width - len(first_row)) / 2), max_height))

    rows = get_rows(first_row=first_row, rule=rule, number_of_rows=number_of_rows, pad_rows=True)

    # Make readable
    rows = blockify(rows)
    for row in rows:
        print(row)

if __name__ == "__main__":
    print_automaton(first_row='1', rule=30)
