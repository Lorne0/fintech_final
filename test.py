import numpy as np
import pandas as pd
#from myStrategy import *
from myStrategy import myStrategy

pastData = pd.read_csv('SPY.csv')
pastData.set_index('Date', inplace=True)

capital = 1000.0 # initial cash
unit = 0.0 # unit of stock in hand
days = 6276 # number of days for testing
result = []
for i in range(days-1, -1, -1):
    data = pastData[0:len(pastData)-i] # 0~1, 0~2, 0~3, ...
    answer = data[-1:].values[0] # last row of data -> y
    data = data[:-1] # delete last row of data -> X
    a = myStrategy(data)

    if a==1: #buy
        if unit==0: # change all cash to stock unit
            unit = capital/(answer[4]+answer[0]-answer[3])
            capital = 0
    elif a==-1: #sell
        if unit>0: # change all stock unit to cash
            capital = unit*(answer[4]+answer[0]-answer[3])
            unit = 0

    result.append(capital+unit*(answer[4]+answer[0]-answer[3]))

answer = pastData[-1:].values[0]
total = capital+unit*(answer[4]+answer[0]-answer[3])
print("Result: %f" %(total))
#np.save('sortino.npy', np.array(result))

