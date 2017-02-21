#!/usr/bin/env python
# coding=utf-8

"""class for 1D cell auto rules"""


class RuleList(object):
    """docstring for RuleList"""

    def __init__(self, rule):  # rules are in the form of a number from 0-255
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


BLOCK_RULE_LIST = {
    ('00', '00'): ' ',
    ('00', '01'): '▗',
    ('00', '10'): '▖',
    ('00', '11'): '▄',
    ('01', '00'): '▝',
    ('01', '01'): '▐',
    ('01', '10'): '▞',
    ('01', '11'): '▟',
    ('10', '00'): '▘',
    ('10', '01'): '▚',
    ('10', '10'): '▌',
    ('10', '11'): '▙',
    ('11', '00'): '▀',
    ('11', '01'): '▜',
    ('11', '10'): '▛',
    ('11', '11'): '█',
}
