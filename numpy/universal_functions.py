# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random

print("## square-root of an array:")
arr = np.arange(10)
print(np.sqrt(arr))

print("## Compare array:")
x = np_random.randn(8)
y = np_random.randn(8)
print(x)
print(y)
print(np.maximum(x, y))
print()

print("## Get fractional and integral part:")
arr = np_random.randn(7) * 5
print(arr)
print(np.modf(arr))
