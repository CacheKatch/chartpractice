# Import dependencies

from pathlib import Path 
import csv
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import time
import datetime

'''
Code starts here
'''

# Provide a list of stocks to chart

stock_list = ['TSLA', 'AAPL']

def graphdata(stock):
    try:
        stock_file = 'Resources/'+stock+'.csv'

        df = pd.read_csv(stock_file, header=None, names=['date', 'openp', 'highp', 'lowp', 'closep', 'volume'])

        df['date'] = pd.to_datetime(df['date'])

        df.plot(x='date', y=['openp', 'highp', 'lowp', 'closep'])

        plt.show()

    except Exception as e:
        print(str(e), 'failed main loop')


for stock in stock_list:
    graphdata(stock)
    time.sleep(120)