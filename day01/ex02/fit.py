import numpy as np

def fit_(theta, X, Y, alpha = 0.01, n_cycle = 1000):
	if len(X) == 0 or len(Y) == 0 or len(theta) == 0:
		return None
	X = np.insert(X, 0, 1, axis=1)
	for i in range(1, n_cycle):
		lin_regr = (np.dot(X.transpose(), (np.dot(X, theta) - Y))) / (len(X) * 2)
		theta -= alpha * lin_regr
	return theta
