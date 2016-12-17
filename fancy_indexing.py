# -*- coding: utf-8 -*-

import numpy as np

print("## Fancy Indexing: using integer array as index:")
print()

arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
print(arr)
print()

print("### arr[[4, 3, 0, 6]] selects row 4, row 3, row 0, row 6:")
print(arr[[4, 3, 0, 6]])
print("### arr[[-3, -5, -7]] selects row -3, row -5, row -7:")
print(arr[[-3, -5, -7]])
print()

print("### Convert a one-dimension array to a two-dimension array",
      "using 'reshape':")
arr = np.arange(32).reshape((8, 4))
print(arr)
print( """
### arr[[1, 5, 7, 2], [0, 3, 1, 2]] selects 
    arr[1, 0], arr[5, 3], arr[7, 1], arr[2, 2]:""")
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
print("""
### arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]] selects
    column 0, 3, 1, 2 from row 1, 5, 7, 2:""")
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
print("""
### arr[, [0, 3, 1, 2]][[1, 5, 7, 2]] selects
    row 1, 5, 7, 2 from column 0, 3, 1, 2:""")
print(arr[:, [0, 3, 1, 2]][[1, 5, 7, 2]])
print("""
### equivalent access method using
    arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 3])]:""")
print(arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 3])])
