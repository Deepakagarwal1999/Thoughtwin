from sklearn.metrics import accuracy_score
import pandas as pd
from pycaret.classification import load_model 

df = pd.read_csv('test_set.csv')

# Give y_test to the function as ground truth label

saved_lr = load_model('saved_lr_model')
pred = saved_lr.predict(df)
def performance(y_test,pred):
    acc = accuracy_score(y_test,pred)
    return acc
