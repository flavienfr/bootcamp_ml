import numpy as np

def sigmoid_(x):
	if type(x) == list:
		for i in range(len(x)):
			x[i] = 1 / (1 + np.exp(-x[i]))
		return x
	else:
		return 1 / (1 + np.exp(-x))
	log_loss.py