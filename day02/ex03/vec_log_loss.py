import numpy as np

def vec_log_loss_(y_true, y_pred, m, eps=1e-15):
	return (-1 / m) * (np.dot(y_true, np.log(y_pred + eps)) + np.dot((1 - y_true), np.log(1 - y_pred + eps)))
