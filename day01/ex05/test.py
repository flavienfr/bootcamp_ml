import pandas as pd
import numpy as np
from mylinearregression import MyLinearRegression as MyLR
from multi_linear_model import linear_model

data = pd.read_csv("../resources/spacecraft_data.csv")

def SingleLinearRegression(X, Y, alpha, n_cycle):
	X_train = np.array(data[X]).reshape(-1,1)
	Y_train = np.array(data[Y]).reshape(-1,1)
	myLR_age = MyLR([[1000.0], [-1.0]])

	myLR_age.fit_(X_train, Y_train, alpha, n_cycle)
	Y_pred = myLR_age.predict_(X_train)
	print(myLR_age.cost_(X_train, Y_train))
	linear_model(X_train, Y_train, Y_pred)

def MultiLinearRegression(X, Y, alpha, n_cycle):
	X_train = np.array(data[X])
	Y_train = np.array(data[['Sell_price']])
	my_lreg = MyLR([[1.0], [1.0], [1.0], [1.0]])

	my_lreg.fit_(X_train,Y_train, alpha, n_cycle)
	Y_pred = my_lreg.predict_(X_train)
	print(my_lreg.cost_(X_train, Y_train))
	linear_model(X_train, Y_train, Y_pred)

# Part One: single linear regression
#SingleLinearRegression('Age', 'Sell_price', 0.01, 100000)
#SingleLinearRegression('Thrust_power', 'Sell_price', 0.0003, 500000)
#SingleLinearRegression('Terameters', 'Sell_price', 0.0004, 130000)

# Part Two: Multilinear Regression
#X = ['Age','Thrust_power','Terameters']
Y = ['Sell_price']
#MultiLinearRegression(X, Y, 1e-4, 600000)
#X = ['Thrust_power','Age','Terameters']
#MultiLinearRegression(X, Y, 1e-4, 600000)
X = ['Terameters','Thrust_power','Age']
MultiLinearRegression(X, Y, 1e-4, 600000)
