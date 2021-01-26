#-------------------------------------------------------------------------------
# Name:        fix_haiti_file_cli.py
#
# Purpose:     Provide a command-line interface to fix_haiti_file.py
#
# Author:      Takashi Toyooka
#
# Created:     19/01/2021
#-------------------------------------------------------------------------------
import os, sys

import fix_haiti_file as fhf

def main():
    """Main command line routine for fix_haiti_file.py"""
    # Check number of arguments, print usage if wrong
    if (len(sys.argv) != 3):
        print("Usage: fix_haiti_file_cli.py in_csv out_fixed_csv")
        exit(-1)

    # Check that the input file exists
    if (os.path.exists(sys.argv[1])):
        fhf.in_csv = sys.argv[1]
    else:
        print(f"Input file {sys.argv[1]} does not exist.")
        exit(-1)

    # Output file
    fhf.out_fixed_csv = sys.argv[2]

    # Fix the CSV file
    fhf.process_file()

if __name__ == '__main__':
    main()
