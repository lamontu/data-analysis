# -*- coding: utf-8 -*-

import numpy as np
import sys
from pandas import Series, DataFrame

print("## integer index:")
ser = Series(np.arange(3.))
print(ser)
print(ser[0])  # OK, integer as index value
print()
try:
    print(ser[-1])  # Error, integer as index value, -1 not exist 
except:
    print(sys.exc_info()[0])
ser2 = Series(np.arange(3.), index = ['a', 'b', 'c'])
print(ser2)
print(ser2[-1])  # integer as index location 
print(ser2[2])  # integer as index location
print()

ser3 = Series(range(3), index = [-5, 1, 3])
print(ser3)
# print(ser3[2])  # Error, integer as index value, 2 not exist
print(ser3[1])  # OK, integer as index value 
print(ser3.iloc[1])  # index location as parameter
print(ser3.iloc[0])
print(ser3.iloc[-1])
print(ser3.iloc[2])
