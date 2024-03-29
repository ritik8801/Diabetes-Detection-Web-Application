from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score, KFold
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt 

class ModelBuilding:

    def __init__(self, df, path=None, X_train=None, X_test=None,
    y_train=None, y_test=None):
        self.data = df
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.y_pred = None
        self.split()
        self.train()
        self.predict()


    def split(self):
        X = self.data[['Pregnancies', 'Glucose', 'BloodPressure',
       'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age']]
        y = self.data['Outcome']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y,
        test_size=0.3)
    
    def train(self):
        self.rcb = RandomForestClassifier()
        self.rcb.fit(self.X_train, self.y_train)
        score = self.rcb.score(self.X_train, self.y_train)
        print("Training score: ", score)
    
    def predict(self):
        self.y_pred = self.rcb.predict(self.X_test)
        mse = mean_squared_error(self.y_test, self.y_pred)
        print(mse)
