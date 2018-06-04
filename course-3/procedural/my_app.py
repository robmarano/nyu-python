#!/usr/bin/env python

from module_1.module_1 import process_1
from module_2.functions import process_2

def run_my_app():
	''' The mainline of my app '''
	process_1()
	process_2()

if __name__ == '__main__':
  run_my_app()
