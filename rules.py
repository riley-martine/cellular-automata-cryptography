#!/usr/bin/env python
"""class for 1D cell auto rules"""

class RuleList(object):
    """docstring for RuleList"""
    def __init__(self, rule): # rules are in the form of a number from 0-255
        b_rule_string = format(rule, '08b')
        b_rule_list = [char for char in b_rule_string]

        self.rules = {
            "111": b_rule_list[0],
            "110": b_rule_list[1],
            "101": b_rule_list[2],
            "100": b_rule_list[3],
            "011": b_rule_list[4],
            "010": b_rule_list[5],
            "001": b_rule_list[6],
            "000": b_rule_list[7]
        }

rl = RuleList(30)
