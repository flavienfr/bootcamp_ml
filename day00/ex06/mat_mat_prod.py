import numpy as np

def mat_mat_prod(x, y):
	if x.size == 0 or y.size == 0 or x[0].size != len(y):
		return None
	vect = np.zeros((len(x), y[0].size), dtype=int)
	for i in range(len(x)):
		for j in range(y[0].size):
			for k in range(x[0].size):
				vect[i][j] += x[i][k] * y[k][j]
	return vect
