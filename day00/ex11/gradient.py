def gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.ndarray, using
a for-loop. The two arrays must have the compatible dimensions.
    Args:
     x: has to be an numpy.ndarray, a matrice of dimension m * n.
     y: has to be an numpy.ndarray, a vector of dimension m * 1.
     theta: has to be an numpy.ndarray, a vector n * 1.
    Returns:
     The gradient as a numpy.ndarray, a vector of dimensions n * 1.
     None if x, y, or theta are empty numpy.ndarray.
     None if x, y and theta do not have compatible dimensions.
    Raises:
     This function should not raise any Exception.
	"""
	if len(x) == 0 or len(y) == 0 or len(theta) == 0:
		return None
	total = 0.0
	for i in range(len(x)):
		total += (np.dot(theta,x[i]) - y[i]) * x[i]
	return total / len(x)
