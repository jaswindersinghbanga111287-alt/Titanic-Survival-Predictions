import pandas as pd
from sklearn.preprocessing import StandardScaler
def EDA(dataFrame):
    dataFrame.drop(columns=["PassengerId","Name","Ticket","Cabin"],inplace=True)
    dataFrame["Sex"]=dataFrame["Sex"].map({
        "male":1,
        "female":0
    })
    dataFrame=pd.get_dummies(dataFrame,columns=["Embarked"],drop_first=True)
    dataFrame=dataFrame.dropna()
    scale=StandardScaler()
    dataFrame["Age"]=scale.fit_transform(dataFrame[["Age"]])
    dataFrame["Fare"]=scale.fit_transform(dataFrame[["Fare"]])
    return dataFrame