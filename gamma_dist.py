# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 23:10:36 2022

@author: tndim
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.gamma(2, 3, 100000)
#plt.hist(x, bins = 30, normed=True)
plt.figure()
plt.subplot(2,2,1)
plt.hist(x, bins = 30)
plt.subplot(2,2,2)
plt.hist(x, bins = 30)
plt.subplot(223)
plt.hist(x, bins=30, cumulative= 30)
plt.subplot(224)
plt.hist(x, bins = 30, cumulative=True, histtype="step")
#plt.savefig("hist.pdf")

