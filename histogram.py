# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 23:02:22 2022

@author: tndim
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(size=1000)

plt.hist(x, normed=True, bins = np.linspace(-5, 5, 21));