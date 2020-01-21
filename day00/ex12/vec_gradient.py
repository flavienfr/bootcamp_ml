import numpy as np

def vec_gradient(x, y, theta):
	"""Computes a gradient vector from three non-empty numpy.ndarray,
without any for-loop. The three arrays must have the compatible dimensions.
    Args:
     x: has to be an numpy.ndarray, a matrice of dimension m * n.
     y: has to be an numpy.ndarray, a vector of dimension m * 1.
     theta: has to be an numpy.ndarray, a vector n * 1.
    Returns:
     The gradient as a numpy.ndarray, a vector of dimensions n * 1, containg
the result of the formula for all j.
     None if x, y, or theta are empty numpy.ndarray.
     None if x, y and theta do not have compatible dimensions.
    Raises:
     This function should not raise any Exception.
	"""
	if len(x) == 0 or len(y) == 0 or len(theta) == 0:
		return None
	return np.mean((np.dot(x, theta) - y) * x.transpose(), axis = 1)
