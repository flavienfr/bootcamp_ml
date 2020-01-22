import math
import numpy as np

def log_loss_(y_true, y_pred, m, eps=1e-15):
	vec = 0
	if type(y_true) == list:
		for i in range(len(y_true)):
			vec += -y_true[i] * math.log(y_pred[i] + eps) - (1 - y_true[i]) * math.log(1 - y_pred[i] + eps)
	else:
		vec = -y_true * math.log(y_pred + eps) - (1 - y_true) * math.log(1 - y_pred + eps)
	total = (1 / m) * vec
	return total
