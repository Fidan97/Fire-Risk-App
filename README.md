# Industrial Fire & Accident Risk Predictor

## Project Overview

This project focuses on predicting industrial accidents.

**Dataset Information:**
- **Rows:** 100,000
- **Columns:** 20
- **Target:** Accident
- **Problem Type:** Binary Classification
- **Classes:** 0 (Safe), 1 (Accident)

The dataset contains information about factory conditions, temperature, pressure, gas levels, machine age, maintenance intervals, worker experience, and safety training.

**Main Objective:** Develop a machine learning model that can identify potential industrial accidents with high recall, minimizing missed accident cases.

---

## Exploratory Data Analysis (EDA)

### Data Quality Analysis

- **Missing Values:** 2,000 missing values in Workers (2%).
- **Duplicate Rows:** No duplicates found.
- **Outliers:** 508 outliers detected in Pressure.
- **Data Types:** Numerical and categorical features.
- **Class Imbalance:** Approximately 4.09% accident cases.

### Key Findings

- Temperature and Service_Days are important predictive features.
- Pressure also contributes significantly to accident prediction.
- Seasonal patterns were investigated.
- Correlation analysis was performed.
- **Problem Type:** Binary Classification
- **Classes:** 0 (Safe), 1 (Accident)

The dataset contains information about factory conditions, temperature, pressure, gas levels, machine age, maintenance intervals, worker experience, and safety training.

**Main Objective:** Develop a machine learning model that can identify potential industrial accidents with high recall, minimizing missed accident cases.

---

## Exploratory Data Analysis (EDA)

### Data Quality Analysis

- **Missing Values:** 2,000 missing values in Workers (2%).
- **Duplicate Rows:** No duplicates found.
- **Outliers:** 508 outliers detected in Pressure.
- **Data Types:** Numerical and categorical features.
- **Class Imbalance:** Approximately 4.09% accident cases.

### Key Findings

- Temperature and Service_Days are important predictive features.
- Pressure also contributes significantly to accident prediction.
- Seasonal patterns were investigated.
- Correlation analysis was performed.
---

## Model Selection & Training

Three machine learning algorithms were evaluated:

1. **Logistic Regression**
2. **Decision Tree**
3. **Random Forest**

### Training Strategy

- Used Scikit-learn Pipelines and ColumnTransformer.
- Applied `class_weight="balanced"` to handle class imbalance.
- Used stratified train-validation-test splitting.
- Evaluated models using Precision, Recall, F1-Score and ROC-AUC.
- Optimized classification thresholds using Precision-Recall curves.

---

## Model Performance Comparison

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.945 | 0.425 | 0.962 | 0.589 | 0.989 |
| Decision Tree | 0.926 | 0.353 | 0.965 | 0.517 | 0.971 |
| Random Forest | 0.976 | 0.826 | 0.526 | 0.643 | 0.988 |

### Key Observations

- **Logistic Regression:** Achieved the highest Recall and ROC-AUC.
- **Decision Tree:** Achieved high Recall but lower Precision.
- **Random Forest:** Achieved the highest Accuracy, Precision and F1-Score.

---
---

## Threshold Optimization

Optimized classification thresholds to achieve approximately 98% Recall.

**Selected Model:** Logistic Regression.

## Feature Importance

Top features:
- Temperature
- Service_Days
- Pressure
- Season
- Machine Age

## Technologies Used

Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Streamlit.

## Conclusion

Machine learning models were developed to predict industrial accidents, prioritizing high accident detection rates.

**Note:** This project is designed for decision support and does not replace professional safety systems.