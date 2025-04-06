# Malicious_Webpage_Detection_ML_Model
This project is a simple and smart web app that helps you check is a URL might be malicious or safe. It uses a machine learning model trained on both the structure of the URL and the content of the webpage, like scripts, forms, and hidden tags. Just enter any link , and it will analyze it in seconds using a clean Streamlit interface.


# 🔒 Malicious Webpage Detector

A simple yet powerful Streamlit web app that helps detect whether a given webpage URL is safe or malicious using machine learning. This tool is built to assist users in identifying suspicious URLs by analyzing both URL-based and content-based features. Whether you're a student, developer, or security enthusiast, this project offers a hands-on look at applying ML in cybersecurity.

---

## 🚀 Features

- ✅ Real-time URL safety prediction  
- 🧠 Trained using a Random Forest Classifier  
- 🔍 Combines both URL structure and HTML/JavaScript content features  
- 📊 Interactive UI with Streamlit  
- ⚡ Fast, offline, and easy to use

---

## 📂 Project Structure

malicious_webpage_detector/     # Root folder of project
│
├── app.py                      # Main Streamlit app file
├── model/                      # Folder that stores trained model files
│   ├── malicious_webpage_detector.pkl   # The trained ML model
│   └── feature_names.pkl      # The list of feature names used while training
├── utils/                      # Folder for utility/helper scripts
│   └── feature_extraction.py  # The script that contains the logic to extract features from a URL
├── requirements.txt            # A list of Python dependencies needed to run the project
├── sample_urls.csv             # A CSV file with example safe/malicious URLs for testing
└── README.md                   # Project documentation (this file)


## 🧠 How It Works

1. The user inputs a URL in the Streamlit interface.
2. The app extracts both URL-based features (like `url length`, presence of keywords) and content-based features (like `HTML tags`, `JavaScript obfuscation`, etc.).
3. The trained Random Forest model analyzes the feature set.
4. The app returns a prediction: 🟢 Safe or 🔴 Malicious.

---

## ⚙️ Getting Started

Follow these steps to set up and run the Malicious Webpage Detector locally:

1. Clone the Repository:
    git clone https://github.com/yourusername/malicious_webpage_detector.git
    cd malicious_webpage_detector

2. Set Up a Virtual Environment:
    python -m venv venv
    source venv/bin/activate (For Linux)
    venv\Scripts\activate  (For Windows)

3. Install Dependencies
    pip install -r requirements.txt

4. Run the App
    streamlit run app.py


##Note:- This app will open in your default browser.(If not copy the provided local host ip address and paste it in you browser.)


 Try These URLs
Safe URLs:

  https://www.wikipedia.org
  
  https://www.google.com
  
  https://www.github.com
  
  https://www.microsoft.com
  
  https://www.python.org

Malicious URLs:

  http://malicious-login-now.com
  
  http://192.168.0.1/login
  
  http://free-prizes.biz/claim
  
  http://secure-banking-alert.net
  
  http://clickme-fast-download.ru

Contributing

Feel free to fork the repo, raise issues, or submit PRs to:
  
->  Add new feature sets
->  Improve model accuracy
->  Expand dataset
->  Deploy with Docker or cloud










