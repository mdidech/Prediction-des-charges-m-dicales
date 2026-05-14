import pandas as pd
from joblib import load

model=load("artifacts/model_xgb.pkl")



def predict(to_predict):
    data=pd.DataFrame([to_predict])
    predication=model.predict(data)
    return float(predication[0])