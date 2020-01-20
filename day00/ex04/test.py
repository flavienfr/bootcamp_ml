import numpy as np
from dot import dot

X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
res =dot(X, Y)
print(res)

res =np.dot(X, Y)
print(res)

res =dot(X, X)
print(res)

res =np.dot(X, X)
print(res)

res =dot(Y, Y)
print(res)

res =np.dot(Y, Y)
print(res)
