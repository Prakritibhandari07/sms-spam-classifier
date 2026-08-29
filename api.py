from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib

# ---------------------------------------------------------
# Load the trained model and vectorizer ONCE at startup
# (not on every request — that would be slow and wasteful)
# ---------------------------------------------------------
MODEL_PATH = "model.pkl"
VECTORIZER_PATH = "vectorizer.pkl"

try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
except FileNotFoundError as e:
    raise RuntimeError(
        f"Could not load model files: {e}. "
        f"Make sure '{MODEL_PATH}' and '{VECTORIZER_PATH}' are in this folder."
    )

app = FastAPI(
    title="Spam Classifier API",
    description="Predicts whether a message is spam or legitimate, with a confidence score.",
    version="1.0.0",
)


# ---------------------------------------------------------
# Request/response schemas (this is what makes FastAPI nice —
# it auto-validates input and auto-generates docs from these)
# ---------------------------------------------------------
class MessageRequest(BaseModel):
    message: str


class PredictionResponse(BaseModel):
    message: str
    prediction: str          # "spam" or "not spam"
    confidence: float        # 0.0 to 1.0


# ---------------------------------------------------------
# Routes
# ---------------------------------------------------------
@app.get("/")
def root():
    return {"status": "ok", "message": "Spam Classifier API is running. See /docs for usage."}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/predict", response_model=PredictionResponse)
def predict(request: MessageRequest):
    if not request.message or not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    # Transform the input text using the SAME vectorizer used during training
    features = vectorizer.transform([request.message])

    # Predict class and probability
    prediction = model.predict(features)[0]
    probabilities = model.predict_proba(features)[0]

    # Assumes label encoding: 0 = not spam, 1 = spam (adjust if yours differs)
    is_spam = bool(prediction == 1)
    confidence = float(probabilities[1] if is_spam else probabilities[0])

    return PredictionResponse(
        message=request.message,
        prediction="spam" if is_spam else "not spam",
        confidence=round(confidence, 4),
    )
