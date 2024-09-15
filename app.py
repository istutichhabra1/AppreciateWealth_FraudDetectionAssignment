from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

# Load the trained Gradient Boosting model
model = joblib.load('gradient_boosting_model.pkl')

# Create a FastAPI app
app = FastAPI()

# Define the input data model
class TransactionInput(BaseModel):
    amt: float
    lat: float
    long: float
    city_pop: int
    merch_lat: float
    merch_long: float
    hour: int
    day: int
    category_personal_care: int
    category_health_fitness: int
    gender_M: int
    merchant_fraud_Kirlin_and_Sons: int
    merchant_fraud_Sporer_Keebler: int
    merchant_fraud_Swaniawski_Nitzsche_and_Welch: int

# Preprocess the input to match the model features
def preprocess(input_data: TransactionInput):
    # Convert the input data to a NumPy array (or pandas DataFrame if needed)
    data = np.array([[
        input_data.amt,
        input_data.lat,
        input_data.long,
        input_data.city_pop,
        input_data.merch_lat,
        input_data.merch_long,
        input_data.hour,
        input_data.day,
        input_data.category_personal_care,
        input_data.category_health_fitness,
        input_data.gender_M,
        input_data.merchant_fraud_Kirlin_and_Sons,
        input_data.merchant_fraud_Sporer_Keebler,
        input_data.merchant_fraud_Swaniawski_Nitzsche_and_Welch
    ]])

    return data

# Define the prediction endpoint
@app.post("/predict")
def predict(input_data: TransactionInput):
    # Preprocess the input data
    processed_data = preprocess(input_data)

    # Make a prediction using the loaded model
    prediction = model.predict(processed_data)

    # Return the prediction (0 for non-fraud, 1 for fraud)
    return {"prediction": int(prediction[0])}

# Run the app with uvicorn: `uvicorn app:app --reload`
