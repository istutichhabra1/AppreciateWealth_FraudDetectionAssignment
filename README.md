
# Fraud Detection API

This repository is part of a machine learning project that predicts fraudulent transactions using a Gradient Boosting model. The model is served via a **FastAPI** web API, which accepts transaction data in JSON format and returns a prediction on whether the transaction is fraudulent or not.

## Repository Structure

- `Assignment.ipynb`: Jupyter Notebook containing the code for data preprocessing, model training, and evaluation of various machine learning models.
- `app.py`: FastAPI application that serves the fraud detection model via an API.
- `requirements.txt`: File containing the necessary dependencies to run the project.
- `gradient_boosting_model.pkl`: The trained Gradient Boosting model file used by the API to make predictions.

## Features

- **Machine Learning Models**: The notebook (`Assignment.ipynb`) contains code for building and evaluating different models such as Logistic Regression, Decision Tree, Random Forest, and Gradient Boosting.
- **FastAPI Application**: The `app.py` file hosts the trained model as an API endpoint, allowing users to input transaction data and receive a prediction.
- **Real-time Prediction**: The API takes JSON inputs and returns a prediction for fraud detection (0 for non-fraudulent and 1 for fraudulent).
- **JSON Input Format**: The API accepts a structured JSON format as input for real-time predictions.

## How to Run

### 1. Clone the repository

```bash
[git clone https://github.com/your-username/fraud-detection-api.git
cd fraud-detection-api](https://github.com/istutichhabra1/AppreciateWealth_FraudDetectionAssignment.git)
```

### 2. Install dependencies

Make sure you have Python 3.8+ installed. Install the required packages using the following command:

```bash
pip install -r requirements.txt
```

### 3. Running the FastAPI app

Run the FastAPI app locally using Uvicorn:

```bash
uvicorn app:app --reload
```

This will start the server at `http://127.0.0.1:8000`. You can view the automatically generated API documentation at `http://127.0.0.1:8000/docs`.

### 4. Making Predictions

Send a POST request to the `/predict` endpoint with the required transaction data in JSON format. Example request using cURL:

```bash
curl -X 'POST'   'http://127.0.0.1:8000/predict'   -H 'Content-Type: application/json'   -d '{
    "amt": 29.84,
    "lat": 40.3207,
    "long": -110.436,
    "city_pop": 302,
    "merch_lat": 39.4505,
    "merch_long": -109.96,
    "hour": 12,
    "day": 21,
    "category_personal_care": 1,
    "category_health_fitness": 0,
    "gender_M": 0,
    "merchant_fraud_Kirlin_and_Sons": 1,
    "merchant_fraud_Sporer_Keebler": 0,
    "merchant_fraud_Swaniawski_Nitzsche_and_Welch": 0
}'
```

You will receive a JSON response indicating whether the transaction is fraudulent or not:

```json
{
  "prediction": 1
}
```

## Dependencies

The dependencies required to run the project are listed in the `requirements.txt` file. The key libraries are:

- **FastAPI**: For building and hosting the API.
- **Uvicorn**: ASGI server for serving the FastAPI application.
- **Scikit-learn**: For machine learning algorithms and preprocessing.
- **Pandas**: For data manipulation.
- **NumPy**: For numerical operations.
- **Joblib**: For saving and loading machine learning models.

To install them, run:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License. Feel free to modify and use it for your own projects.
