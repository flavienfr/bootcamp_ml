import numpy as np
from cost_function import cost_elem_
from cost_function import cost_

X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[2.], [4.]])
Y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
res = cost_elem_(theta1, X1, Y1)
print(res)

res = cost_(theta1, X1, Y1)
print(res)

X2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
theta2 = np.array([[0.05], [1.], [1.], [1.]])
Y2 = np.array([[19.], [42.], [67.], [93.]])
res = cost_elem_(theta2, X2, Y2)
print(res)

res = cost_(theta2, X2, Y2)
print(res)
