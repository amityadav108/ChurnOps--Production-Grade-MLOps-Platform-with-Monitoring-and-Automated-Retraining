import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "model_registry",
    "production",
    "model.pkl"
)

PREPROCESSOR_PATH = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "preprocessor.pkl"
)

production_model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)


def predict(data):

    columns = [
        "gender",
        "SeniorCitizen",
        "Partner",
        "Dependents",
        "tenure",
        "PhoneService",
        "MultipleLines",
        "InternetService",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
        "Contract",
        "PaperlessBilling",
        "PaymentMethod",
        "MonthlyCharges",
        "TotalCharges"
    ]

    df = pd.DataFrame(data, columns=columns)

    transformed_data = preprocessor.transform(df)

    prediction = production_model.predict(transformed_data)

    probability = production_model.predict_proba(transformed_data)

    return prediction[0], probability[0][1]