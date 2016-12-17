# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random

print("## Use boolean array as index:")
print()

name_arr = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(name_arr)
rnd_arr = np_random.randn(7, 4)
print(rnd_arr)
print()

print("### Get a boolean array:")
print(name_arr == 'Bob')
print("### Select using a boolean array:")
print(rnd_arr[name_arr == 'Bob'])
print("### Select using a boolean array and slicing:")
print(rnd_arr[name_arr == 'Bob', :2])
print("### Negate the boolean array:")
print(rnd_arr[-(name_arr == 'Bob')])
print()

print("### Select after logical operatinos:")
mask_arr = (name_arr == 'Bob') | (name_arr == 'Will')
print(mask_arr)
print(rnd_arr[mask_arr])
print("### Select using boolean array and then change the selected element:")
rnd_arr[name_arr != 'Joe'] = 7
print(rnd_arr)
