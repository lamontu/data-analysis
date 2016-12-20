# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import pylab

print("## Simulate random walks:")
nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()

print("Draw graph ...")
plt.title("Random Walk")
limit = max(abs(min(walk)), abs(max(walk)))
plt.axis([0, 1000, -limit, limit])
x = np.linspace(0, 1000, 1000)
plt.plot(x, walk, 'g-')
print("Finish drawing graph.")
plt.show()
print("Graph closed") 
