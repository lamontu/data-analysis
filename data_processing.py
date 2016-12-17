# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pylab

print("## Create coordinate matrices:")
row = np.arange(-5, 5, 1)
col = np.arange(-5, 5, 2)
print("row:")
print(row)
print("col:")
print(col)
print("""
### xs, ys = np.meshgrid(row, col) means
    creating xs by repeating row for length of col,
    creating ys by repeating col for length of row.""")
xs, ys = np.meshgrid(row, col)
print(xs)
print(ys)
print()

print("## Create z in coordinate matrices created by meshgrid:")
points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
print(xs)
print(ys)
z = np.sqrt(xs ** 2 + ys ** 2)
print(z)

print("### Draw graph ==>")
plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
pylab.show() 
