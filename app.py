
import streamlit as st
import pandas as pd
import joblib

# Load model and threshold
saved = joblib.load("fire_risk_model.pkl")
rf = saved["model"]
threshold = saved["threshold"]

st.set_page_config(page_title="Fire Risk Prediction", page_icon="🏭")

st.title("🏭 Industrial Fire Risk Prediction")
st.write("Enter the factory conditions to predict fire risk.")

st.subheader("Factory Conditions")

temp = st.number_input("Temperature", value=30.0)
service_days = st.number_input("Service Days", min_value=0, value=100)
pressure = st.number_input("Pressure", min_value=0.0, value=10.0)

season = st.selectbox(
    "Season", ["Spring", "Summer", "Autumn", "Winter"]
)

age = st.number_input("Age", min_value=0, value=30)
gas = st.number_input("Gas", min_value=0.0, value=5.04)
speed = st.number_input("Speed", min_value=0.0, value=50.0)

if st.button("Predict Fire Risk"):

    input_data = pd.DataFrame([{
        "Factory": "Factory_D",
        "Region": "Urban",
        "Shift": "Night",
        "Workers": 27.0,
        "Exp": "Senior",
        "Training": "No",
        "Temp": temp,
        "Pressure": pressure,
        "Humidity": 50.0,
        "Vibration": 1.0,
        "Speed": speed,
        "Age": age,
        "Service_Days": service_days,
        "Gas": gas,
        "Sparks": 2,
        "Alarm": "On",
        "Season": season,
        "Gas_Level": "Medium",
        "Machine_Age_Group": "Old",
        "Temp_Gas_Interaction": temp * gas
    }])

    probability = rf.predict_proba(input_data)[0][1]
    prediction = int(probability >= threshold)

    st.subheader("Prediction Result")
    st.metric("Predicted Fire Probability", f"{probability:.2%}")
    st.caption(f"Decision threshold: {threshold:.2%}")

    if prediction == 1:
        st.error("⚠️ High fire risk detected!")
    else:
        st.success("✅ Lower predicted fire risk")
