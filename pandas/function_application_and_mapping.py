# -*- coding: utf-8 -*-

import numpy as np
from pandas import Series, DataFrame

print("## Universal functions:")
frame = DataFrame(np.random.randn(4, 3),
                  columns = list('bde'),
                  index = ['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
print(np.abs(frame))
print()

print("## lambda functions:")
f = lambda x: x.max() - x.min()
print(frame.apply(f))
print(frame.apply(f, axis=1))
def fm(x):
    return Series([x.min(), x.max()], index = ['min', 'max'])
print(frame.apply(fm))
print()

print("## applymap, map:")
_format = lambda x: '%.2f' % x
print(frame.applymap(_format))
print(frame['e'].map(_format))
