# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 23:54:33 2022

@author: tndim
"""
import random
import matplotlib.pyplot as plt
import numpy as np

rolls = []

# for k in range(10000):
#     rolls.append(random.choice([1,2,3,4,5,6]))
    
# plt.hist(rolls, bins = np.linspace(0.5, 6.5, 7))
for k in range(100000000):
    num = 0
    for j in range(10):
        num += random.choice([1,2,3,4,5,6])
    rolls.append(num)    

#print(rolls)
plt.hist(rolls, bins = np.linspace(5, 60, 7))

                 
        