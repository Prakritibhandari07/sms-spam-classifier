# SMS Spam Classifier

An NLP-based spam classifier that predicts whether a message is spam or legitimate, with a confidence score. Available two ways: a Streamlit web app for interactive use, and a FastAPI REST API for programmatic access.

## Live Demos

- **Streamlit app:** https://sms-spam-classifier-hz3uzddeyeamfbcgmktqup.streamlit.app/
- **FastAPI docs (interactive):** https://sms-spam-classifier-3pag.onrender.com/docs

> Note: the API is hosted on Render's free tier, which spins down after inactivity. The first request after idle time may take up to ~50 seconds to respond while it wakes up.

## How It Works

The model uses a TF-IDF vectorizer to convert message text into numerical features, then a trained classifier predicts spam vs. legitimate with a confidence score. Text preprocessing includes tokenization and stopword removal.

## Project Structure

```
sms-spam-classifier/
├── app.py              # Streamlit web app
├── api.py              # FastAPI REST API
├── model.pkl           # Trained classifier
├── vectorizer.pkl      # Fitted TF-IDF vectorizer
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container definition for the API
├── .dockerignore
└── spamdetection.ipynb # Model training notebook
```

## Running the API Locally

**Without Docker:**
```bash
pip install -r requirements.txt
python -m uvicorn api:app --reload
```
Then visit `http://127.0.0.1:8000/docs`.

**With Docker:**
```bash
docker build -t spam-classifier-api .
docker run -p 8000:8000 spam-classifier-api
```
Then visit `http://127.0.0.1:8000/docs`.

## API Usage

**Endpoint:** `POST /predict`

**Request:**
```json
{
  "message": "Congratulations! You've won a free prize, click here now!"
}
```

**Response:**
```json
{
  "message": "Congratulations! You've won a free prize, click here now!",
  "prediction": "spam",
  "confidence": 0.8109
}
```

**Other endpoints:**
- `GET /` — health check / status message
- `GET /health` — simple health check

## Deployment

The API is containerized with Docker and deployed on [Render](https://render.com) using their free web service tier, built directly from this repo's `Dockerfile`.

## Tech Stack

Python, Scikit-learn, NLTK, FastAPI, Uvicorn, Docker, Streamlit, Render
