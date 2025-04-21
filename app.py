import streamlit as st
import joblib
import pandas as pd
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# Load the trained model and feature names
model = joblib.load("malicious_webpage_detector.pkl")
feature_names = model.feature_names_in_  # Automatically gets correct feature order

# Function to extract features from a given URL
def extract_features_from_url(url):
    features = {}

    # URL-based features
    features['url_len'] = len(url)
    features['https'] = int(url.startswith('https'))
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    path = parsed_url.path

    features['domain_len'] = len(domain)
    features['path_len'] = len(path)
    features['contains_ip'] = int(any(char.isdigit() for char in domain))
    features['contains_login'] = int('login' in url.lower())
    features['contains_bank'] = int('bank' in url.lower())
    features['contains_secure'] = int('secure' in url.lower())

    # Try fetching HTML content for content-based features
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        features['script_tags'] = len(soup.find_all('script'))
        features['form_tags'] = len(soup.find_all('form'))
        features['iframe_tags'] = len(soup.find_all('iframe'))
        
        js_code = ''.join([script.text for script in soup.find_all('script')])
        features['js_len'] = len(js_code)
        features['js_obf_len'] = sum(1 for c in js_code if c in '{}[]();')

    except Exception as e:
        st.warning(f"⚠️ Error while fetching HTML: {e}")
        features['script_tags'] = 0
        features['form_tags'] = 0
        features['iframe_tags'] = 0
        features['js_len'] = 0
        features['js_obf_len'] = 0

    # Ensure the feature order matches training time
    for col in feature_names:
        if col not in features:
            features[col] = 0  # Add missing features with default 0

    return pd.DataFrame([features])[list(feature_names)]

# Streamlit UI
st.title("🔒 Malicious Webpage Detector")
url_input = st.text_input("Enter a URL to check if it's safe:")

if st.button("Analyze"):
    try:
        features = extract_features_from_url(url_input)
        prediction = model.predict(features)[0]
        label = "🟢 Safe" if prediction == 0 else "🔴 Malicious"
        st.markdown(f"## Result: {label}")
    except Exception as e:
        st.error(f"An error occurred while analyzing the URL: {e}")
