# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import sys
from pandas import Series, DataFrame, Index

print("## Get index:")
obj = Series(range(3), index=['a', 'b', 'c'])
index = obj.index
print(index[1:])
try:
    index[1] = 'd'
except:
    print(sys.exc_info()[0])
print()

print("## Use Index object:")
index = Index(np.arange(3))
obj2 = Series([1.5, -2.5, 0], index=index)
print(obj2)
print(obj2.index is index)
print()

print("## Check whether a index or column exist:")
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame = DataFrame(pop)
print('Utah' in frame.columns)
print('Ohio' in frame.columns)
print('2001' in frame.index)
print(2001 in frame.index)
