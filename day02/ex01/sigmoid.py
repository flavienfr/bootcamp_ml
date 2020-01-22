import math

def sigmoid_(x):
	if type(x) == list:
		for i in range(len(x)):
			x[i] = 1 / (1 + math.exp(-x[i]))
		return x
	else:
		return 1 / (1 + math.exp(-x))
	