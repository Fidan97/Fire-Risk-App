import streamlit as st
import pandas as pd
import joblib

rf = joblib.load("model.pkl")
threshold = joblib.load("threshold.pkl")

st.title("🏭 Industrial Accident Prediction")

st.write("Enter the industrial conditions below "
"to predict the probability of an accident.")
st.subheader("Factory Conditions")

temp = st.number_input("Temperature", value=30.0)
service_days = st.number_input(
    "Service Days", min_value=0, value=100
)
pressure = st.number_input("Pressure", min_value=0.0, value=10.0)

season = st.selectbox(
    "Season", ["Spring", "Summer", "Autumn", "Winter"]
)

age = st.number_input("Age", min_value=0, value=30)
humidity = st.number_input(
    "Humidity", min_value=0.0, max_value=100.0, value=50.0
)
speed = st.number_input("Speed", min_value=0.0, value=50.0)
vibration = st.number_input("Vibration", min_value=0.0, value=1.0)
if st.button("Predict Accident Risk"):
    input_data = pd.DataFrame([{
        "Factory": "Factory_D",
        "Region": "Urban",
        "Shift": "Night",
        "Workers": 27.0,
        "Exp": "Senior",
        "Training": "No",
        "Temp": temp,
        "Pressure": pressure,
        "Humidity": humidity,
        "Vibration": vibration,
        "Speed": speed,
        "Age": age,
        "Service_Days": service_days,
        "Gas": 5.04,
        "Sparks": 2,
        "Alarm": "On",
        "Season": season
    }])

    probability = rf.predict_proba(input_data)[0][1]

    prediction = int(probability >= threshold)

    st.subheader("Prediction Result")
    st.write(f"Accident probability: {probability:.2%}")

    if prediction == 1:
        st.error("⚠️ High accident risk detected")
    else:
        st.success("✅ Lower predicted accident risk")