import numpy as np

def vec_linear_mse(x, y, theta):
	if len(x) == 0 or len(y) == 0 or len(theta) == 0:
		return None
	total = 0.0
	return ((np.dot(x, theta) - y).transpose() * (np.dot(x, theta) - y)).mean()
