from fastapi import FastAPI
from app.schema import CustomerData
from app.predictor import predict

app = FastAPI()


# Fix those repeated 404 requests
@app.get("/hybridaction/zybTrackerStatisticsAction")
def tracker():
    return {"status": "ok"}


@app.get("/")
def home():
    return {"message": "ChurnOps API Running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict_customer(data: CustomerData):

    values = [[
        data.gender,
        data.SeniorCitizen,
        data.Partner,
        data.Dependents,
        data.tenure,
        data.PhoneService,
        data.MultipleLines,
        data.InternetService,
        data.OnlineSecurity,
        data.OnlineBackup,
        data.DeviceProtection,
        data.TechSupport,
        data.StreamingTV,
        data.StreamingMovies,
        data.Contract,
        data.PaperlessBilling,
        data.PaymentMethod,
        data.MonthlyCharges,
        data.TotalCharges
    ]]

    prediction, probability = predict(values)

    return {
    "prediction": int(prediction),
    "probability": round(float(probability), 4)
    }