#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

gis_file = 'Annual_Average_Daily_Traffic__AADT___Beginning_1977.csv'

df = pd.read_csv(gis_file)

print(df.head())

# remove spaces from column names
cols = df.columns
cols = cols.map(lambda x: x.replace(' ', '_') if isinstance(x, (str, unicode)) else x)
df.columns = cols

print(df.columns)

# Delete the columns we don't care about
df = df.drop(['RC_ID', 'GIS_Code'], axis=1)

# Aggregations

# Find total by year
df_grouped_year = df.groupby(df.Year)
print(df_grouped_year)

df_total_grouped_year = df_grouped_year.sum()
print(df_total_grouped_year)

df_total_grouped_year = df_grouped_year.aggregate({'AADT': np.sum})
print(df_total_grouped_year)
print(df_total_grouped_year.columns)

municipalities = ['NEW YORK CITY', 'TROY', 'CROTON-ON-HUDSON']
df_grouped_muni = df.loc[df.Municipality.isin(municipalities)]
df_total_muni_aadt_grouped = df_grouped_muni.groupby(['Year'])
df_total_muni_aadt = df_total_muni_aadt_grouped.agg({'AADT': np.sum})

print(df_total_muni_aadt.columns)
print(df_total_muni_aadt.head())

exclude_cols = ['Region', 'Begin_Milepoint', 'End_Milepoint']
df_total_muni_aadt.ix[:, df_total_muni_aadt.columns.difference(exclude_cols)].plot(kind='bar')
plt.legend(loc='best').get_texts()[0].set_text('Annual Average Daily Traffic for {}'.format(', '.join(map(str,municipalities))))

file_name = 'AADT_{}'.format('_'.join(map(str,municipalities)))
file_name = re.sub('\s+','_',file_name)
plt.savefig(file_name)
plt.show()

