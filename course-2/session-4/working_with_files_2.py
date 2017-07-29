#!/usr/bin/env python3

import os

cwd = os.getcwd()
file_name = os.path.join(cwd,'test_file.dat')
file_object = open(file_name,'r')
line = file_object.readline()
print(line)
file_object.close()



file_object = open(file_name,'r+')
count = 0
while file_object.readline() != "":
    count += 1
print('{} lines read.'.format(count))
file_object.write("Hello, World!\n")
file_object.close()

count = 0
with open(file_name,'r+') as f:
    while f.readline() != "":
        count += 1
print('{} lines read.'.format(count))


cwd = os.getcwd()
file_name = os.path.join(cwd,'test_file.bin')
with open(file_name,'wb+') as f:
    chars_written = f.write(b'0123456789abcdef')
    print('{} bytes written'.format(chars_written))

with open(file_name,'r') as f:
    data = f.read()
    print(data)

# working with packed binary data structures
import struct
# record format = h=single C short integer; d=single C double-precision floating point number;
# 4s=four string characters
record_format = "hd4s"
record_size = struct.calcsize(record_format)
print('Record size = {}'.format(record_size))
# create data first
the_data = []
my_data = struct.pack(record_format,7, 3.14159, b'gbye')
the_data.append(my_data)
my_data = struct.pack(record_format,3, 3.14159, b'xbye')
the_data.append(my_data)

# write data to file
cwd = os.getcwd()
file_name = os.path.join(cwd,'test_data.bin')
with open(file_name,'wb+') as f:
    for x in the_data:
        chars_written = f.write(x)
        print('{} bytes written'.format(chars_written))
    

# read data second
result_list = []
with open(file_name,'rb') as f:
    while True:
        record = f.read(record_size)
        print('the record fetched = {}'.format(record))
        if record == b'':
            break
        result_list.append(struct.unpack(record_format, record))

for x in result_list:
    print('binary record = {}'.format(x))
