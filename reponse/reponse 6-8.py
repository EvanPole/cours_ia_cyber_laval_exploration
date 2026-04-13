import joblib
import numpy as np
from skrub.datasets import fetch_midwest_survey
from sklearn.metrics import classification_report, confusion_matrix, recall_score
from sklearn.model_selection import cross_validate
from midwest_survey_models.transformers import NumericalStabilizer

dataset = fetch_midwest_survey()
X = dataset.X
y = dataset.y

y = y.apply(lambda x: "North Central" if x in ["East North Central", "West North Central"] else "other")

sample_idx = X.sample(n=1000, random_state=1).index
X_train = X.loc[sample_idx].reset_index(drop=True)
y_train = y.loc[sample_idx].reset_index(drop=True)
X_test = X.drop(sample_idx).reset_index(drop=True)
y_test = y.drop(sample_idx).reset_index(drop=True)

model_lr = joblib.load("../model_logistic_regression.pkl")
model_rf = joblib.load("../model_random_forest.pkl")
model_gb = joblib.load("../model_gradient_boosting.pkl")

models = {"Logistic Regression": model_lr, "Random Forest": model_rf, "Gradient Boosting": model_gb}

print("Question 6 :")


for name, model in models.items():
    y_pred = model.predict(X_test)
    recall = recall_score(y_test, y_pred, pos_label="North Central")
    print(f"\n--- {name} ---")
    print(classification_report(y_test, y_pred, target_names=["North Central", "other"]))
    print(f"Recall (North Central) : {recall:.4f}")


print("Question 7 : ")


for name, model in models.items():
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred, labels=["North Central", "other"])
    tp, fn, fp, tn = cm[0][0], cm[0][1], cm[1][0], cm[1][1]
    gain = tp * 5 + tn * 2 + fp * (-10) + fn * (-1)
    print(f"\n--- {name} ---")
    print(f"TP={tp}, FN={fn}, FP={fp}, TN={tn}")
    print(f"Gain total : {gain}")

print("Question 8 :")

for name, model in models.items():
    cv_results = cross_validate(model, X, y, cv=5, scoring="accuracy", return_train_score=True)
    train_mean = cv_results["train_score"].mean()
    test_mean = cv_results["test_score"].mean()
    gap = train_mean - test_mean
    print(f"\n--- {name} ---")
    print(f"Score train moyen : {train_mean:.4f}")
    print(f"Score test moyen  : {test_mean:.4f}")
    print(f"Écart (overfitting) : {gap:.4f}")
