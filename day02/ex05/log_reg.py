import numpy as np

class LogisticRegressionBatchGd:
	def __init__(self, alpha=0.001, max_iter=1000, verbose=False, learning_rate='constant'):
		self.alpha = alpha
		self.max_iter = max_iter
		self.verbose = verbose
		self.learning_rate = learning_rate
		self.thetas = [0, 0, 0, 0]#np.zeros(82)
		self.eps = 1e-15

	def predict(self, x_train):
		if type(x_train) == list or type(x_train) == np.ndarray:
			for i in range(len(x_train)):
				x_train[i] = 1 / (1 + np.exp(-x_train[i]))
				x_train[i] = np.where(x_train[i]<0.5, 0, 1)
			return x_train
		else:
			#res < 0.5 ? 0 1 
			return 1 / (1 + np.exp(-x_train))

	def fit(self, x_train, y_train):
		x_train = np.insert(x_train, 0, 1, axis=1)
		y_pred = self.predict(x_train)
		print(y_train)
		print(y_pred)
		#for i in range(1, self.max_iter):
			#y_pred = self.predict(x_train)
			#print(y_train)
			#cost = (-1 / len(x_train)) * (np.dot(y_train, np.log(y_pred + self.eps)) + np.dot((1 - y_train), np.log(1 - y_pred + self.eps)))
			#print(y_pred - y_train)

			#print(cost)
			#self.thetas = np.dot((self.alpha / len(x_train)), np.dot((cost - y_train), x_train))
			#x_train = np.dot(x_train, self.thetas)
		return self
	
	def score(self, x_train, y_train):
		pass


'''
	def fit(self, x_train, y_train):
		x_train = np.insert(x_train, 0, 1, axis=1)
		for i in range(1, self.max_iter):
			y_pred = self.predict(x_train)
			log_grad = np.dot((y_pred.transpose() - y_train), x_train)#warning with .transpose()
			self.thetas -= self.alpha * log_grad
			cos = (-1 / len(y_train)) * (np.dot(y_train, np.log(y_pred + self.eps)) + np.dot((1 - y_train), np.log(1 - y_pred + self.eps)))
			print(cos)
			x_train = np.dot(x_train, self.thetas)
		return self
'''