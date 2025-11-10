import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("fraud_detection_pipeline.pkl")

st.title("💰 Fraud Detection App")

# --- User Inputs ---
t_type = st.selectbox("Transaction Type", ["PAYMENT", "CASH_OUT", "DEPOSIT"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
old_s = st.number_input("Old Balance (Sender)", min_value=0.0, value=5000.0)
new_s = st.number_input("New Balance (Sender)", min_value=0.0, value=4000.0)
old_r = st.number_input("Old Balance (Receiver)", min_value=0.0, value=5000.0)
new_r = st.number_input("New Balance (Receiver)", min_value=0.0, value=6000.0)

if st.button("Predict!"):
    sender_diff = old_s - new_s
    receiver_diff = new_r - old_r
    #st.write(f"Computed: sender_diff = {sender_diff:.2f}, receiver_diff = {receiver_diff:.2f}")

    valid = True

    # --- Logic per Transaction Type ---
    if t_type == "PAYMENT":
        if abs(sender_diff - amount) > 1 or new_s > old_s:
            st.error("🚨 Invalid PAYMENT: sender’s balance mismatch!")
            valid = False
        if abs(receiver_diff - amount) > 1 or new_r <= old_r:
            st.error("🚨 Invalid PAYMENT: receiver’s balance mismatch!")
            valid = False

    elif t_type == "CASH_OUT":
        if abs(sender_diff - amount) > 1 or new_s > old_s:
            st.error("🚨 Invalid CASH_OUT: sender’s balance mismatch!")
            valid = False
        if receiver_diff != 0:
            st.error("🚨 CASH_OUT: receiver’s balance should not change!")
            valid = False

    elif t_type == "DEPOSIT":
        if abs(sender_diff - amount) > 1 or new_s > old_s:
            st.error("🚨 Invalid DEPOSIT: sender’s balance mismatch!")
            valid = False
        if abs(receiver_diff - amount) > 1 or new_r <= old_r:
            st.error("🚨 Invalid DEPOSIT: receiver’s balance mismatch!")
            valid = False
        if valid:
            st.info("✅ Legitimate Transaction")

    # --- If logical checks pass and type is PAYMENT or CASH_OUT, use the model ---
    if valid and t_type in ["PAYMENT", "CASH_OUT"]:
        data = pd.DataFrame([{
            "type": t_type, "amount": amount,
            "oldbalanceOrg": old_s, "newbalanceOrig": new_s,
            "oldbalanceDest": old_r, "newbalanceDest": new_r
        }])
        pred = model.predict(data)[0]
        if pred == 1:
            st.error("🚨 Fraudulent Transaction Detected!")
        else:
            st.success("✅ Legitimate Transaction")
