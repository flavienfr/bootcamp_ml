import numpy as np

def mat_vec_prod(x, y):
	if x.size == 0 or y.size == 0 or x[0].size != len(y):
		return None
	vect = np.zeros((len(x), 1), dtype=int)
	for i in range(len(x)):
		for j in range(y.size):
			vect[i] += y[j] * x[i][j]
	return vect
