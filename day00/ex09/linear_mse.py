import numpy as np
#add protection
def linear_mse(x, y, theta):
	if len(x) == 0 or len(y) == 0 or len(theta) == 0:
		return None
	total = 0.0
	for i in range(len(x)):
		total += (np.dot(theta,x[i]) - y[i]) ** 2
	return total / len(x)
