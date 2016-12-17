# -*- coding: utf-8 -*-

import numpy as np

print("## Get sum, and mean:")
arr = np.random.randn(5, 4)
print(arr)
print(arr.sum())
print(arr.mean())
print()

print("### arr.sum(axis=1) get sum of each row:")
print(arr.sum(axis=1))
print("### arr.mean(axis=1) get mean of each row:")
print(arr.mean(axis=1)) 
print()

print("### arr.sum(axis=0) get sum of each column:")
print(arr.sum(axis=0))
print("### arr.mean(axis=0) get mean of each column:")
print(arr.mean(axis=0))

print("## demo of 'cumsum' and 'cumprod':")
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(arr)
print("### arr.cumsum(0) get cumulative sum of each column:")
print(arr.cumsum(0))
print("### arr.cumprod(1) get cumulative product of each row:")
print(arr.cumprod(1))
