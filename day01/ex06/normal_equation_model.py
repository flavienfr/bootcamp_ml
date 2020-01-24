import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def graph_model(Xpill, Y_train, Y_pred_lgd, Y_pred_ne):
	Xpill = Xpill[:,0].reshape(-1,1)
	plt.scatter(Xpill, Y_train)#trainning set  value 
	plt.scatter(Xpill, Y_pred_lgd, 10, color='red')
	plt.scatter(Xpill, Y_pred_ne, 10, color='green')
	plt.grid()
	plt.show()
