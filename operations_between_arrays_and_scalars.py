# -*- coding: utf-8 -*-

import numpy as np

print("## Operations between arrays, operating on corresponding element:") 
arr = np.array([[1.0, 2.0, 3.0], [4., 5., 6.]])
print(arr * arr)
print(arr - arr)
print()

print("## Operations between a scalar and an array,",
      "the scalar operateing on each element of the array:")
arr = np.array([[1.0, 2.0, 3.0], [4., 5., 6.]])
print(1 / arr)
print(arr ** 0.5)
