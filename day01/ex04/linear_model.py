import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def linear_model(Xpill, Y_model, Y_pred):
	plt.scatter(Xpill, Y_pred)
	plt.plot(Xpill, Y_model, color='red')
	plt.grid()
	plt.show()

def	cost_model(theta, cost_elem):
	#plt.scatter(Xpill, cost_elem)
	plt.plot(theta, cost_elem, color='red')
	plt.grid()
	plt.show()