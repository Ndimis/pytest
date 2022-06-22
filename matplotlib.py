# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 22:18:31 2022

@author: tndim
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 20)

y = x**2

z = x**1.5

plt.plot(x, y, "bo-", linewidth=2, markersize=4, label="First") 
plt.plot(x, z, "gs-", linewidth=3, markersize=12, label="Second")
plt.xlabel("$X$")
plt.ylabel("$Y$") 
plt.axis([-0.5,10.5, -5, 105])
plt.legend(loc="upper left")
plt.savefig("myplot.pdf")