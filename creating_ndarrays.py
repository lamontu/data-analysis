# -*- coding: utf-8 -*-

import numpy as np

print("## Use ordinary one-dimension array to create NumPy array:")
data = [6, 7.5, 8, 0, 1]
arr = np.array(data)
print(arr)
print("### Print element type:")
print(arr.dtype)
print()

print("## Use ordinary two-dimension array to create NumPy array:")
data = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr = np.array(data)
print(arr)
print("### Print array dimension:")
print(arr.shape)
print()

print("## Use zers/empty:")
print(np.zeros(10))
print(np.zeros((3, 6)))
print(np.empty((2, 3, 2)))
print()

print("## Use 'arange' to create consecutive element:")
print(np.arange(15))
