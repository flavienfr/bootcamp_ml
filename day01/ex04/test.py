import pandas as pd
import numpy as np
#from sklearn.metrics import mean_squared_error
from mylinearregression import MyLinearRegression as MyLR
from linear_model import linear_model, cost_model

data = pd.read_csv('../resources/are_blue_pills_magics.csv')
Xpill = np.array(data['Micrograms']).reshape(-1,1)
Yscore = np.array(data['Score']).reshape(-1,1)

linear_model1 = MyLR(np.array([[0.0], [0.0]]))

linear_model1.theta =linear_model1.fit_(Xpill, Yscore, alpha = 0.05, n_cycle = 1000)

Y_model1 = linear_model1.predict_(Xpill)

cost_elem = linear_model1.cost_(Xpill, Yscore)

#cost_model(linear_model1.theta, cost_elem)

linear_model(Xpill, Y_model1, Yscore)
print(linear_model1.theta)

#print(linear_model1.mse_(Yscore, Y_model1))

#print(mean_squared_error(Yscore, Y_model1))

#print(linear_model2.mse_(Yscore, Y_model2))

#print(mean_squared_error(Yscore, Y_model2))