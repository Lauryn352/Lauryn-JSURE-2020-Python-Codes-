# -*- coding: utf-8 -*-
"""
Spyder Editor

This is the script file for the modified model 3 (Logistic)
"""
import numpy as np
from math import log
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dy/dt
def model(ym,t):
#    a = 0.9
    b = 100000
    
    if t <=3:
        a = 1.50
    else:
        a =-0.4
        
        dydt = log(2)/a *ym*(1-ym/b)
        return dydt
    
# initial condition
y0 = 10000
    
    
# time poits
t = np.linspace(0,6)

# solve ODE
ym = odeint(model,y0,t)

# plot data
td = [0,1,2,3,4,5]
yd = [10000,30500,79000,90000,75090,23000]
plt.plot(td,yd,'*',label='Data')

# plot results 
plt.plot(t,ym,label='Model')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()
  