#1
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

a= []
b= []
for i in range (-1000000,1000000):
    if i!=0:
        i=i/1000000
        a.append(i)
        b.append(np.sin(1/i))
plt.plot(a,b, 'g')
plt.show()