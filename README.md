# 📩 SMS/Email Spam Classifier

A Machine Learning web application that classifies SMS and email messages as **Spam** or **Not Spam (Ham)** using **Natural Language Processing (NLP)** and a **Multinomial Naive Bayes** classifier. The application is built with **Python**, **Scikit-learn**, **NLTK**, and **Streamlit**.

---

## 🚀 Live Demo

Check out the deployed app here:
https://sms-spam-classifier-hz3uzddeyeamfbcgmktqup.streamlit.app/

## 📌 Features

- Detects Spam and Ham messages
- Interactive Streamlit web interface
- Text preprocessing using NLP
- Stopword removal
- Stemming using Porter Stemmer
- TF-IDF Vectorization
- Fast real-time prediction
- Lightweight and easy to use

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- Pickle

---

## 📂 Dataset

This project is trained on the **SMS Spam Collection Dataset**, which contains thousands of labeled SMS messages.

### Dataset Information

- Total Messages: 5,572
- Classes:
  - Ham (Not Spam)
  - Spam

---

## ⚙️ Machine Learning Workflow

1. Load the dataset
2. Clean and preprocess text
3. Remove punctuation
4. Convert text to lowercase
5. Tokenize words
6. Remove stopwords
7. Apply stemming
8. Convert text using TF-IDF Vectorizer
9. Train the Multinomial Naive Bayes classifier
10. Save the trained model and vectorizer
11. Deploy using Streamlit

---

## 📁 Project Structure

```
SMS-Spam-Classifier/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
└── sms_spam_classifier.ipynb
```

---

## 🤖 Machine Learning Model

**Algorithm Used**

- Multinomial Naive Bayes

**Text Processing**

- Tokenization
- Stopword Removal
- Porter Stemming
- TF-IDF Vectorization

The trained model and vectorizer are stored using **Pickle**, enabling fast predictions without retraining.

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/Prakritibhandari07/sms-spam-classifier.git
```

Navigate to the project directory

```bash
cd sms-spam-classifier
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 💻 Usage

1. Open the web application.
2. Enter an SMS or email message.
3. Click **Predict**.
4. The model classifies the message as:

- ✅ Not Spam (Ham)
- 🚨 Spam

---

## 📊 Model Performance

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score

The TF-IDF + Multinomial Naive Bayes combination provides strong performance for spam classification.

---

## 📸 Screenshots

### Home Page

*(Add your homepage screenshot here.)*

### Prediction Result

*(Add a screenshot showing a Spam and a Not Spam prediction.)*

---

## 🔮 Future Improvements

- Display prediction confidence score
- Support multiple languages
- Allow bulk prediction from CSV files
- Add message history
- Improve UI and responsiveness
- Deploy using Docker

---

## 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Prakriti Bhandari**

- **GitHub:** https://github.com/Prakritibhandari07
- **LinkedIn:** https://linkedin.com/in/prakriti-bhandari-18pp

---

⭐ If you found this project useful, don't forget to star the repository!
