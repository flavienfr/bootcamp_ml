import numpy as np
from pred import predict_

X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[2.], [4.]])
res = predict_(theta1, X1)
print(res)

X2 = np.array([[1], [2], [3], [5], [8]])
theta2 = np.array([[2.]])
res = predict_(theta2, X2)
print(res)

X3 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
theta3 = np.array([[0.05], [1.], [1.], [1.]])
res = predict_(theta3, X3)
print(res)
