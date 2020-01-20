import numpy as np
from mat_mat_prod import mat_mat_prod
'''
W = np.array([
	[ -8, 8, -6, 14, 14, -9, -4],
	[ 2, -11, -2, -11, 14, -2, 14],
	[-13, -2, -5, 3, -8, -4, 13],
	[ 2, 13, -14, -15, -14, -15, 13],
	[ 2, -1, 12, 3, -7, -3, -6]])

Z = np.array([
	[ -6, -1, -8, 7, -8],
	[ 7, 4, 0, -10, -10],
	[ 7, -13, 2, 2, -11],
	[ 3, 14, 7, 7, -4],
	[ -1, -3, -8, -4, -14],
	[ 9, -14, 9, 12, -7],
	[ -9, -4, -10, -3, 6]])
'''
W = np.array([
	[ 1, 2, 3],
	[ 4, 5, 6]])

Z = np.array([
	[ 7, 8],
	[ 9, -1],
	[-2, -3]])
'''
W = np.array([
	[ 3, 2, 1, 5],
	[ 9, 1, 3, 0]])

Z = np.array([
	[ 2, 9, 0],
	[ 1, 3, 5],
	[ 2, 4, 7],
	[ 8, 1, 5]])
'''
res = mat_mat_prod(W, Z)
print(res)

res = W.dot(Z)
print(res)

res = mat_mat_prod(Z,W)
print(res)

res = Z.dot(W)
print(res)
