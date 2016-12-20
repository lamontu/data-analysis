# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random

print("## transposing an array:")
arr = np.arange(15).reshape((3, 5))
print(arr)
print(arr.T)
print()

print("## transposing an array to calculate matrix pruduct:")
arr = np_random.randn(6, 3)
print(np.dot(arr.T, arr))
print()

print("## high dimension array conversion:")
arr = np.arange(16).reshape((2, 2, 4))
print(arr)
print("""
### arr.transpose((1, 0, 2)) means
    transposing between the first and the second dimensions:""")
print(arr.transpose((1, 0, 2))) 
print("""
### equivalent transposing method, arr.swapaxes(0, 1) menas
    swap the first and the second dimensions:""")
print(arr.swapaxes(0, 1))
