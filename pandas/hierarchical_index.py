# -*- coding: utf-8 -*-

import numpy as np
from pandas import Series, DataFrame, MultiIndex

print("## Series hierarchical index:")
data = Series(np.random.randn(10),
              index = [['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                       [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
print(data)
print(data.index)
print(data.b)
print(data['b':'c'])
print(data[:2])
print(data.unstack())
print(data.unstack().stack())
print()

print("## DataFrame hierarchical index:")
frame = DataFrame(np.arange(12).reshape((4, 3)),
            index = [['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
            columns = [['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
print(frame)
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
print(frame)
print(frame.ix['a', 1])
print(frame.ix['a', 2]['Colorado'])
print(frame.ix['a', 2]['Ohio']['Red'])
print()

print("## Create hierarchial index using MultiIndex:")
idx = MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorado'],
                              ['Green', 'Red', 'Green']],
                             names = ['state', 'color'])
print(idx)
data = Series(list(range(3)), index=idx)
print(data)
