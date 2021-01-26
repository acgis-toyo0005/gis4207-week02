#-------------------------------------------------------------------------------
# Name:        md5_for_files.py
#
# Purpose:     Calculate MD5 sums of a set of files and find duplicates
#
# Author:      Takashi Toyooka
#
# Created:     24/01/2021
#-------------------------------------------------------------------------------
import os, sys
import csv
import checksum_calculator as cc

def process_files(top_folder, out_filename):
    """Calculate MD5 of files under top_folder and write to out_filename

    Returns the number of duplicate files
    """
    # Set for tracking MD5 and the count of duplicates
    md5_set = set()
    dupe_count = 0

    # Open the output file and write the header row
    with open(out_filename, 'w', newline='') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(["Filename", "MD5"])

        # Walk the files under top_folder
        for root,dirs,filenames in os.walk(top_folder):
            for f in filenames:
                filepath = os.path.join(root,f)

                # Calculate MD5 and check for duplicate
                md5 = cc.get_md5_checksum(filepath)
                if (md5 in md5_set):
                    dupe_count += 1
                else:
                    md5_set.add(md5)

                # Write to the output CSV file
                out_csv.writerow([filepath, md5])

    return dupe_count

def main():
    # Check the number of arguments and print usage if wrong
    if (len(sys.argv) != 3):
        print("Usage: md5_for_files.py top_folder out_csv")
        exit(-1)

    # Check that the input folder exists
    if (os.path.exists(sys.argv[1])):
        top_folder = sys.argv[1]
    else:
        print(f"Input folder {sys.argv[1]} does not exist.")
        exit(-1)

    # Grab the output CSV filename
    out_filename = sys.argv[2]

    # Process the files, generate out_filename, get duplicate count
    dupe_count = process_files(top_folder, out_filename)

    # Print useful final output
    print(f"MD5 values for files under {top_folder}")
    print(f"have been written to {out_filename}.")
    print(f"{dupe_count} duplicates found.")

if __name__ == '__main__':
    main()