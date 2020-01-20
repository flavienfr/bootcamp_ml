def sum_(x, f):
	if x.size == 0 or not f:
		return None
	total = 0.0
	try:
		for value in x:
			total += f(value)
		return total
	except (RuntimeError, TypeError, NameError):
		print('This function should not raise any Exception.')