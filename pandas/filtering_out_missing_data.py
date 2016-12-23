# -*- coding: utf-8 -*-

import numpy as np
from numpy import nan as NA
from pandas import Series, DataFrame

print("## Drop NA from Series:")
data = Series([1, NA, 3.5, NA, 7])
print(data.dropna())
print(data[data.notnull()])

print("## Drop NA from DataFrame:")
data = DataFrame([[1., 6.5, 3.], [1., NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])
print(data)
print(data.dropna())  # drop the row containing NA
print(data.dropna(how='all'))  # drop the row all is NA
data[4] = NA  # add a column
print("data:")
print(data)
print("data.dropna(axis=0, how='all'):")
print(data.dropna(axis=0, how='all'))
print("data.dropna(axis=1, how='all'):")
print(data.dropna(axis=1, how='all'))
print()

data = DataFrame(np.random.randn(7, 3))
data.ix[:4, 1] = NA
data.ix[:2, 2] = NA
print(data)
print(data.dropna(thresh=2))  ## left the rows containing at least 2 NOT NA
