# -*- coding: utf-8 -*-

import numpy as np
from pandas import Series, DataFrame

print("## Series index and default ordinal number index")
obj = Series(np.arange(4.0), index = ['a', 'b', 'c', 'd'])
print(obj)
print(obj['b'])
print(obj[3])
print(obj[[1, 3]])
print(obj[obj < 2])
print()

print("## Series slice:")
print(obj['b':'c'])  ## closed interval
obj['b':'c'] = 5
print(obj)
print()

print("## DataFrame index:")
data = DataFrame(np.arange(16).reshape((4, 4)),
                 index = ['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns = ['one', 'two', 'three', 'four'])
print(data)
print(data['two'])
print(data[['three', 'one']])

print(data[:2])
print(data.ix['Colorado', ['two', 'three']])
print(data.ix[['Colorado', 'Utah'], [3, 0, 1]])
print(data.ix[2])
print(data.ix[:'Utah', 'two'])
print()

print("## Setect based on condition:")
print(data[data.three > 5])
print(data < 5)
data[data < 5] = 0
print(data)
