# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        fix_haiti_file.py
#
# Purpose:     Fix admin_codes in Haiti data files.
#
# Author:      Takashi Toyooka
#
# Created:     19/01/2021
#-------------------------------------------------------------------------------

import csv

# in_csv = file where a column contains a admin_code that needs fixing.
#          That is, the 5th character in admin_code needs to be removed.
#
in_csv = None

# out_fixed_csv = file with same contents as in_csv with fixed admin_code
#
out_fixed_csv = None


def process_file():
    """Read input csv file, fix the admin code, and write to another file
    
    Uses in_csv and out_fixed_csv module variables to get filenames
    """

    with open(in_csv) as in_file:
        in_recs = csv.reader(in_file)
        in_line = 0

        with open(out_fixed_csv, 'w') as out_file:
            out_recs = csv.writer(out_file)

            try:
                # Expect the first line to be header, just copy it
                rec = next(in_recs)
                in_line += 1
                out_recs.writerow(rec)

                while True:
                    rec = next(in_recs)
                    in_line += 1
                    rec[0] = _fix_code(rec[0])
                    out_recs.writerow(rec)
            except StopIteration:
                # Presumed end of file
                pass

# Prefixing a function with one underscore is a convention that lets 
# programmers know that this function is used internally in the 
# module.  It is not meant to be called from outside the module.
def _fix_code(admin_code):
    """Returns code with 5th character removed.  For example,
    given HT12345-01, return "HT1245-01

    Args:
        admin_code (str): Haitian administration district code

    Returns:
        str: admin_code with 5th character removed
    """
    return admin_code[0:4] + admin_code[5:]
