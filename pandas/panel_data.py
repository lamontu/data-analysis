# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import pandas_datareader.data as web
from pandas import Series, DataFrame, Index, Panel

pdata = Panel(dict( (stk, web.get_data_yahoo(stk, '1/1/2016', '1/15/2016'))
                    for stk in ['AAPL', 'GOOG', 'BIDU', 'MSFT'] ))
print(pdata)
pdata = pdata.swapaxes('items', 'minor')
print(pdata)
print()

print("## access order: Item -> Major -> Minor:")
print(pdata['Adj Close'])
print(pdata[:, '1/5/2016', :])  # items as columns
print(pdata['Adj Close', '1/6/2016', :])
print()

print("## conversion between Panel and DataFrame:")
print("""### items as columns;
    major, and minor as hierarchical index:""")
stacked1 = pdata.ix[:, '1/7/2016':, :].to_frame()
print("stacked1 ==>")
print(stacked1)
print()

stacked2 = pdata.ix[:, '1/7/2016':, 0:1].to_frame()
#stacked2 = pdata.ix[:, '1/7/2016':, 0].to_frame()  # Error, not interval
print("stacked2 ==>")
print(stacked2)
print()

print("stacked1.to_panel() ==>")
print(stacked1.to_panel())
