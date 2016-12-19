# -*- coding: utf-8 -*-

import numpy as np

print("## repeate by element:")
arr = np.arange(3)
print(arr.repeat(3))
print(arr.repeat([2, 3, 5]))  # len(arr) == len([2, 3, 5])
print()

print("## repeat by axis:")
arr = np.random.randn(2, 3)
print(arr)
print("### repeate by row:")
print(arr.repeat(2, axis=0))
print("### repeate by column:")
print(arr.repeat(2, axis=1))

print("## tile an array to create a new array:")
arr = np.random.randn(2, 2)
print(arr)
print("np.tile(arr, 2):")  
print(np.tile(arr, 2))  
print("np.tile(arr, (1, 2)):")
print(np.tile(arr, (1, 2)))  # equivalent as above
print("np.tile(arr, (1, 1, 2)):")
print(np.tile(arr, (1, 1, 2)))  # add dim 2
print()

arr2 = np.array([1, 2, 3])
print("arr2:")
print(arr2)
print("""### np.tile(arr2, (1, 2)):
    len((1,2)) == 2 > arr2.ndim == 1, so arr2 is promoted to shape (1, 3):""")
arr2_t = np.tile(arr2, (1, 2))
print(arr2_t)
print("arr2_t.shape:", arr2_t.shape)
print()

print("""### np.tile(arr3, (2, 1, 1)):
    len((2, 1, 1)) == 3 > arr3.ndim == 2, so arr3 is promoted to shape (1, 2, 2):""")
arr3 = np.array([[1, 2], [3, 4]])
print("arr3:")
print(arr3)
print("np.tile(arr3, (2, 1, 1):")
arr3_t = np.tile(arr3, (2, 1, 1))
print(arr3_t)
print("arr3_t.shape:", arr3_t.shape)
