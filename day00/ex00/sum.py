def sum_(x, f):
	"""Computes the sum of a non-empty numpy.ndarray onto wich a function is
applied element-wise, using a for-loop.
    Args:
     x: has to be an numpy.ndarray, a vector.
     f: has to be a function, a function to apply element-wise to the
vector.
    Returns:
     The sum as a float.
     None if x is an empty numpy.ndarray or if f is not a valid function.
    Raises:
     This function should not raise any Exception.
	"""
	if x.size == 0 or not f:
		return None
	total = 0.0
	for value in x:
		total += f(value)
	return total