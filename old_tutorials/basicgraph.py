import time
import datetime
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.dates import (
    DateFormatter, AutoDateLocator, AutoDateFormatter, datestr2num
)

each_stock = ['TSLA', 'AAPL']

def graphdata(stock):
    try:
        stock_file = stock+'.txt'
        date, openp, highp, lowp, closep, volume = np.loadtxt(stock_file, delimiter=',', unpack=True,
        converters={ 0: mdates.datestr2num('%d-%m-%Y')})

        fig = plt.figure()
        ax1 = plt.sulplot(1,1,1)
        ax1.plot(date, openp)
        ax1.plot(date, highp)
        ax1.plot(date, lowp)
        ax1.plot(date, closep)

        plt.show()
    
    except Exception as e:
        print(str(e), 'failed main loop')


for stock in each_stock:
    graphdata(stock)
    time.sleep(600)