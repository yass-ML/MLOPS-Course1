from fastapi import FastAPI
import joblib

app = FastAPI()

HOUSE_MODEL_PATH = "regression.joblib"

@app.get("/predict")
def predict_get():
    return {"y_pred": 2}


@app.post("/predict")
def predict_post(data: dict):
    model = joblib.load(HOUSE_MODEL_PATH)
    input_data = [[data['size'], data['nb_rooms'], data['garden']]]
    prediction = model.predict(input_data)
    return {"y_pred": float(prediction[0])}
