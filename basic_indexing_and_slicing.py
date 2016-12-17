# -*- coding: utf-8 -*-

import numpy as np

print("## Access to row or element of a 2-dimension array:")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[2])
print(arr[0][2])
print(arr[0, 2])  # not valid for ordinary array
print()

print("## Access to high dimension array:")
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("### print(arr[0]:")
print(arr[0])
print("### print(arr[1, 0]:")
print(arr[1, 0])
old_values = arr[0].copy()
arr[0] = 42
print("### after change arr[0]:")
print(arr)
arr[0] = old_values
print("### after restore arr[0]:") 
print(arr)

print("## Access to and manipulate arrays:")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("### arr[1:6] means from arr[1] to arr[5]:")
print(arr[1:6])
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("### arr[:2] means from arr[0] to arr[1]:") 
print(arr[:2])
print("### arr[:2, 1:] means from row 0 to row 1",
      "and from column 1 to last column:")
print(arr[:2, 1:])
print("### arr[:, :1] means from column 0:")
print(arr[:, :1])
print("### arr[:2, 1:] = 0:")
arr[:2, 1:] = 0
print(arr)
