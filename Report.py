from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix,mean_absolute_error,mean_squared_error,root_mean_squared_error,r2_score,ConfusionMatrixDisplay
import matplotlib.pyplot as plt
def Classification_Report(y_test,predictions,Time):
    print("\n\n*****\tClassification Report\t*****\n\n")
    print("Time taken by Decision Tree Classifier: ",Time)
    print("Accuracy of Decision Tree Classifier: ",accuracy_score(y_test,predictions))
    print("Precesion of Decision Tree Classifier: ",precision_score(y_test,predictions))
    print("recall of Decision Tree Classifier: ",recall_score(y_test,predictions))
    print("f1 score of Decision Tree Classifier: ",f1_score(y_test,predictions))
    print ("Confision Matrix of Decision Tree Classifier:\n",confusion_matrix(y_test,predictions))

def Regression_Report(y_test,predictions,Time):
    print("\n\n*****\tLogistic Regression Report\t*****\n\n")
    print("Time taken by logistic Cla: ",Time)
    print("MAE of Logistic Regression model: ",mean_absolute_error(y_test,predictions))
    print("MSE of Logistic Regression model: ",mean_squared_error(y_test,predictions))
    print("RMSE of Logistic Regression model: ",root_mean_squared_error(y_test,predictions))
    print("R2 score of Logistic Regression model: ",r2_score(y_test,predictions))