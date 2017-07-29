#!/usr/bin/env python3

import os
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

x = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
pp.pprint(x)

y = json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)
pp.pprint(y)

cwd = os.getcwd()
file_name = os.path.join(cwd,'data.json')
with open(file_name,'r') as f:
    my_data = json.load(f)

#pp.pprint(my_data)

print(my_data['intervals'])

intervals = my_data['intervals']
for x in intervals:
    print(x['powr'])

