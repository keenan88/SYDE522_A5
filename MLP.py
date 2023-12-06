try:
    from IPython import get_ipython
    get_ipython().magic('clear')
    get_ipython().magic('reset -f')
except:
    print("Could not clear console and varaiables")

from Data_to_matrix import x_train, x_test, y_train, y_test
import numpy as np
from sklearn import neural_network


mlp = neural_network.MLPRegressor(
    hidden_layer_sizes=(200,100), # one hidden layer with 20 features 
    activation='relu',        # rectified linear
    learning_rate_init=1e-2,  # learning rate
    max_iter=5000,            # number of iterations
    early_stopping=True,      # stop training if validation data gets worse
    random_state=0            # random number seed for initialization
)           

mlp.fit(x_train, y_train)
predictions = mlp.predict(x_test)

rmse = np.sqrt(np.mean(np.square(predictions - y_test)))

print("MLP Regressor", rmse)





