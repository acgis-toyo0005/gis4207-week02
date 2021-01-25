#-------------------------------------------------------------------------------
# Name:        md5_for_files.py
#
# Purpose:     Testing duplicates finder code
#
# Author:      Takashi Toyooka
#
# Created:     24/01/2021
#-------------------------------------------------------------------------------
import os, csv
import pytest

import md5_for_files as mf

data_dir = "..\\..\\..\\data\\DuplicateData"
# The files in this directory were constructed independently by hand using the
# GNU md5sum tool and a text editor.
expected_output_dir = "TakashiT\\md5_for_files_test_data"

def compare_csv(filename1, filename2):
    with open(filename1) as file1:
        with open(filename2) as file2:
            csv1 = list(csv.reader(file1))
            csv2 = list(csv.reader(file2))
            assert csv1 == csv2

def test_Duplicates():
    top = os.path.join(data_dir, "Duplicates")
    out_csv = "test_dupes.csv"
    exp_csv = os.path.join(expected_output_dir, "expected_dupes.csv")
    mf.process_files(top, out_csv)
    compare_csv(out_csv, exp_csv)

def test_FalseDuplicates():
    top = os.path.join(data_dir, "FalseDuplicates")
    out_csv = "test_falsedupes.csv"
    exp_csv = os.path.join(expected_output_dir, "expected_falsedupes.csv")
    mf.process_files(top, out_csv)
    compare_csv(out_csv, exp_csv)
