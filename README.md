# 🚀 ChurnOps: Production-Grade Customer Churn Prediction Platform

An end-to-end **Production MLOps Platform** for customer churn prediction built with **Python, Scikit-Learn, LightGBM, MLflow, FastAPI, Docker, Monitoring, Automated Retraining, and Batch Inference**.

This project demonstrates the complete machine learning lifecycle from raw data preprocessing to production deployment and automated model management.

---

# 📌 Project Highlights

✅ Data preprocessing pipeline
✅ Feature engineering
✅ Multiple ML models comparison
✅ MLflow experiment tracking
✅ Model registry & versioning
✅ FastAPI inference API
✅ Docker containerization
✅ Monitoring & logging
✅ Automated retraining pipeline
✅ Drift detection
✅ Batch inference pipeline
✅ Production-ready architecture

---

# 🏗️ Architecture

```text
Raw Data
    ↓
Data Preprocessing
    ↓
Feature Engineering
    ↓
Model Training
    ↓
MLflow Experiment Tracking
    ↓
Model Registry
    ↓
FastAPI API
    ↓
Docker Container
    ↓
Monitoring & Logging
    ↓
Drift Detection
    ↓
Automated Retraining
    ↓
Batch Inference
```

---

# 🛠 Tech Stack

### Programming

* Python

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-Learn
* XGBoost
* LightGBM

### Experiment Tracking

* MLflow

### API Development

* FastAPI
* Uvicorn

### Containerization

* Docker

### Serialization

* Joblib

### Monitoring

* Logging
* Drift Detection

---

# 📂 Project Structure

```text
ChurnOps/
│
├── notebooks/
│     Notebook_1_Data_Preprocessing.ipynb
│     Notebook_2_Feature_Engineering.ipynb
│     Notebook_3_Model_Training.ipynb
│     ...
│     Notebook_13_Batch_Inference.ipynb
│
├── app/
│     main.py
│     predictor.py
│     schema.py
│
├── models/
│     best_model.pkl
│     preprocessor.pkl
│
├── model_registry/
│     production/
│
├── monitoring/
│     prediction_logs.csv
│     retraining_logs.csv
│
├── artifacts/
│
├── batch_predictions/
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📘 Notebook Overview

---

## Notebook 1 — Data Preprocessing

### Features

* Missing value handling
* Data cleaning
* Train-test split

---

## Notebook 2 — Feature Engineering

### Features

* Categorical encoding
* Numerical scaling
* ColumnTransformer pipeline

---

## Notebook 3 — Model Training

Trained:

* Logistic Regression
* Random Forest
* XGBoost
* LightGBM

---

## Notebook 4 — Model Evaluation

Metrics:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

---

## Notebook 5 — Model Comparison

Compared all models and selected the best-performing model.

---

## Notebook 6 — Model Saving

Saved:

```python
best_model.pkl
preprocessor.pkl
```

---

## Notebook 7 — MLflow Experiment Tracking

### Added

* Experiment tracking
* Metrics logging
* Parameters logging
* Artifact storage

---

## Notebook 8 — MLflow Model Registry

### Added

* Model versioning
* Production model management
* Model lifecycle tracking

---

## Notebook 9 — FastAPI Inference API

Endpoints:

### Health Check

```http
GET /health
```

### Prediction

```http
POST /predict
```

---

## Notebook 10 — Docker Containerization

### Added

* Dockerfile
* Reproducible environment
* Production container

Run:

```bash
docker build -t churnops-api .
docker run -p 8000:8000 churnops-api
```

---

## Notebook 11 — Monitoring & Logging

### Added

* Request logging
* Prediction logging
* Exception handling
* Health endpoint
* Production observability

---

## Notebook 12 — Automated Retraining Pipeline

### Added

* Performance monitoring
* Drift detection
* Retraining trigger
* Model comparison
* Model promotion
* Retraining logs

### Lifecycle

```text
User Predictions
       ↓
Prediction Logs
       ↓
Performance Monitoring
       ↓
Drift Detection
       ↓
Retraining Trigger
       ↓
Train New Model
       ↓
Compare Models
       ↓
Promote Best Model
```

---

## Notebook 13 — Batch Inference Pipeline

### Added

* Offline prediction
* Batch scoring
* CSV reports
* Large-scale inference

Pipeline:

```text
CSV File
     ↓
Load Model
     ↓
Batch Prediction
     ↓
Save Predictions
     ↓
Business Report
```

---

# 📊 Models Used

| Model               | Description       |
| ------------------- | ----------------- |
| Logistic Regression | Baseline model    |
| Random Forest       | Ensemble model    |
| XGBoost             | Gradient boosting |
| LightGBM            | Production model  |

---

# 🚀 API Example

### Request

```json
{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "Yes",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 89.5,
  "TotalCharges": 1250.75
}
```

### Response

```json
{
  "prediction": 1,
  "probability": 0.6023
}
```

---

# ▶️ Installation

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/churnops-production-mlops-platform.git
cd churnops-production-mlops-platform
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run API:

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://localhost:8000/docs
```

---

# 🐳 Docker

Build image:

```bash
docker build -t churnops-api .
```

Run container:

```bash
docker run -p 8000:8000 churnops-api
```

---

# 🎯 Skills Demonstrated

### Machine Learning

* Feature Engineering
* Model Training
* Model Evaluation
* Model Selection

### MLOps

* MLflow
* Model Registry
* Monitoring
* Drift Detection
* Automated Retraining
* Batch Inference

### Deployment

* FastAPI
* Docker

### Software Engineering

* Modular Code Structure
* Logging
* Exception Handling

---

# 📈 Future Improvements

* GitHub Actions CI/CD
* Kubernetes Deployment
* Prometheus Monitoring
* Grafana Dashboard
* AWS Deployment

---

# 👨‍💻 Author

**Amit Yadav**

Aspiring Machine Learning Engineer | Generative AI Enthusiast | MLOps Practitioner

---

⭐ If you found this project useful, consider giving it a star.
