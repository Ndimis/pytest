# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 21:20:36 2022

@author: tndim
"""

import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
X = np.array([[1,2,3],[4,5,6]])
Y = np.array([[2,4,6],[8,10,12]])

z = x + y
print(X[:,1])

print(X[1,:]+Y[1,:])

z1 = np.array([1,3,5,7,9])
z2 = z1 + 1

z3 = np.linspace(0, 100, 10)

z4 = np.logspace(1, 2, 10)

z5= np.logspace(np.log10(250), np.log10(500), 10)

x = 7
print(not np.any([x%i == 0 for i in range(2, x)]))

print(X.shape)
print(X.size)