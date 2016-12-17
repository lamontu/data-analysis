# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random

print("""
## zip(*iterables)
   Make an iterator that aggregates elements from each of the iterables""")
zipped = zip([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(zipped)
print(list(zipped))
print()

print("## Select elements from boolean array:")
x_arr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
y_arr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
result = [(x if c else y) for x, y, c in zip(x_arr, y_arr, cond)]
print(result)
print("### np.where(cond, x_arr, y_arr):")
print(np.where(cond, x_arr, y_arr))
print()

print("### examples using 'where':")
arr = np_random.randn(4, 4)
print(arr)
print(np.where(arr > 0, 2, -2))
print()

print("## nested where:")
cond_1 = np.array([True, False, True, True, False])
cond_2 = np.array([False, True, False, True, False])
print("### Using ordinary code:")
result = []
for i in range(len(cond)):
    if cond_1[i] and cond_2[i]:
        result.append(0)
    elif cond_1[i]:
        result.append(1)
    elif cond_2[i]:
        result.append(2)
    else:
        result.append(3)
print(result)
print("### Using NumPy code:")
result = np.where(cond_1 & cond_2, 0,
                  np.where(cond_1, 1, np.where(cond_2, 2, 3)))
print(result)
