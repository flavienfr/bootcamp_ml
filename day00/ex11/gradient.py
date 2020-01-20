import numpy as np

def gradient(x, y, theta):
	if len(x) == 0 or len(y) == 0 or len(theta) == 0:
		return None
	total = 0.0
	for i in range(len(x)):
		total += (np.dot(theta,x[i]) - y[i]) * x[i]
	return total / len(x)
