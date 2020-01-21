def dot(x, y):
	"""Computes the dot product of two non-empty numpy.ndarray, using a
for-loop. The two arrays must have the same dimensions.
    Args:
     x: has to be an numpy.ndarray, a vector.
     y: has to be an numpy.ndarray, a vector.
    Returns:
     The dot product of the two vectors as a float.
     None if x or y are empty numpy.ndarray.
     None if x and y does not share the same dimensions.
    Raises:
     This function should not raise any Exception.
	"""
	if x.size == 0 or y.size == 0 or x.size != y.size:
		return None
	total = 0.0
	for i in range(x.size):
		total += x[i] * y[i]
	return total
