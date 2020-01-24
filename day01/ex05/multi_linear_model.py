import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def linear_model(Xpill, Y_train, Y_pred):
	Xpill = Xpill[:,0].reshape(-1,1)
	plt.scatter(Xpill, Y_train)
	plt.scatter(Xpill, Y_pred, 10,color='red')
	#plt.plot(Xpill, Y_pred, color='red')
	plt.grid()
	plt.show()
