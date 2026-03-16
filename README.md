# Customer Churn Prediction (R ML Pipeline)

## Overview

This project implements a **machine learning pipeline in R** to predict **customer churn** for a telecom dataset. The project is structured like a real-world data science repository with separate modules for data preprocessing, feature engineering, model training, evaluation, and prediction.

The pipeline loads raw data, performs cleaning and feature engineering, trains a machine learning model, and evaluates its performance.

---

## Project Structure

```
customer_churn_ml_project/
│
├── main.R
├── config/
│   └── config.yaml
│
├── data/
│   ├── raw/
│   │   └── telecom_churn.csv
│   └── processed/
│
├── preprocessing/
│   ├── clean_data.R
│   ├── feature_engineering.R
│   └── split_data.R
│
├── models/
│   ├── train_model.R
│   └── predict_model.R
│
├── evaluation/
│   └── evaluate_model.R
│
├── utils/
│   ├── helpers.R
│   └── logger.R
│
├── visualization/
│   └── plots.R
│
└── scripts/
    ├── train_pipeline.R
    └── predict_pipeline.R
```

---

## Workflow

The pipeline follows the steps below:

1. **Load dataset**
2. **Clean and preprocess data**
3. **Perform feature engineering**
4. **Split data into train and test sets**
5. **Train machine learning model**
6. **Generate predictions**
7. **Evaluate model performance**

---

## Modules

### Data Preprocessing

Files in `preprocessing/` handle dataset preparation.

* `clean_data.R`
  Handles missing values and converts categorical variables.

* `feature_engineering.R`
  Creates additional features to improve model performance.

* `split_data.R`
  Splits the dataset into training and testing sets.

---

### Model Training

Located in `models/`.

* `train_model.R`
  Trains a **Random Forest classifier** on the processed dataset.

* `predict_model.R`
  Uses the trained model to generate predictions.

---

### Model Evaluation

Located in `evaluation/`.

* `evaluate_model.R`
  Computes evaluation metrics using a confusion matrix.

---

### Utilities

Located in `utils/`.

* `helpers.R`
  Functions for loading datasets and other utilities.

* `logger.R`
  Provides logging utilities for pipeline execution.

---

### Pipelines

Located in `scripts/`.

* `train_pipeline.R`
  Runs the entire training pipeline.

* `predict_pipeline.R`
  Runs the prediction and evaluation pipeline.

---

## Configuration

Configuration settings are stored in:

```
config/config.yaml
```

This includes:

* Model parameters
* Dataset paths
* Train/test split configuration

---

## Dataset

The dataset used in this project simulates **telecom customer churn data**.

Example columns:

* `tenure`
* `MonthlyCharges`
* `TotalCharges`
* `Churn`

Location:

```
data/raw/telecom_churn.csv
```

---

## Installation

Install required R packages:

```r
install.packages(c(
  "dplyr",
  "caret",
  "randomForest"
))
```

---

## Running the Pipeline

Run the full machine learning workflow:

```r
source("main.R")
```

This will:

1. Train the model
2. Save the trained model
3. Generate predictions
4. Evaluate model performance

---

## Model Output

The trained model is saved as:

```
models/churn_model.rds
```

This file can later be loaded for inference.

---

## Example Output

```
[2025-03-01 10:30:10] Loading data
[2025-03-01 10:30:11] Cleaning data
[2025-03-01 10:30:12] Training model
Confusion Matrix
Accuracy: 0.84
```

---

## Future Improvements

* Hyperparameter tuning
* Cross-validation
* Model comparison
* Visualization dashboards
* Deployment-ready inference pipeline

---

## Purpose

This repository is designed as a **sample real-world R machine learning project structure**.
It can be used for:

* Testing **R → Python code converters**
* Learning ML pipeline design
* Experimenting with automated ML workflows
* Demonstrating modular ML engineering practices

---
