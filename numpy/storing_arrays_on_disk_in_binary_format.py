# -*- coding: utf-8 -*-

import numpy as np

print("## write and read an array file:")
arr = np.arange(10)
np.save('some_array.npy', arr)
# np.save('some_array', arr)  # also OK
print(np.load('some_array.npy'))
print()

print("## compress multiple arrays:")
arr2 = np.arange(10, 20)
np.savez('array_archive.npz', a=arr, b=arr2)
arch = np.load('array_archive.npz')
print(arch['a'])
print(arch['b'])
