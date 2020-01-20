def mean(x):
	if x.size == 0:
		return None
	total = 0.0
	for value in x:
		total += value
	return total / len(x)
