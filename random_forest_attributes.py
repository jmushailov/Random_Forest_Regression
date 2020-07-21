import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

# Random Forest Attributes
class rfa():
    
    def __init__ (self, rf):
        # constructor requires random forest object
        self.rf = rf
        
    
    def attributes(self, list_of_vars = None):
        print(" Base Estimator: ", self.rf.base_estimator_)
        print("Feature Importances: ", self.rf.feature_importances_)
        # checking for oob score
        try:
            print("OOB Score: ", self.rf.oob_score_)
        except ValueError:
            print("OOB score argument was not set to true in RF model")
            
    # This method tests optimal estimators based on OOB
    def oob_score(X,y, min_est, max_est):
        oob_list = []
        est_range = np.arange(min_est, max_est+1) # for plotting
        
        for est in range(min_est, max_est+1):
            regressor = RandomForestRegressor(n_estimators = est, min_samples_split = 20, oob_score = True)
            rf = regressor.fit(X,y)
            oob_list.append(rf.oob_score_)
            
        plt.plot(est_range, oob_list)
        plt.xlabel("Number of Estimators")
        plt.ylabel("OOB Score")
        title = "OOB Score vs. Estimators. N_min = ", min_est , ", N_max = ", max_est
        plt.title(title)
        return oob_list

    
    # This method uses the rf's features and a passed table of col names (since values are passed to RF) to show most important features
    def feature_importances(self, columns):
        return pd.DataFrame({"Feature": columns, "Importance": self.rf.feature_importances_}).sort_values(by = 'Importance', ascending = False)
        

    # This method checks the RMSE over the sample    
    def test_rmse(X,y,X_test,y_test,min_est, max_est):
        rmse_list = []
        est_range = np.arange(min_est, max_est+1) # for plotting
        
        for est in range(min_est, max_est+1): 
            regressor = RandomForestRegressor(n_estimators = est, min_samples_split = 20, oob_score = True)
            rf = regressor.fit(X,y)
            y_pred = rf.predict(X_test)
            rmse = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
            rmse_list.append(rmse)
            
        plt.plot(est_range, rmse_list)
        plt.xlabel("Number of Estimators")
        plt.ylabel("RMSE")
        title = "RMSE vs. Estimators. N_min = ", min_est , ", N_max = ", max_est
        plt.title(title)
        return rmse_list

    # Basic method to print evaluation scores of a single y test / pred
    def evaluation(y_test, y_pred):
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
        print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
        
        
