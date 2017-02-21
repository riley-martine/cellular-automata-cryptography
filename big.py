#!/usr/bin/env python3

from rules import RuleList
from functions import get_rows


rule_dict = RuleList(90).rules

first_row = list('1'*100)
rows = get_rows(first_row, rule_dict, 5000)
with open("rows", 'w') as row_file:
    for row in rows:
        row_file.write(row)
        row_file.write("\n")
