#!/usr/bin/env python3


def get_next_row(row, rule_dict):
    """prec: collections.deque composed of 1s and 0s
    postc: returns collections.deque with rules applied"""
    scan_row = [0, 0]
    scan_row.extend(row)
    scan_row.extend([0,0])  # scan every group of 3, zer0 padded


    next_row = list()
    next_row_length = len(row) + 2

    for pos in range(next_row_length):
        local_three = ''.join(str(i) for i in scan_row[pos:pos + 3])
        next_row.append(rule_dict[local_three.ljust(3, '0')])
    return next_row


def get_rows(first_row, rule_dict, number_of_rows):
    row = first_row
    rows = [row]

    for _ in range(number_of_rows):
        row = get_next_row(row, rule_dict)
        rows.append(row)

    for index, row in enumerate(rows):
        rows[index] = ''.join(str(item) for item in row)

    # Pad with zeros. Disabled to save disk space.
    # max_length = len(rows[-1])
    # rows = ['{row:0^{max_length}}'.format(
    #     row=row, max_length=max_length) for row in rows]

    return list(rows)


def string_to_bin(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    as_int = [alphabet.index(char) for char in string]
    as_bin = ["{0:08b}".format(integer) for integer in as_int]
    return ''.join(as_bin)
