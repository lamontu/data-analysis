# -*- coding: utf-8 -*-

import numpy as np

print("## Designate data type when creating an array:")
arr = np.array([1, 2, 3], dtype=np.float64)
print(arr.dtype)
arr = np.array([1, 2, 3], dtype=np.int32)
print(arr.dtype)
print()

print("## Use 'astype' to convert data type when copy an array:")
int_arr = np.array([1, 2, 3, 4, 5])
float_arr = int_arr.astype(np.float)
print(int_arr.dtype)
print(float_arr.dtype)
print()

print("## Discard decimal part when using 'astype' to convert float to int:")
float_arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
int_arr = float_arr.astype(dtype=np.int)
print(int_arr)
print() 

print("## Use 'astype' to convert string to array, throw exception if failed:")
str_arr = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
float_arr = str_arr.astype(dtype=np.float)
print(float_arr)
print(str_arr)
print()

print("## Use the data type of other array as an argument of 'astype':")
int_arr = np.arange(10)
print(int_arr.dtype)
float_arr = np.array([.23, 0.270, .357, 0.44, 0.5], dtype=np.float64)
print(int_arr.astype(float_arr.dtype))  # copy to create a new array
print(int_arr[0], int_arr[1])
