#!/usr/bin/env python3

try:
    # for Python 2.x
    import StringIO
except:
    # for Python 3.x
    import io

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# define data

csv_input = """timestamp,title,reqid
2016-07-23 11:05:08,SVP,2356556-AS
2016-12-12 01:23:33,VP,5567894-AS
2016-09-13 12:43:33,VP,3455673-AS
2016-09-13 19:43:33,EVP,8455673-AS
2016-09-30 11:43:33,VP,9455673-AS
2016-08-02 01:23:33,VP,5698765-AS
2016-04-22 01:23:33,VP,1234556-AS
"""

# load data

try:
    # for Python 2.x
    f = StringIO.StringIO(csv_input)
except:
    # for Python 3.x
    f = io.StringIO(csv_input)

reader = csv.reader(f, delimiter=',')
for row in reader:
    print('\t'.join(row))

# reset file pointer position to beginning of file
f.seek(0)

# create pandas dataframe
#df = pd.read_csv(io.StringIO(csv_input))
df = pd.read_csv(f)
print(df.head())

print(df.info())
print(df)

df['date'] = pd.DatetimeIndex(df.timestamp).normalize()
print(df)
print(df.index)

#df = df.drop('timestamp',axis=1)
df.drop('timestamp', axis=1, inplace=True)

#df = df.reindex(df.reqid, fill_value=0)
#df = df.reindex(df.reqid, method='bfill')
#print(df)
#print(df.index)

#i = df[((df.title == 'SVP') & (df.reqid == '3455673-AS'))].index
#df.drop(df.index[0],inplace=True)
#df.drop(i,inplace=True)
#i = df.index[0]
#df = df.drop(i)
#print(df)
#print(i)
print(type(df['date'][0]))

#df = df.sort_values(by='date',axis=0,ascending=True)
df.sort_values(by='date',axis=0,ascending=True,inplace=True)
print(df)

df['weekday'] = df['date'].apply( lambda x: x.dayofweek)

# setup date processing
now_string = '2016-10-01 08:01:20'
past_by_days = 30
time_delta = pd.to_timedelta('{} days'.format(past_by_days))
print(time_delta)
#now = pd.tslib.Timestamp('2016-10-01 08:01:20')
now = pd.Timestamp(now_string)
now_norm = now.normalize()
print(now_norm)

now_start = now_norm - time_delta
print(now_start)

# process
ddf = df.loc[((df['date'] >= now_start) & (df['date'] <= now_norm))]
print(ddf)
print('number of observations found in filtered df = {}'.format(len(ddf)))
print(len(ddf.columns))

# histogram of number of observations by date
df_grouped_date = df.groupby(['date'])
df_date_count = df_grouped_date['reqid'].aggregate(['count'])
#df_date_count = df_grouped_date.aggregate(['count'])
print(df_date_count)


#exclude_cols = ['title count']
#df_date_count.ix[:, df_date_count.columns.difference(exclude_cols)].plot(kind='bar')
df_date_count.ix[:, df_date_count.columns].plot(kind='bar')
plt.legend(loc='best').get_texts()[0].set_text('Reqs Added Per Day')

file_name = 'myBar'
file_name = re.sub('\s+','_',file_name)
plt.savefig(file_name)
plt.show()

