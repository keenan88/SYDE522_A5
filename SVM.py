try:
    from IPython import get_ipython
    get_ipython().magic('clear')
    get_ipython().magic('reset -f')
except:
    print("Could not clear console and varaiables")

from Data_to_matrix import x_train, x_test, y_train, y_test
import numpy as np
from sklearn.svm import SVR

kernel_types = ['linear', 'poly', 'rbf', 'sigmoid']

for kernel_type in kernel_types:

    svm_regressor = SVR(kernel = kernel_type)  # You can choose different kernels like 'linear', 'rbf', etc.
    
    svm_regressor.fit(x_train, y_train)
    predictions = svm_regressor.predict(x_test)
    
    rmse = np.sqrt(np.mean(np.square(predictions - y_test)))
    
    print(kernel_type, rmse)



