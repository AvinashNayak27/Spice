import numpy as np
import matplotlib.pyplot as plt

def H(s):
    return 5e5/(s+1.5e6)
S=np.linspace(-6e6,3e6,100)
plt.plot(S,H(S),color='blue',label=r"$H(s)=\frac{0.5}{1.5+10^{-6}s}$")
plt.legend()
plt.grid()
plt.grid("Transfer function")
plt.xlabel("$s$")
plt.ylabel("$H(S)$")
plt.savefig("./figs/4.3.png")
plt.show()