from fastapi import FastAPI, Request
from pydantic import BaseModel
import pandas as pd
import pickle
import logging
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import start_http_server

start_http_server(8000)


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

with open("wine_quality_rfc_model.pkl", "rb") as f:
    model = pickle.load(f)


app = FastAPI()
instrumentator = Instrumentator().instrument(app).expose(app)


class Input(BaseModel):
    features: list[float]

feature_names = [
    'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
    'chlorides', 'free sulfur dioxide', 'total sulfur dioxide',
    'density', 'pH', 'sulphates', 'alcohol'
]


@app.post("/predict")
async def predict(input: Input, request: Request):
    try:
        data = pd.DataFrame([input.features], columns=feature_names)
        prediction = model.predict(data)

        logging.info(f"Request from {request.client.host} - Features: {input.features}")
        logging.info(f"Prediction result: {prediction[0]}")

        return {"prediction": int(prediction[0])}
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return {"error": "Prediction failed"}
