import pandas as pd
import numpy as np
from log_reg import LogisticRegressionBatchGd

df_train = pd.read_csv('../resources/dataset/train_dataset_clean.csv', delimiter=',', header=None, index_col=False)
x_train, y_train = np.array(df_train.iloc[:, 1:82]), np.array(df_train.iloc[:, 0])
df_test = pd.read_csv('../resources/dataset/test_dataset_clean.csv', delimiter=',', header=None, index_col=False)
x_test, y_test = np.array(df_test.iloc[:, 1:82]), df_test.iloc[:, 0]
print(y_train)
model = LogisticRegressionBatchGd(alpha=0.01, max_iter=10, verbose=True, learning_rate='constant')

#model.predict(x_train)

#model.fit(x_train, y_train)

'''
print(f'Score on train dataset : {model.score(x_train, y_train)}')
y_pred = model.predict(x_test)
print(f'Score on test dataset : {(y_pred == y_test).mean()}')
'''
