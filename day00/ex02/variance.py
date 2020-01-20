def variance(x):
	if x.size == 0:
		return None
	mean = 0.0
	total = 0.0
	for value in x:
		mean += value
	mean = mean / len(x)
	for value in x:
		total += (value - mean) * (value - mean)
	return total / len(x)
