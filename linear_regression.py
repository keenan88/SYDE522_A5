try:
    from IPython import get_ipython
    get_ipython().magic('clear')
    get_ipython().magic('reset -f')
except:
    print("Could not clear console and varaiables")

from Data_to_matrix import x_train, x_test, y_train, y_test
import numpy as np


X = np.matrix(x_train)
Y = np.matrix(y_train).T

W = np.linalg.pinv(X.T * X) * X.T * Y

y_predict = x_test * W

rmse = np.sqrt(np.mean(np.square(y_predict.T - y_test)))

print(rmse)

