import pandas as pd
import numpy as np
from normal_equation_model import graph_model
from mylinearregression import MyLinearRegression as MyLR

data = pd.read_csv("../resources/spacecraft_data.csv")
X_train = np.array(data[['Age','Thrust_power','Terameters']])
Y_train = np.array(data['Sell_price']).reshape(-1,1)
myLR_ne = MyLR([[1.0], [1.0], [1.0], [1.0]])
myLR_lgd = MyLR([[1.0], [1.0], [1.0], [1.0]])

#Linear Gradient Descent
myLR_lgd.fit_(X_train, Y_train, alpha = 5e-5, n_cycle = 10000)
Y_pred_lgd = myLR_lgd.predict_(X_train)
print('COST Linear gradient descent:',myLR_lgd.cost_(X_train, Y_train))

#Normal Equation
myLR_ne.normalequation_(X_train,Y_train)
Y_pred_ne = myLR_ne.predict_(X_train)
print('COST Normal equation:',myLR_ne.cost_(X_train, Y_train))

graph_model(X_train, Y_train, Y_pred_lgd, Y_pred_ne)
