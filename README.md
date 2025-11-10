💰 Fraud Detection App

An interactive machine learning web application that detects fraudulent transactions in real time using a trained pipeline model — built with Streamlit, Pandas, and Scikit-learn.

🚀 Features

🔍 Predict whether a financial transaction is fraudulent or legitimate

📊 Real-time transaction validation and fraud detection

🧠 Integrated ML model (fraud_detection_pipeline.pkl) trained on real-world transaction patterns

🧾 Smart logic checks for transaction consistency (e.g., invalid sender/receiver balances)

💻 Easy-to-use interface powered by Streamlit

⚙️ Tech Stack

Python 

Streamlit – for front-end UI

Pandas – for data handling

Scikit-learn / Joblib – for model loading and prediction

Machine Learning Pipeline – trained fraud detection classifier

🧠 How It Works

User selects a transaction type (PAYMENT, CASH_OUT, or DEPOSIT)

Inputs transaction details (amount, sender and receiver balances)

The app runs:

Validation logic to check if the transaction makes sense

Model inference to detect fraud based on input features

Displays results as ✅ Legitimate or 🚨 Fraudulent

🧩 Model Overview

The machine learning model was trained on a financial transactions dataset containing millions of records.
It identifies patterns in fraudulent behavior by analyzing:

Transaction type

Amount

Sender and receiver balance changes

Logical inconsistencies

The model was serialized using Joblib and integrated into this Streamlit app for real-time predictions.
