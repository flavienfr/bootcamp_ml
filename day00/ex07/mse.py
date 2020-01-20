def mse(y, y_hat):
	if len(y) == 0 or len(y_hat) == 0 or len(y) != len(y_hat):
		return None
	total = 0.0
	for i in range(len(y)):
		total += (y_hat[i] - y[i]) * (y_hat[i] - y[i])
	return total / len(y)
