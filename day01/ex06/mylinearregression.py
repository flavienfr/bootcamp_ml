import numpy as np

class MyLinearRegression():
	"""
	Description:
		My personnal linear regression
	"""
	def __init__(self, theta):
		self.theta = theta
	
	def predict_(self, X):
		if len(self.theta) == 0 or len(X) == 0:
			return None
		X = np.insert(X, 0, 1, axis=1)
		if X[0].size != len(self.theta):
			return None
		return np.dot(X, self.theta)

	def cost_elem_(self, X, Y):
		if len(X) == 0 or len(Y) == 0 or len(self.theta) == 0:
			return None
		X = np.insert(X, 0, 1, axis=1)
		if X[0].size != len(self.theta):
			return None
		return (((np.dot(X, self.theta) - Y) * (np.dot(X, self.theta) - Y)) / (2 * len(X)))

	def cost_(self, X, Y):
		if len(X) == 0 or len(Y) == 0 or len(self.theta) == 0:
			return None
		X = np.insert(X, 0, 1, axis=1)
		if X[0].size != len(self.theta):
			return Nones
		return (((np.dot(X, self.theta) - Y) * (np.dot(X, self.theta) - Y)) / 2).mean()

	def fit_(self, X, Y, alpha = 0.01, n_cycle = 1000):
		if len(X) == 0 or len(Y) == 0 or len(self.theta) == 0:
			return None
		X = np.insert(X, 0, 1, axis=1)
		for i in range(1, n_cycle):
			lin_regr = (np.dot(X.transpose(), (np.dot(X, self.theta) - Y))) / (len(X) * 2)
			self.theta -= alpha * lin_regr
		return self.theta

	def normalequation_(self, X, Y):
		if len(X) == 0 or len(Y) == 0:
			return None
		X = np.insert(X, 0, 1, axis=1)
		l = np.linalg.inv(np.dot(X.transpose(), X))
		r = np.dot(X.transpose(), Y)
		self.theta = np.dot(l, r)
		return self.theta
