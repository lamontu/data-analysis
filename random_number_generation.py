# -*- coding: utf-8 -*-

import numpy as np
from random import normalvariate

print("Draw random samples from a normal distribution:")
samples = np.random.normal(size=(4, 4))
print(samples)

print("Draw random samples from a distribution N(0, 1):")
num = 10
lst1 = [normalvariate(0, 1) for _ in range(num)]
print("len(lst1):", len(lst1))
print(lst1)
lst2 = np.random.normal(size=num)  # equivalent to above
print("len(lst2):", len(lst2))
print(lst2)
