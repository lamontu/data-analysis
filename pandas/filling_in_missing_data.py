# -*- coding: utf-8 -*-

import numpy as np
from numpy import nan as NA
import pandas as pd
from pandas import Series, DataFrame, Index

print("## fill with 0:")
df = DataFrame(np.random.randn(7, 3))
df.ix[:4, 1] = NA
df.ix[:2, 2] = NA
print("df.fillna(0):")
print(df.fillna(0))
print("df:")
print(df)
print("df.fillna(0, inplace=True):")  # modify df
print(df.fillna(0, inplace=True))
print("df:")
print(df)
print()

print("## fill with different value in different columns:")
df = DataFrame(np.random.randn(7, 3))
df.ix[:4, 1] = NA
df.ix[:2, 2] = NA
print(df.fillna({1:0.5, 3:-1}))  # a dict parameter, column 3 not exist
print()

print("## fill by different methods:")
df = DataFrame(np.random.randn(6, 3))
df.ix[2:, 1] = NA
df.ix[4:, 2] = NA
print(df)
print(df.fillna(method='ffill'))
print(df.fillna(method='ffill', limit=2))
print()

print("## fill by statistic data:")
data = Series([1, NA, 3.5, NA, 7])
print(data.fillna(data.mean()))
