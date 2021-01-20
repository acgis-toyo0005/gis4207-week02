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

def test_fix_code_typical_code():
    """Given HT12345-01, expecting HT1245-01"""
    input = "HT12345-01"
    expected = "HT1245-01"
    actual = fhf._fix_code(input)
    assert actual == expected

def test_process_file():
    """"Haiti_Admin_Names.csv contains ADMIN_CODES in the first column
        Haiti_Admin_Names_fixed.csv contains a fixed version.
        Compare them against those in Haiti_LandUse_And_Pop.csv"""
    with open("../../../data/Haiti/Haiti_LandUse_And_Pop.csv") as exp_file:
        exp_csv = csv.reader(exp_file)
        exp_codes = set()
        first = True
        for rec in exp_csv:
            if first:
                first = False
                continue
            exp_codes.add(rec[0])

    fhf.in_csv = "../../../data/Haiti/Haiti_Admin_Names.csv"
    fhf.out_fixed_csv = "test_Haiti_Admin_Names_Fixed.csv"
    fhf.process_file()

    with open(fhf.out_fixed_csv) as act_file:
        act_csv = csv.reader(act_file)
        act_codes = set()
        first = True
        for rec in act_csv:
            if first:
                first = False
                continue
            act_codes.add(rec[0])

    assert act_codes == exp_codes