# 🚢 Titanic Survival Prediction using Machine Learning

A machine learning classification project that predicts whether a passenger survived the Titanic disaster using demographic and ticket information.

---

## 📌 Project Overview

This project demonstrates the complete machine learning workflow:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Preprocessing
- Model Training
- Model Evaluation
- Visualization

Models Used:
- Logistic Regression
- Decision Tree Classifier

---

## 📂 Dataset

Dataset: Titanic Survival Dataset

Features include:

- Passenger Class
- Sex
- Age
- Fare
- Family Size
- Embarked Port
- etc.

Target:

- Survived (0 = No, 1 = Yes)

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 📊 Exploratory Data Analysis

Performed:

- Age Distribution
- Fare Distribution
- Passenger Class Distribution
- Survival by Gender
- Survival by Passenger Class
- Box Plot
- Correlation Heatmap

Example:

![Correlation Heatmap](Visuals/correlation_heatmap.png)

---

## ⚙ Data Preprocessing

- Dropped missing Age values using Median
- Dropped missing Embarked values using Mode
- Dropped Cabin column
- Dropped PassengerId, Name and Ticket
- Label Encoded Sex
- One-Hot Encoded Embarked
- Standardized Age and Fare
- Train/Test Split (70/30)

---

## 🤖 Models Trained

### Logistic Regression

Used as a baseline classification model.

### Decision Tree Classifier

Used to compare performance with Logistic Regression.

---

## 📈 Model Evaluation

Metrics Used:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- MAE
- MSE
- RMSE
- R2

Example:

| Model | Metrics | Score
|------|---------:|
| Logistic Regression | MAE | 24.65% |
| Decision Tree | Accuracy | 75.34% |

---

## 📷 Visualizations

### Accuracy Comparison

![Accuracy](Visuals/Accuracy.png)

### Logistic Regression Confusion Matrix

![Logistic CM](Visuals/Logistic_ConfusionMat.png)

### Decision Tree Confusion Matrix

![Tree CM](Visuals/Decision_Tree_ConfusionMat.png)

### Feature Importance

![Feature Importance](Visuals/Feature_Importance.png)

---

## 📁 Project Structure

```
Titanic-Survival-Prediction/
│
├── data/
├── Visuals/
├── Main.py
├── PreProcess.py
├── Report.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ▶ How to Run

Clone the repository

```bash
git clone https://github.com/jaswindersinghbanga111287-alt/Titanic-Survival-Predictions
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python Main.py
```

---

## 📌 Future Improvements

- Feature Engineering

---

## 👤 Author

Jaswinder Singh Banga
