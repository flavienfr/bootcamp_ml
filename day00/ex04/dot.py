def dot(x, y):
	if x.size == 0 or y.size == 0 or x.size != y.size:
		return None
	total = 0.0
	for i in range(x.size):
		total += x[i] * y[i]
	return total
