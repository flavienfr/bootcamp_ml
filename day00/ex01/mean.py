def mean(x):
	"""Computes the mean of a non-empty numpy.ndarray, using a for-loop.
    Args:
     x: has to be an numpy.ndarray, a vector.
    Returns:
     The mean as a float.
     None if x is an empty numpy.ndarray.
    Raises:
     This function should not raise any Exception.
    """
	if x.size == 0:
		return None
	total = 0.0
	for value in x:
		total += value
	return total / len(x)
