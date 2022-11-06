import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy as sp
diff=[]
def y_diff(n):
    if n < 0:
        return 0
    else:
        changes=(y_diff(n-1)*((1e-6 - 0.75)/(1e-6 + 0.75)))+1/(1e-6+1.5)
        diff.append(changes)
        return changes
y_diff(10)
print(diff)