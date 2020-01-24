import math
import numpy as np

def sigmoid_(x):
	if type(x) == list or type(x) == np.ndarray:
		for i in range(len(x)):
			x[i] = 1 / (1 + math.exp(-x[i]))
		return x
	else:
		return 1 / (1 + math.exp(-x))
	log_loss.py