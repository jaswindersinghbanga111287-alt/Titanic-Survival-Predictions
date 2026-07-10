import Report
import PreProcess
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import time
df=pd.read_csv("data/Titanic-Dataset.csv")
df=PreProcess.EDA(df)
x=df.drop("Survived",axis=1)
y=df["Survived"]
x_train,x_test,y_train,y_test=train_test_split(
    x,
    y,
    test_size=.3,
    random_state=42
)
LogRegmodel=LogisticRegression()
treemodel=DecisionTreeClassifier()
LogRegmodel.fit(x_train,y_train)
treemodel.fit(x_train,y_train)
print("Training Features: ",x_train.shape)
print("Testing Features: ",x_test.shape)
print("Training Labels: ",y_train.shape)
print("Testing Labels: ",y_test.shape)
start=time.time()
lg=LogRegmodel.predict(x_test)
Report.Regression_Report(y_test,lg,time.time()-start)
start=time.time()
t=treemodel.predict(x_test)
Report.Classification_Report(y_test,t,time.time()-start)