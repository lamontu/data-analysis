# -*- coding: utf-8 -*-

import numpy as np

print("## Get the sum of positive numbers:")
arr = np.random.randn(100)
print((arr > 0).sum())

print("## logical operations on arrays:")
bools = np.array([False, False, True, False])
print(bools.any())
print(bools.all())
