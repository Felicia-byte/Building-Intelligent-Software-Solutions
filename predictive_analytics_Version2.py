#!/usr/bin/env python3
"""
Task 3: Predictive Analytics for Resource Allocation

- Uses the Breast Cancer dataset (sklearn) as a stand-in for a realistic dataset.
- Demonstrates:
  * preprocessing (scaling, label mapping)
  * training a Random Forest to predict a synthetic 'issue priority' label
  * evaluation: accuracy and F1-score
- Note: The original assignment expects a Kaggle dataset; replace the data loading section to use a Kaggle CSV if needed.
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
import joblib
import os

os.makedirs("assets", exist_ok=True)

def load_and_prepare():
    # Load dataset
    bc = load_breast_cancer()
    X = pd.DataFrame(bc.data, columns=bc.feature_names)
    y = pd.Series(bc.target)  # 0 = malignant, 1 = benign

    # For this task, we synthesize a 3-class 'priority' label from the binary target:
    # This is only illustrative. In a real issue-priority dataset, labels come from ticket metadata.
    # Mapping strategy (synthetic):
    # - If malignant (0) and mean radius > median -> 'high' priority
    # - If benign (1) and mean texture < median -> 'low' priority
    # - Else 'medium'
    radius_med = X['mean radius'].median()
    texture_med = X['mean texture'].median()

    def map_priority(row, label):
        if label == 0 and row['mean radius'] > radius_med:
            return "high"
        if label == 1 and row['mean texture'] < texture_med:
            return "low"
        return "medium"

    y_priority = [map_priority(X.loc[i], y.iloc[i]) for i in range(len(X))]
    y_priority = pd.Series(y_priority, name="priority")
    return X, y_priority

def preprocess(X_train, X_test):
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)
    return X_train_s, X_test_s, scaler

def train_and_evaluate(X, y):
    # Encode labels
    y_encoded = y.map({"low": 0, "medium": 1, "high": 2})
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded)

    X_train_s, X_test_s, scaler = preprocess(X_train, X_test)

    # Random Forest with basic hyperparameter search
    clf = RandomForestClassifier(random_state=42, n_jobs=-1)
    param_grid = {"n_estimators": [50, 100], "max_depth": [5, 10, None]}
    grid = GridSearchCV(clf, param_grid, cv=3, scoring='f1_macro', verbose=0)
    grid.fit(X_train_s, y_train)

    best = grid.best_estimator_
    y_pred = best.predict(X_test_s)

    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='macro')

    print("=== Predictive Analytics Results ===")
    print("Best params:", grid.best_params_)
    print(f"Accuracy: {acc:.4f}")
    print(f"Macro F1:  {f1:.4f}")
    print("\nClassification report:\n", classification_report(y_test, y_pred, target_names=["low","medium","high"]))
    print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))

    # Save the model and scaler for deployment
    joblib.dump(best, "assets/priority_rf.joblib")
    joblib.dump(scaler, "assets/priority_scaler.joblib")
    print("Saved model and scaler to assets/")

def main():
    X, y = load_and_prepare()
    train_and_evaluate(X, y)

if __name__ == "__main__":
    main()