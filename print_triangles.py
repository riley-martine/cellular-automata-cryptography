#!/usr/bin/env python3
"""prints a bunch of random triangles."""

from functions import get_rows
import rules

import time
import random
import os


def print_automata(first_row, rule_dict, max_height, max_width):
    number_of_rows = int(min(((max_width - len(first_row)) / 2), max_height))
    rows = get_rows(first_row, rule_dict, number_of_rows)

    # Make readable
    for row in rows:
        print(row.replace('1', '█').replace('0', '░'))

    # print(*rows, sep='\n')

for _ in range(10000):
    terminal_rows, terminal_columns = os.popen('stty size', 'r').read().split()
    num = random.randint(0, 255)
    RULES = rules.RuleList(random.randint(0, 255)).rules
    bin_row = format(num, '08b')
    print_automata(bin_row, RULES, int(terminal_rows), int(terminal_columns))
    time.sleep(1)
