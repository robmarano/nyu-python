#!/usr/bin/env python3

from pprint import pprint
import logging
import pandas as pd
import numpy as np
import piv

# Globals
POWER_CONFIG_FILE='power_config.csv'

# initialize logging for this application
logging.basicConfig(filename='./power.log',level=logging.DEBUG)

def main():
	dp = piv.Daily_Power(POWER_CONFIG_FILE)
	logging.debug('Daily_Power = {}'.format(str(dp)))
	#print(dp)
	readings_string = 'Power readings = \n{}'.format(dp.power_readings)
	logging.debug(readings_string)
	#print(readings_string)
	hour = 21
	power_value = dp.power(hour)
	print('The power reading during hour {} averaged {} Watts'.format(hour, power_value))
	pass

if __name__ == '__main__':
	main()
