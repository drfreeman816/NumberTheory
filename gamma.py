import os

os.system('clear')

import numpy as np
import matplotlib.pyplot as plt

def Gamma(x, n):
    "Gamma(x, n) returns the period of x^j mod n"
    d = x
    while d < n:
        d = d*x
    d = np.mod(d, n)
    m = np.mod(x, n)
    p = 1
    v = np.mod(d*m, n)
    while v != d:
        v = np.mod(v*m, n)
        if v == 0:
            return 1
        p = p + 1
    return p

def D(n):
    "D(n) = Gamma(2, n) returns the period of 2^j mod n"
    return Gamma(2, n)

# 

x_plot = np.arange(2, 1000, 1)
y_plot = np.array([D(x) for x in x_plot])
plt.plot(x_plot, y_plot, 'r.')
plt.show()