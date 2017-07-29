#!/usr/bin/env python3

''' Working with Files Part 1'''

''' Path and pathnames '''

import os

# the current working directory
current_working_dir = os.getcwd()
print(current_working_dir)

dir_listing = os.listdir(current_working_dir)
print(dir_listing)

os.chdir('/')
print(os.getcwd())

a_dir_path = os.path.join('bin','utils','disktools')
print(a_dir_path)

path1 = os.path.join('mydir','bin')
path2 = os.path.join('utils','disktools','chkdisk')
newpath = os.path.join(path1,path2)
print(newpath)

the_base_name = os.path.basename(newpath)
print(the_base_name)

fully_qualified_app_path = os.path.join('/home','rob','picture.jpg')
file_type = os.path.splitext(fully_qualified_app_path)
print(file_type[1])

p1 = os.path.join('/usr','bin','1app')
p2 = os.path.join('/usr','bin','2app')
plist = list()
plist.append(p1)
plist.append(p2)
in_common = os.path.commonprefix(plist)
print(in_common)

p1 = os.path.join('/usr','bin','app1')
p2 = os.path.join('/usr','bin','app2')
plist = list()
plist.append(p1)
plist.append(p2)
in_common = os.path.commonprefix(plist)
print(in_common)

expanded_user = os.path.expanduser('~rob')
print(expanded_user)

my_env_vars = os.path.expandvars('$HOME/temp')
print(my_env_vars)

is_dir = os.path.isdir(p1)
print(is_dir)

if os.name == 'posix':
    root_dir = '/'
    print(root_dir)
elif os.name == 'nt':
    root_dir = 'C:\\'
    print(root_dir)
else:
    print("Unknown OS")

import pprint
pp = pprint.PrettyPrinter(indent=4)

my_environs = os.environ
pp.pprint(my_environs)

for x in os.walk(os.path.expanduser('~'),True,None,False):
    print(x)

