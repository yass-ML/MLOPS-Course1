from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

from fastapi import FastAPI, APIRouter
import joblib

app = FastAPI()

# House regression model
house_router = APIRouter(prefix="/house")

HOUSE_MODEL_PATH = "regression.joblib"
house_model = joblib.load(HOUSE_MODEL_PATH)

@house_router.get("/predict")
def predict_get():
    return {"y_pred": 2}


@house_router.post("/predict")
def predict_post(data: dict):
    input_data = [[data['size'], data['nb_rooms'], data['garden']]]
    prediction = house_model.predict(input_data)
    return {"y_pred": float(prediction[0])}


# NLP model using T5 (example: text summarization)
nlp_router = APIRouter(prefix="/nlp")


# Load tokenizer and model (t5-small for demo, switch to preferred T5 or BERT)
tokenizer = AutoTokenizer.from_pretrained("t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")


@nlp_router.get("/summarize")
def summarize_get():
    sample_text = "The quick brown fox jumps over the lazy dog. This is a sample text for summarization."
    inputs = tokenizer.encode("summarize: " + sample_text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return {"summary": summary}


@nlp_router.post("/summarize")
def summarize_post(data: dict):
    text = data.get("text", "")
    if not text:
        return {"error": "No text provided"}

    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return {"summary": summary}


app.include_router(house_router)
app.include_router(nlp_router)
