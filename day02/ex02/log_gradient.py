def log_gradient_(x, y_true, y_pred):
	if type(y_true) == list:
		n_x = [0]*len(x[0])
		for i in range(len(x[0])):
			res = 0
			for j in range(len(y_true)):
				n_x[i] += (y_pred[j] - y_true[j]) * x[j][i]
		return n_x
	else:
		for i in range(len(x)):
			x[i]= (y_pred - y_true) * x[i]
	return x
