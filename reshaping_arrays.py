# -*- coding: utf-8 -*-

import numpy as np

print("## convert a one-dimension array to a two-dimension array:")
arr = np.arange(8)
print(arr.reshape((4, 2)))
print(arr.reshape((4, 2)).reshape((2, 4)))
print()

print("## auto infer dimension length:")
arr = np.arange(15)
print(arr.reshape((5, -1)))
print()

print("## get dimension length and use it:")
other_arr = np.ones((3, 5))
print(other_arr.shape)
print(arr.reshape(other_arr.shape))
print()

print("## ravel a high dimension array:")
arr = np.arange(15).reshape((5, 3))
print(arr.ravel())
