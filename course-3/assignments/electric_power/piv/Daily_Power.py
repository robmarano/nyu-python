"""
Daily_Power.py
"""

__all__ = ['Daily_Power',]
__version__ = '0.1.0'
__author__ = 'Rob Marano'

import logging
from pprint import pprint
import pandas as pd
import numpy as np

PLACEHOLDER_DATE = '1/1/2000'
PERIODS = 24
FREQUENCY = '1H'
TOLERANCE = 0.1


class Daily_Power(object):
	def __init__(self, power_config_file='power_config.csv'):
		''' Self constructor '''
		super().__init__()
		# place Daily_Power initialization here
		times = pd.date_range(PLACEHOLDER_DATE, periods=PERIODS, freq=FREQUENCY)
		hours = [x.hour for x in times]
		self.power_readings = pd.DataFrame(hours, columns=['hours'])
		self.power_config_file = power_config_file
		self.get_power_config()
		self.create_daily_power_readings()
		logging.info('Initialized Daily_Power object')
		pass

	def power(self, time):
		'''
		Return the power value in Watts at given hour
		'''
		if (type(time) is int):
			if (time in range(0,23)):
				power_value = self.power_readings.at[time,'power']
				return power_value
			else:
				err_msg = 'Hour value ({}) is out of range.'.format(time)
				raise ValueError(err_msg)
		else:
				err_msg = 'Time value ({}) is not integer value of an hour.'.format(time)
				raise TypeError(err_msg)			
		pass

	def get_power_config(self):
		self.power_config = pd.read_csv(self.power_config_file)
		#print(self.power_config)
		pass

	def create_daily_power_readings(self):
		self.power_readings['power'] = self.power_readings.apply(lambda row: self.calculate_power(row['hours']), axis=1)
		print(self.power_readings['power'])
		pass

	def create_daily_power_readings_old_hardcoded(self):
		self.power_readings['power'] = self.power_readings.apply(lambda row: self.calculate_power_old_hardcoded(row['hours']), axis=1)
		print(self.power_readings['power'])
		pass

	def calculate_power(self, hour):
		power_value = float(0)
		for cindex, crow in self.power_config.iterrows():
			if (hour >= crow['start_hour']) and (hour <= crow['end_hour']):
				power_baseline = crow['power_value_watts']
				power_value = float(np.random.randint(power_baseline*(1-TOLERANCE),power_baseline*(1+TOLERANCE)))
		return power_value
		pass

	def calculate_power_old_hardcoded(self, hour):
		'''
		This should be re-written using processing DataFrames between power_config and the initialized power_readings
		'''
		if (hour >= 0) and (hour <= 5):
			baseline = 500
		elif (hour >= 6) and (hour <= 7):
			baseline = 1000
		elif (hour >= 8) and (hour <= 15):
			baseline = 500
		elif (hour >= 16) and (hour <= 17):
			baseline = 1500
		elif (hour >= 18) and (hour <= 19):
			baseline = 3000
		elif (hour >= 20) and (hour <= 22):
			baseline = 750
		elif (hour == 23):
			baseline = 500
		power_value = float(np.random.randint(baseline*(1-TOLERANCE),baseline*(1+TOLERANCE)))
		###df.apply(lambda x: x + np.random.uniform(50))
		return(power_value)

	def __str__(self):
		to_string = 'Class Name = {} \nPower Config File = {}'.format(self.__class__.__name__, self.power_config_file)
		#print(to_string)
		return to_string
