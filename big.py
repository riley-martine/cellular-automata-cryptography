#!/usr/bin/env python3

from rules import RuleList
from functions import get_rows
import random
import os

os.chdir('genfiles')
for rule in (30, 90, 106, 110, 6, 25, 38, 57, 62, 39, 22, 150, 45, 73, 225, 60, 105):
    rule_dict = RuleList(rule).rules

    for start in range(5):
        first_row = [str(random.randint(0,1)) for k in range(500)]
        rows = get_rows(first_row, rule_dict, 1000)
        with open("rows."+str(rule)+'.'+str(start), 'w') as row_file:
            for row in rows:
                row_file.write(row)
                row_file.write("\n")

        first_row2 = first_row[:250] + list(str((int(first_row[250]) + 1) % 2)) + first_row[251:]
        rows2 = get_rows(first_row2, rule_dict, 1000)
        with open("rows2."+str(rule)+'.'+str(start), 'w') as row2_file:
            for row in rows2:
                row2_file.write(row + '\n')

        errors = []
        for i in range(len(rows)):
            current_row = rows[i]
            current_row2 = rows2[i]

            error_row = ''
            for k in range(len(current_row)):
               error_row += str((int(current_row[k] != current_row2[k])))
            errors.append(error_row)



        with open("errors"+str(rule)+'.'+str(start), 'w') as error_file:
            for error in errors:
                error_file.write(error + '\n')
                
            
