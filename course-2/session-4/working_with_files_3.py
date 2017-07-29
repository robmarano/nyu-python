#!/usr/bin/env python3

# how to pickle data
import os
import pickle

a = b'12345678'
b = b'9abcdef'
print('a = {}; b = {}'.format(a,b))
# write data to file
cwd = os.getcwd()
file_name = os.path.join(cwd,'program_state.bin')
with open(file_name,'wb+') as f:
    pickle.dump(a,f)
    pickle.dump(b,f)

a = b'9abcdef'
b = b'12345678'
print('a = {}; b = {}'.format(a,b))

with open(file_name,'rb') as f:
    a = pickle.load(f)
    b = pickle.load(f)

print('a = {}; b = {}'.format(a,b))
