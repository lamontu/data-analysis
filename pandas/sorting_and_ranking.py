# -*- coding: utf-8 -*-

import numpy as np
from pandas import Series, DataFrame

print("## Sort by index of Series:")
obj = Series(range(4), index = ['d', 'a', 'b', 'c'])
print(obj.sort_index())
print()

print("## Sort by ispecified axis of DataFrame:")
frame = DataFrame(np.arange(8).reshape((2, 4)),
                  index = ['three', 'one'],
                  columns = list('dabc'))
print(frame.sort_index())
# print(frame.sort_index(axis=0))  # equivalent as above
print(frame.sort_index(axis=1))
print(frame.sort_index(axis=1, ascending=False))
print()

print("## Sort by value of Series:")
obj = Series([4, 7, -3, 2])
print(obj.sort_values())
print()

print("## Sort by columns of DataFrame:")
frame = DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
print(frame)
print(frame.sort_values(by='b'))
print(frame.sort_values(by = ['a', 'b']))
print()

print("## rank(), compute numerical data ranks, start from 1:") 
obj = Series([7, -5, 7, 4, 2, 0, 4])
print("obj.rank(axis='index'):")
print(obj.rank(axis='index'))  # default: axis=0, axis='index'
print("""obj.rank(method='first')),
ranks assigned in order they appear in the array:""")
print(obj.rank(method='first'))
print("obj.rank(method='min'):")
print(obj.rank(method='min'))
print("obj.rank(ascending=False, method='max'):")
print(obj.rank(ascending=False, method='max'))
print()

frame = DataFrame({'b': [4.3, 7, -3, 2],
                   'a': [0, 1, 0, 1],
                   'c': [-2, 5, 8, -2.5]})
print("frame:")
print(frame)
print("frame.rank(axis=1):")
print(frame.rank(axis=1))
