# -*- coding: utf-8 -*-

import numpy as np

print("## sorting a one-dimension array:")
arr = np.random.randn(8)
print(arr)
arr.sort()
print(arr)
print()

print("## sorting a two-dimension array:")
arr = np.random.randn(5, 3) * 100 // 1
print(arr)
print("### np.sort(arr, axis=0) creates an array with each column of arr sorted:")
print(np.sort(arr, axis=0))
print("### np.sort(arr, axis=1) create an array with each row of arr sorted:")
print(np.sort(arr, axis=1))
# print(np.sort(arr, 1)) ## also OK
print()

print("### arr.sort(1) sort each row of arr:")
arr.sort(1);
print(arr)
print()

print("## find the element at sorted position of 5%:")
large_arr = np.random.randn(1000)
large_arr.sort()
print(large_arr[int(0.05 * len(large_arr))])
