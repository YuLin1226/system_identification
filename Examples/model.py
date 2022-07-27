import control.matlab as cnt
import numpy as np


A = np.array([  [ 0.93482068,  0.09904593],
                [-0.01676111,  0.944566  ]])

B = np.array([  [-0.00545749],
                [-0.03763569]])

C = np.array([  [-1.44937325, -0.03476855]])

D = np.array([  [0]])

# ---

# A = np.array([  [ 0.9604271,   0.09975666, -0.19224271],
#                 [-0.02640439,  0.94400327,  0.20051166],
#                 [ 0.10044895, -0.1505409,  -0.42226104]])

# B = np.array([  [ 0.34888736],
#                 [-0.39491558],
#                 [ 2.51732669]])

# C = np.array([  [-1.44937325, -0.03476855,  0.0176019 ]])

# D = np.array([  [0]])



sysd = cnt.StateSpace(A, B, C, D, 0.02)

dc = cnt.dcgain(sysd)
print(dc)
print(cnt.ss2tf(sysd))