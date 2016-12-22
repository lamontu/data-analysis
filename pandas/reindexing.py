# -*- coding: utf-8 -*-

import numpy as np
from pandas import DataFrame, Series

print("## Redesignate index and order:")
obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)
obj2 = obj.reindex(['a', 'b', 'd', 'c', 'e'])
print(obj2)
print("### fill with specified value if the index not exist:")
obj3 = obj.reindex(['a', 'b', 'd', 'c', 'e'], fill_value=0)
print(obj3)
print()

print("## Redesignate index and fill method:")
obj4 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(obj4)
print(obj4.reindex(range(6), method='ffill'))
print()

print("## Redesignate index of DataFrame:")
frame = DataFrame(np.arange(9).reshape(3, 3),
                  index = ['a', 'c', 'd'],
                  columns = ['Ohio', 'Texas', 'California'])
print(frame)
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)
print()

print("## Redesignate column:")
states = ['Texas', 'Utah', 'California']
print(frame.reindex(columns=states))
print()

print("## Redesignate index of DataFrame and fill method:")
print(frame.reindex(index = ['a', 'b', 'c', 'd'],
                    method = 'ffill',
                    columns = states))
print(frame.ix[['a', 'b', 'd', 'c'], states])
