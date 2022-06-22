# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 22:52:03 2022

@author: tndim
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.logspace(-1, 1, 40)

y = x**2

z = x**1.5

plt.loglog(x, y, "bo-", linewidth=2, markersize=4, label="First") 
plt.loglog(x, z, "gs-", linewidth=3, markersize=12, label="Second")
plt.xlabel("$X$")
plt.ylabel("$Y$") 
plt.axis([-0.5,10.5, -5, 105])
plt.legend(loc="upper left")
#plt.savefig("myplot.pdf")