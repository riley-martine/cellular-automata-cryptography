#!/usr/bin/env python3
"""prints a bunch of random triangles."""

import time
import random
import os
from cellautocommon import get_rows

def print_automaton(first_row, rule):
    """Print largest 1D automaton that will fit onscreen."""
    terminal_rows, terminal_columns = os.popen('stty size', 'r').read().split()
    max_height = (int(terminal_rows) - 1) # Current line
    max_width = (int(terminal_columns) - len(first_row))
    number_of_rows = int(min(((max_width - len(first_row)) / 2), max_height))

    rows = get_rows(first_row=first_row, rule=rule, number_of_rows=number_of_rows, pad_rows=True)

    # Make easier to view
    for row in rows:
        print(row.replace('1', '█').replace('0', '░'))

if __name__ == "__main__":
    for _ in range(10000):
        num = random.randint(0, 255)
        RULE = random.randint(0, 255)
        bin_row = format(num, '08b')
        print_automaton(first_row=bin_row, rule=RULE)
        time.sleep(1)
