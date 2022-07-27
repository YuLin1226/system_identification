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
import control.matlab as cnt

file_name = "collected_data" + input("vel: ") + ".xlsx"
sheet_name = "sheet1 -1"

input = pd.read_excel(file_name, 
                    # sheet_name=sheet_name, 
                    usecols="A")

output = pd.read_excel(file_name, 
                    # sheet_name=sheet_name, 
                    usecols="B")

time = pd.read_excel(file_name, 
                    # sheet_name=sheet_name,  
                    usecols="C")

U = input.values.T
y_tot = output.values.T
Time = time.values.T

#
plt.close("all")
plt.figure(0)
plt.ylabel("input")
plt.grid()
plt.xlabel("Time")
plt.plot(Time[0,:], U[0,:])
lege = ['Input']
#
plt.ylabel("y_tot")
plt.grid()
plt.xlabel("Time")
plt.plot(Time[0,:], y_tot[0,:])
plt.title("Ytot")
lege.append('System') 

##System identification
# METHOD = ['N4SID', 'CVA', 'MOESP', 'PARSIM-S', 'PARSIM-P', 'PARSIM-K']
# METHOD = ['N4SID', 'CVA', 'MOESP', 'PARSIM-K']
METHOD = ['PARSIM-K']
for i in range(len(METHOD)):

    system_order = 2
    method = METHOD[i]
    sys_id = system_identification(y_tot, U, method, SS_fixed_order = system_order )
    xid, yid = fsetSIM.SS_lsim_process_form(sys_id.A, sys_id.B, sys_id.C, sys_id.D, U, sys_id.x0)
    #
    sysd = cnt.StateSpace(sys_id.A, sys_id.B, sys_id.C, sys_id.D, 0.02)
    dc = cnt.dcgain(sysd)
    plt.plot(Time[0,:], yid[0]/dc)
    lege.append(method) 


    print("\n--- %s system ---" %method)
    print("- State Space Model: ")
    print("\n>>> Matrix A:")
    print(sysd.A)
    print("\n>>> Matrix B:")
    print(sysd.B)
    print("\n>>> Matrix C:")
    print(sysd.C)
    print("\n>>> Matrix D:")
    print(sysd.D)
    print("\n- Transfer function: ")
    print(cnt.ss2tf(sysd))
    print("- DC Gain: %f"%dc)
    # print("B",sys_id.B)
    # print("C",sys_id.C)
    # print("D",sys_id.D)

plt.legend(lege) 
plt.show()


