def mat_vec_prod(x, y):
	"""Computes the product of two non-empty numpy.ndarray, using a
for-loop. The two arrays must have compatible dimensions.
    Args:
     x: has to be an numpy.ndarray, a matrix of dimension m * n.
     y: has to be an numpy.ndarray, a vector of dimension n * 1.
    Returns:
     The product of the matrix and the vector as a vector of dimension m *
1.
     None if x or y are empty numpy.ndarray.
     None if x and y does not share compatibles dimensions.
    Raises:
     This function should not raise any Exception.
    """
	if x.size == 0 or y.size == 0 or x[0].size != len(y):
		return None
	vect = np.zeros((len(x), 1), dtype=int)
	for i in range(len(x)):
		for j in range(y.size):
			vect[i] += y[j] * x[i][j]
	return vect
