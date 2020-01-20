import numpy as np
from std import std

X = np.array([0, 15, -9, 7, 12, 3, -21])
res=std(X)
print(res)

res=np.std(X)
print(res)

Y = np.array([2, 14, -13, 5, 12, 4, -19])
res=std(Y)
print(res)

res=np.std(Y)
print(res)
