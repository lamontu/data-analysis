# -*- coding: utf-8 -*-

import numpy as np

arr = np.arange(10) * 100
inds = [7, 1, 2, 6]
print("arr:")
print(arr)
print("inds:")
print(inds)
print()

print("## Fancy indexing examples:")
print(arr[inds])
print()

print("## arr.take[inds]:")
print(arr.take(inds))
print()

print("## arr.put(inds, 50):")
arr.put(inds, 50)
print("arr:")
print(arr)
print("## arr.put(inds, [70, 10, 20, 60]):")
arr.put(inds, [70, 10, 20, 60])
print("arr:")
print(arr)
print()

print("## Using 'take' with specified axis:")
arr2 = np.random.randn(2, 4)
inds2 = [2, 0, 2, 1]
print("arr2:")
print(arr2)
print("inds2:")
print(inds2)
print("arr.take(inds2, axis=1):")
print(arr2.take(inds2, axis=1))
