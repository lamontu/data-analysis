# -*- coding: utf-8 -*-

import numpy as np
from pandas import Series, DataFrame

print("## Duplicate index:")
obj = Series(range(5), index = ['a', 'a', 'b', 'b', 'c'])
print(obj.index.is_unique)
print(obj)
print(obj[:1])  #  [interval]
# print(obj[0])  # Error
print(obj['a'][1:])
print()

df = DataFrame(np.random.randn(4, 3), index = ['a', 'a', 'b', 'b'])
print(df)
print("### df.ix['b']:")
print(df.ix['b'])

print("### df.ix['b'][1]:")
print(type(df.ix['b'][1]))
print(df.ix['b'][1])

print("### df.ix['b'][1:]:")
print(type(df.ix['b'][1:]))
print(df.ix['b'][1:])

print("### df.ix['b'].ix[1]:")
print(type("df.ix['b'].ix[1]:"))
print(df.ix['b'].ix[1])
print()
