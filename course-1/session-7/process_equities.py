#!/usr/bin/env python3

import csv
import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)

equities_filename = 'equities.csv'
#equitiesReader = csv.reader(open(equities_filename), delimiter=',', quotechar="'")
#equitiesReader = csv.reader(open(equities_filename), delimiter=',')
raw_file = open(equities_filename)
headers = 'ticker,date,open,high,low,close,volume,ex-dividend,split_ratio,adj_open,adj_high,adj_low,adj_close,adj_volume'

'''
for row in equitiesReader:
    try:
        print(', '.join(row))
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
# try to determine some useful information about the CSV file
possible_delims = ","
dialect = csv.Sniffer().sniff(headers, delimiters=possible_delims)
raw_file.seek(0)
file_reader = csv.reader(raw_file, dialect)

# process each of the rows into a dictionary and add to the result list
data = list()
for row in raw_file:
#    item = dict(zip(headers, item for item in row))
    item = zip(headers.split(','), row)
    pp.pprint(list(item))
#    data.append(item)

print(data)
'''
file_reader = csv.DictReader(raw_file, delimiter=',')
for row in file_reader:
    print('{}, {}, {}'.format(row['ticker'],row['date'],row['close']))
