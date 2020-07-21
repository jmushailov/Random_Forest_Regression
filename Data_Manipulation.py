# An easy way to manipulate data
class data_manipulation:
    
    def __init__ (self, dataset):
        self.dataset = dataset
        
    def explore(self):
        print("Column Names:" , self.dataset.columns)
        print(self.dataset.describe)
        self.dataset.head(10) 
        self.dataset.tail(10)
        
    def clean_data(self):
        self.dataset.replace([np.inf, -np.inf], np.nan) # Replace inf
        self.dataset = self.dataset.dropna(axis=1, how = 'any') # Drop NA's
        
    def create_xy(self, X_index_start, X_index_end, y_index_start, y_index_end, test_set_size):
        # Indicies can be 
       if not isinstance(test_set_size, float):
           raise ValueError("Test size must be float")
       else:
           from sklearn.model_selection import train_test_split
           X = self.dataset.iloc[:,slice(X_index_start, X_index_end, None)].values
           y = self.dataset.iloc[:,slice(y_index_start, y_index_end, None)].values
           X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_set_size)
           return X,y,X_train, X_test, y_train, y_test

    def data_scaling(x_to_scale, y_to_scale):
        from sklearn.preprocessing import StandardScaler
        sc = StandardScaler
        x_to_scale = sc.fit_transform(x_to_scale)
        y_to_scale = sc.fit_transform(y_to_scale)
        return x_to_scale, y_to_scale
        
