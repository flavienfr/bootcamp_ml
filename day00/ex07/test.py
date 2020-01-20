import numpy as np
from mse import mse

X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])

res = mse(X, Y)
print(res)