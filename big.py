#!/usr/bin/env python3

from rules import RuleList
from functions import get_rows


rule_dict = RuleList(90).rules

first_row = list('1')
rows = get_rows(first_row, rule_dict, 500)
