import numpy as np
from sum import sum_

X = np.array([0, 15, -9, 7, 12, 3, -21])
res = sum_(X, lambda x: x)
print (res)

X = np.array([0, 15, -9, 7, 12, 3, -21])
res = sum_(X, lambda x: x**2)
print (res)

X = np.array([])
res = sum_(None,  None)
print (res)