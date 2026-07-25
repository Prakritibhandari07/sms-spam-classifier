import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("📩 Email/SMS Spam Classifier")
st.write("Enter a message below to check whether it's spam or legitimate.")

# Sample buttons for easy demoing
col1, col2 = st.columns(2)
with col1:
    if st.button("✅ Try a legitimate message"):
        st.session_state.sms_input = "Hey, are we still on for lunch tomorrow at 1? Let me know if that works."
with col2:
    if st.button("🚫 Try a spam message"):
        st.session_state.sms_input = "CONGRATULATIONS! You've WON a $1000 gift card! Click here NOW: bit.ly/claim-prize. Reply STOP to opt out."

input_sms = st.text_area(
    "Enter the message",
    value=st.session_state.get("sms_input", ""),
    placeholder="Type or paste a message here...",
    height=100
)

if st.button('Predict', type="primary"):
    if not input_sms.strip():
        st.warning("Please enter a message first.")
    else:
        # 1. preprocess
        transform_sms = transform_text(input_sms)
        # 2. vectorize
        vector_input = tfidf.transform([transform_sms])
        # 3. predict
        result = model.predict(vector_input)[0]
        proba = model.predict_proba(vector_input)[0]

        # 4. display
        if result == 1:
            st.error(f"🚫 **Spam** — {proba[1]:.1%} confidence")
        else:
            st.success(f"✅ **Not Spam** — {proba[0]:.1%} confidence")
