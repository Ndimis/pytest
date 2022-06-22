# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 22:27:15 2022

@author: tndim
"""

import numpy as np

zero_vector = np.zeros(5)

zero_matrix = np.zeros((5,3))

unit_vector = np.ones(5)

unit_matrix = np.ones((5,3))

x = np.array([1,2,3])
y = np.array([2,4,6])

X = np.array([[1,3],[2,4]])

zero_vector = np.zeros(8)
#transpose
Y = X.transpose()
Z = np.array([0., 0., 0., 0., 0.])
print(Z)