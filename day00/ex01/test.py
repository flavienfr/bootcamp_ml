import numpy as np
from mean  import mean

X = np.array([0, 15, -9, 7, 12, 3, -21])
res = mean(X)
print(res)

X = np.array([0, 15, -9, 7, 12, 3, -21])
res = mean(X ** 2)
print(res)