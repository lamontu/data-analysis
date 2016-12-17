# -*- coding: utf-8 -*-

import numpy as np

print("## find unique elemens of an array:")
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(names)
print("### sorted(set(names))")
print(sorted(set(names)))
print(names)
print("### np.unique(names")
print(np.unique(names))
print(names)
print()

ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print(ints)
print(np.unique(ints))
print()

print("## check whether the elements of an array in another array:")
arr = np.array([6, 0, 0, 3, 2, 5, 6])
print(arr)
values = np.array([2, 3, 6])
# values = [2, 3, 6]  # also OK
print(values)
find_index = np.in1d(arr, values)
print(find_index)
print(arr[find_index])
