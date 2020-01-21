def std(x):
	"""Computes the standard deviation of a non-empty numpy.ndarray, using a
for-loop.
    Args:
     x: has to be an numpy.ndarray, a vector.
    Returns:
     The standard deviation as a float.
     None if x is an empty numpy.ndarray.
    Raises:
     This function should not raise any Exception.
    """
	if x.size == 0:
		return None
	mean = 0.0
	total = 0.0
	for value in x:
		mean += value
	mean = mean / len(x)
	for value in x:
		total += (value - mean) * (value - mean)
	return math.sqrt(total / len(x))
