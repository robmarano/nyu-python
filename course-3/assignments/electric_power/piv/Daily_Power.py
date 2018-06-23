"""
Daily_Power.py
"""

__all__ = ['Daily_Power',]
__version__ = '0.1.0'
__author__ = 'Rob Marano'

import logging
import pandas as pd
import numpy as np

PLACEHOLDER_DATE = '1/1/2000'
PERIODS = 24
FREQUENCY = '1H'


class Daily_Power(object):
	def __init__(self, power_config_file='power_config.csv'):
		''' Self constructor '''
		super().__init__()
		# place Daily_Power initialization here
		#
		# Create a time series of 2000 elements, one very five minutes starting on 1/1/2000
		# https://pandas.pydata.org/pandas-docs/stable/timeseries.html#timeseries-offset-aliases
		# http://pandas.pydata.org/pandas-docs/version/0.18.1/api.html#datetimelike-properties
		# time = pd.Series(pd.date_range('1/1/2000', periods=24, freq='1H'))
		# pprint(time.dt.hour)
		times = pd.date_range(PLACEHOLDER_DATE, periods=PERIODS, freq=FREQUENCY)
		hours = [x.hour for x in times]
		self.power_readings = pd.DataFrame(hours, columns=['hours'])
		self.power_config_file = power_config_file
		self.get_power_config()
		self.create_daily_power_readings()
		logging.info('Initialized Daily_Power object')
		pass

	def get_power_config(self):
		self.power_config = pd.read_csv(self.power_config_file)
		#print(self.power_config)
		pass

	def create_daily_power_readings(self):
		self.power_readings['power'] = self.power_readings.apply(lambda row: self.power_formula(row['hours']), axis=1)
		#print(self.power_readings)
		pass


	def power_formula(self, hour):
		'''
		This should be re-written using processing DataFrames between power_config and the initialized power_readings
		'''
		if (hour >= 0) and (hour <= 5):
			return float(500)
		elif (hour >= 6) and (hour <= 7):
			return float(1000)
		elif (hour >= 8) and (hour <= 15):
			return float(500)
		elif (hour >= 16) and (hour <= 17):
			return float(1500)
		elif (hour >= 18) and (hour <= 19):
			return float(3000)
		elif (hour >= 20) and (hour <= 22):
			return float(750)
		elif (hour == 23):
			return float(500)

	def __str__(self):
		to_string = 'Class Name = {} \nPower Config File = {}'.format(self.__class__.__name__, self.power_config_file)
		#print(to_string)
		return to_string
