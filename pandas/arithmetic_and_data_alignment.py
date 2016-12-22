# -*- coding: utf-8 -*-

import numpy as np
from pandas import Series, DataFrame

print("## Series addition:")
s1 = Series([7.3, -2.5, 3.4, 1.5], index = ['a', 'c', 'd', 'e'])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index = ['a', 'c', 'e', 'f','g'])
print(s1)
print(s2)
print(s1 + s2)
print()

print("## DataFrame addition, compatible index and columns:")
df1 = DataFrame(np.arange(9.).reshape((3, 3)),
                columns = list('bcd'),
                index = ['Ohio', 'Texas', 'Colorado'])
df2 = DataFrame(np.arange(12).reshape((4, 3)),
                columns = list('bde'),
                index = ['Utah', 'Ohio', 'Texas', 'Oregon'])
print(df1)
print(df2) 
print(df1 + df2)
print()

print("## Fill values:")
df1 = DataFrame(np.arange(12.).reshape((3, 4)), columns = list('abcd'))
df2 = DataFrame(np.arange(20.).reshape((4, 5)), columns = list('abcde'))
print(df1)
print(df2)
print(df1.add(df2, fill_value=0))
print(df1.reindex(columns=df2.columns, fill_value=0))
print()

print("## Operate between Series and DataFrame:")
arr = np.arange(12.).reshape((3, 4))
print(arr)
print(arr[0])
print(arr - arr[0])
frame = DataFrame(np.arange(12).reshape((4, 3)),
                  columns = list('bde'),
                  index = ['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.ix[0]
print("frame:")
print(frame)
print("series:")
print(series)
print(type(frame))
print(type(series))
print(frame - series)
series2 = Series(range(3), index = list('bef'))
print("series2:")
print(series2)
print(frame + series2)
series3 = frame['d']
print("series3:")
print(series3)
print(frame.sub(series3, axis=0))  # substract by column(along dim 0)
