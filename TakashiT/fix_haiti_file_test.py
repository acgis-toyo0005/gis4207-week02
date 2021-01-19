# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        Fix_Haiti_File_Tests.py
#
# Author:      Takashi Toyooka
#
# Created:     19/01/2021
#-------------------------------------------------------------------------------

import os
import sys
import csv
import pytest
import fix_haiti_file as fhf

def test_fix_code_valid_code():
    """Given HT12345-01, expecting HT1245-01"""
    input = "HT12345-01"
    expected = input
    actual = fhf._fix_code(input)
    assert actual == expected

def test_fix_code_invalid_code():
    """Given HT12245-01, expecting HT1245-01"""
    input = "HT12245-01"
    expected = "HT1245-01"
    actual = fhf._fix_code(input)
    assert actual == expected

def test_process_file():
    """"Haiti_Admin_Names.csv contains ADMIN_CODES in the first column
        Haiti_Admin_Names_fixed.csv contains a fixed version. """
    pass # TODO
