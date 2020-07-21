#Examples of class utilization

# ~~~ Using the FRED class
import get_fred
list_for_fred = ['unrate','PCU3255103255107', 'houst', 'dspic96']
fred_variables = get_fred.get_fred(list_for_fred)
dat = pd.merge(dat, fred_variables, on = 'date')

# ~~~ Using the attributes class
import random_forest_attributes as rfa

# Plot OOB over set of estimators to see how it adjusts with different n 
rfa.rfa.oob_score(X_train, y_train, 99,100)
# Plot RMSE over set of estimators to see how it adjusts with different n 
rfa.rfa.test_rmse(X_train, y_train, X_test, y_test, 99,101)
# Feature analysis. Since it takes self as a parameter, need to pass the RF to the object
features_df = rfa.rfa(rf).feature_importances(x_cols)
# Basic evaluation of results
rfa.rfa.evaluation(y_test, y_pred)
