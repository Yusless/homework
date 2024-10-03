#2
#1
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

a=(50,30,10,9,1)
label_list=('Лягушка', "Лягушка!","Лягушка?","Лягушка...","акшугяЛ")
plt.pie(a,labels=label_list, shadow=True, colors=('#008000','#43d143','#27610c','#127a00','#56c456'))
plt.show()