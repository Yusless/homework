#2
import numpy as np
x_axis =list(map(int,input().split()))
y_axis =list(map(int,input().split()))
def MNK(x_axis, y_axis):
    xy = np.mean(np.dot(x_axis, y_axis))
    return xy - np.mean(x_axis) * np.mean(y_axis)
k = MNK(x_axis, y_axis) / MNK(x_axis, x_axis)
b = np.mean(y_axis) - k * np.mean(x_axis)
print (k)
print(b)