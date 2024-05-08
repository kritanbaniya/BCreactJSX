####### this code makes 1 graph after taking start date and end date as input.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
sns.set()


import scipy.stats as stats



df = pd.read_csv('flaskserver/NVDA99.csv')

df = df.drop_duplicates()
df = df.dropna()

df['Date'] = pd.to_datetime(df['Date'])  #### important to compare dates

start_date =   '2020-01-01'  ####input("Enter start date in YYYY-MM-DD format:")
end_date =    '2021-01-01'  ####input("Enter end date in YYYY-MM-DD format:")

df_range = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
 
df_range['Average'] = (df_range['Open'] + df_range['High'] + df_range['Low']) / 3
    

avghigh = df_range['High'].mean(axis='index')
avglow = df_range['Low'].mean(axis='index')

print ("The average high was ", avghigh, " and the avg low was ", avglow)

rangemax = df_range['High'].max(axis = 'index')
rangemin = df_range['Low'].min(axis = 'index')

print ("The maximum prce within this range was ", rangemax)
print ("The minimum price within this range was ", rangemin)


fig = px.line(df_range, x='Date', y='Average', title=f'Average of Open, High, and Low for {start_date} to {end_date}')
fig.update_xaxes(title_text='Date', tickangle=45)
fig.update_yaxes(title_text='Average')
fig.show()

print (type(fig))

