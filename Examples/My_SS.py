# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 2018

@author: Giuseppe Armenise, revised by RBdC

In this test, no error occurs. 
Using method='N4SID','MOESP' or 'CVA', if the message
"Kalman filter cannot be calculated" is shown, it means
that the package slycot is not well-installed.

"""
from __future__ import division

from past.utils import old_div

# Checking path to access other files
try:
    from sippy import *
except ImportError:
    import sys, os

    sys.path.append(os.pardir)
    from sippy import *

import numpy as np
from sippy import functionset as fset
from sippy import functionsetSIM as fsetSIM
import matplotlib.pyplot as plt
import pandas as pd


# # Example to test SS-methods

# # sample time
# ts = 1.0

# # SISO SS system (n = 2)
# A = np.array([[0.89, 0.], [0., 0.45]])
# B = np.array([[0.3], [2.5]])
# C = np.array([[0.7, 1.]])
# D = np.array([[0.0]])

# tfin = 500
# npts = int(old_div(tfin, ts)) + 1
# Time = np.linspace(0, tfin, npts)

# # Input sequence
# U = np.zeros((1, npts))
# [U[0],_,_] = fset.GBN_seq(npts, 0.05)

# ##Output
# x, yout = fsetSIM.SS_lsim_process_form(A, B, C, D, U)

# # measurement noise
# noise = fset.white_noise_var(npts, [0.15])

# # Output with noise
# y_tot = yout + noise

# print(U)
# print(y_tot)
# print(Time)


input = pd.read_excel("collected_data.xlsx", 
                    sheet_name="sheet1 -1", 
                    usecols="A")

output = pd.read_excel("collected_data.xlsx", 
                    sheet_name="sheet1 -1", 
                    usecols="B")

time = pd.read_excel("collected_data.xlsx", 
                    sheet_name="sheet1 -1", 
                    usecols="C")

U = input.values.T
y_tot = output.values.T
Time = time.values.T
# t = []
# for i in range(np.size(U)):
#     t.append([i*0.03])

# Time = np.array(t).T

# print(U)
# print(y_tot)
# print(Time)

#
plt.close("all")
plt.figure(0)
# plt.plot(Time, U[0])
plt.plot(Time[0,:], U[0,:])
plt.ylabel("input")
plt.grid()
plt.xlabel("Time")
#
plt.figure(1)
# plt.plot(Time, y_tot[0])
plt.plot(Time[0,:], y_tot[0,:])
plt.ylabel("y_tot")
plt.grid()
plt.xlabel("Time")
plt.title("Ytot")
lege = ['System']

# ##System identification
# # METHOD = ['N4SID', 'CVA', 'MOESP', 'PARSIM-S', 'PARSIM-P', 'PARSIM-K']
# METHOD = ['N4SID', 'CVA', 'MOESP', 'PARSIM-K']
# # METHOD = ['PARSIM-K']
# for i in range(len(METHOD)):

#     method = METHOD[i]
#     sys_id = system_identification(y_tot, U, method, SS_fixed_order = 3 )
#     xid, yid = fsetSIM.SS_lsim_process_form(sys_id.A, sys_id.B, sys_id.C, sys_id.D, U, sys_id.x0)
#     #
#     plt.plot(Time[0,:], yid[0])
#     lege.append(method) 


#     print("\n--- %s system ---" %method)
#     print("A",sys_id.A)
#     print("B",sys_id.B)
#     print("C",sys_id.C)
#     print("D",sys_id.D)


r = []

for i in range(np.size(U)):
    if i == 0:
        r.append([(U[0,i+1] - 1.879*U[0,i])/0.009218])
    elif i == np.size(U)-1:
        r.append([(U[0,i] - 1.879*U[0,i] + 0.8847*U[0,i-1] + 0.003295*r[i-1][0])/0.009218])
    else:
        r.append([(U[0,i] - 1.879*U[0,i] + 0.8847*U[0,i-1] + 0.003295*r[i-1][0])/0.009218])
A = np.array([  [ 0.93482068,  0.09904593],
                [-0.01676111,  0.944566  ]])
B = np.array([  [-0.00545749],
                [-0.03763569]])
C = np.array([  [-1.44937325, -0.03476855]])
D = np.array([  [0]])

# ---
# for i in range(np.size(U)):
#     if i == 0:
#         r.append([(U[0,i+1] - 1.482*U[0,i] + 0.1546*0 + 0.3355*0 - 0.915*0 + 0.4585*0)/-0.4476])
#     elif i == 1:
#         r.append([(U[0,i+1] - 1.482*U[0,i] + 0.1546*U[0,i-1] + 0.3355*0 - 0.915*r[i-1][0] + 0.4585*0)/-0.4476])
#     elif i == np.size(U)-1:
#         r.append([(U[0,i] - 1.482*U[0,i] + 0.1546*U[0,i-1] + 0.3355*U[0,i-2] - 0.915*r[i-1][0] + 0.4585*r[i-2][0])/-0.4476])
#     else:
#         r.append([(U[0,i+1] - 1.482*U[0,i] + 0.1546*U[0,i-1] + 0.3355*U[0,i-2] - 0.915*r[i-1][0] + 0.4585*r[i-2][0])/-0.4476])
# A = np.array([  [ 0.9604271,   0.09975666, -0.19224271],
#                 [-0.02640439,  0.94400327,  0.20051166],
#                 [ 0.10044895, -0.1505409,  -0.42226104]])
# B = np.array([  [ 0.34888736],
#                 [-0.39491558],
#                 [ 2.51732669]])
# C = np.array([  [-1.44937325, -0.03476855,  0.0176019 ]])
# D = np.array([  [0]])

ref = np.array(r).T
xid, yid = fsetSIM.SS_lsim_process_form(A, B, C, D, ref)
plt.plot(Time[0,:], yid[0])
lege.append("Model") 
plt.legend(lege) 

# plt.plot(Time, U[0])
plt.plot(Time[0,:], U[0,:])
lege.append("Input") 
plt.legend(lege) 

plt.figure(0)
plt.plot(Time[0,:], yid[0])
lege.append("Model") 
plt.legend(lege) 


plt.show()


