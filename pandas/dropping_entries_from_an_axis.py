# -*- coding: utf-8 -*-

import numpy as np
from pandas import Series, DataFrame

print("## Drop Series entry from specified index:")
obj = Series(np.arange(5.0), index = ['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop('c')
print(new_obj)
print(obj.drop(['d', 'c']))
print()

print("""## Drop a specified column from a DataFrame
   Drop an entry from a DataFrame by specified index:""")
data = DataFrame(np.arange(16).reshape((4, 4)),
                 index = ['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns = ['one', 'two', 'three', 'four'])
print(data)
print(data.drop('Colorado', axis=0))
print(data.drop(['Colorado', 'Ohio']))
print(data.drop(['Colorado', 'Ohio'], axis=0)) ## equivalent to above
print(data.drop('two', axis=1))
print(data.drop(['two', 'four'], axis=1))
