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
    md5_set = set()
    dupe_count = 0
    with open(out_filename, 'w', newline='') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(["Filename", "MD5"])
        for root,dirs,filenames in os.walk(top_folder):
            for f in filenames:
                filepath = os.path.join(root,f)
                md5 = cc.get_md5_checksum(filepath)
                if (md5 in md5_set):
                    dupe_count += 1
                else:
                    md5_set.add(md5)
                out_csv.writerow([filepath, md5])
    return dupe_count

def main():
    if (len(sys.argv) != 3):
        print("Usage: md5_for_files.py top_folder out_csv")
        exit(-1)

    if (os.path.exists(sys.argv[1])):
        top_folder = sys.argv[1]
    else:
        print(f"Input folder {sys.argv[1]} does not exist.")
        exit(-1)

    out_filename = sys.argv[2]

    process_files(top_folder, out_filename)

    print(f"MD5 values for files under {top_folder}")
    print(f"have been written to {out_filename}.")
    print(f"{dupe_count} duplicates found.")

if __name__ == '__main__':
    main()