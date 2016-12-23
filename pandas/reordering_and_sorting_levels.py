# -*- coding: utf-8 -*-

import numpy as np
from pandas import Series, DataFrame

print("## hierarchical index exchange:")
frame = DataFrame(np.arange(12).reshape((4, 3)),
            index = [['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
            columns = [['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
frame.index.names = ['key1', 'key2']
frame_swapped = frame.swaplevel('key1', 'key2')
print(frame_swapped)
print(frame_swapped.swaplevel(0, 1))
print()

print("## order by index:")
print(frame.sortlevel('key2'))
print(frame.swaplevel(0, 1).sortlevel(0))
