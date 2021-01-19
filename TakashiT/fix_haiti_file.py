# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        fix_haiti_file.py
#
# Purpose:     Fix admin_codes in Haiti data files.
#
# Author:      Your name(s)
#
# Created:     dd/mm/yyyy
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
    # TODO:  Add docstring

    # TODO:  Add code to read in_csv, pass admin code to _fix_code,
    #        and write fixed admin code and remaining columns to the 
    #        out_fixed_csv
    pass


# Prefixing a function with one underscore is a convention that lets 
# programmers know that this function is used internally in the 
# module.  It is not meant to be called from 
def _fix_code(admin_code):
    """Returns code with 5th character removed.  For example,
    given HT12345-01, return "HT1245-01

    Args:
        admin_code (str): Haitian administration district code

    Returns:
        str: admin_code with 5th character removed
    """
    # Add code to fix the admin_code and return the fixed code
    pass

























