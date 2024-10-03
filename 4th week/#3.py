#3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import random as rd
a=list()
b=list()
for i in range (10):
    a.append(i)
    b.append(rd.random())

plt.bar(a,b, color='g')
plt.show()