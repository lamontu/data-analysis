# -*- coding: utf-8 -*-

import numpy as np

print("## create an array arr1:")
arr1 = np.random.randn(6, 4)
print(arr1)
print("## save array arr1 as a csv file array_ex.txt ...")
np.savetxt('array_ex.txt', arr1, '%.6f', ',')
print("## read array_ex.txt as an array arr2:")
arr2 = np.loadtxt('array_ex.txt', delimiter=',')
print(arr2)
