# Visualize ODE assignment
# by Jeffrey Wiedrich and Benjamin Amador
# Using numpy, scipy, and matplotlib, and the notes from class
#The approach was basing solving the ODE off of the notes, and workingn together to figure everythiing out

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dx/dt
def model(x, t, k):
    dxdt = k + t
    return dxdt

# initial condition
x0 = 0.001

# time points
t = np.linspace(0, 12)

# solve ODEs
k = 1
x1 = odeint(model, x0, t, args=(k,))

# plot results
plt.plot(t, x1, 'r-', linewidth=2, label='k=1')
plt.xlabel('Time')
plt.ylabel('Resource Utilization')
plt.legend()
plt.show()
