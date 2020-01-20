import numpy as np

def vec_gradient(x, y, theta):
	if len(x) == 0 or len(y) == 0 or len(theta) == 0:
		return None
	return np.mean((np.dot(x, theta) - y) * x.transpose(), axis = 1)