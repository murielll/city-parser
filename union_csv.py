# -*- coding: utf-8 -*-
'''
This script merge csv files with identical columns
but different data in one file named united.csv.
Cmd args is the filenames of merged csv files.
'''
import sys
import codecs

csv_files = sys.argv[1:]
print csv_files

with codecs.open('united.csv', 'a', encoding='utf-8') as output_file:

    first_csv = codecs.open(csv_files[0], encoding='utf-8')
    for line in first_csv.readlines():
        output_file.write(line)
    first_csv.close()

    for csv_file in csv_files[1:]:
        csv_file = codecs.open(csv_file, encoding='utf-8')
        for line in csv_file.readlines()[1:]:
            output_file.write(line)

print "\nComplete! Results in united.csv"
