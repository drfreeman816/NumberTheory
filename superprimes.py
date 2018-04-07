import os

os.system('clear')

import numpy as np
import matplotlib.pyplot as plt

def is_prime(n):
    "Very simple primality test"
    for x in np.arange(2, int(np.sqrt(n))):
        if np.mod(n, x) == 0:
            return False
    return True

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

# Superprimes
for x in np.arange(6, 100):
    sp = np.array([])
    for n in np.arange(1, 10000):
        if Gamma(x, n) == n-1:
            print(n)
            sp = np.append(sp, n)
    print(x, np.all([is_prime(p) for p in sp]))