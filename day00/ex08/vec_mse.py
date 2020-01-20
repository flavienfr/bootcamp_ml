import numpy as np

def vec_mse(y, y_hat):
	if len(y) == 0 or len(y_hat) == 0 or len(y) != len(y_hat):
		return None
	return np.square(y - y_hat).mean()
