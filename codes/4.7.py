# Plotting y(t) and y(n)

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import subprocess
import shlex

def y_cont(t):
    if t < 0: 
        return 0
    else:
        return 2/3 * (1 - np.exp(-1.5e6 * t))

def y_disc(n):
    if n < 0:
        return 0
    else:
        return 2/3 * (1 - ((1 - 0.075)/(1 + 0.075))**(n*1e7))

def u(n):
    if n>0:
        return 1
    else:
        return 0
def y_diff(n):
    if n < 0:
        return 0
    else:
        return y_diff(n-1)*(((1 - 0.075)/(1 + 0.075))**(n*1e7))+((u(n)+u(n-1))*2/3)*(1 - ((1 - 0.075)/(1 + 0.075))**(n*1e7))
yt = sp.vectorize(y_cont)
yn = sp.vectorize(y_disc)
yd = sp.vectorize(y_diff)



spice = np.loadtxt('codes/4.7.dat')

T = np.linspace(0, 5e-6, 100)

plt.plot(T, yt(T), label='$y(t)$')
plt.plot(spice[:,0], spice[:,1], 'o', label='ngspice')
plt.plot(T, yd(T), '*', label='$ydiff(n)$',ms=10)
plt.plot(T, yn(T), '.', label='$y(n)$')

plt.grid()
plt.legend()
plt.savefig('./figs/4.7.png')
plt.show()
#subprocess.run(shlex.split("termux-open ../figs/4.3.png"))