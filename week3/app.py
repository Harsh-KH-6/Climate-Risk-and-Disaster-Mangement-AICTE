import streamlit as st
import numpy as np
import pickle

# Set page config
st.set_page_config(page_title="Forest Fire Prediction", page_icon="🔥")

# Title
st.title('🔥 Forest Fire Area Prediction')

# Sidebar header
st.sidebar.header('Input Features')

# Input sliders
temp = st.sidebar.slider('Temperature (°C)', 8.0, 33.0, 22.0)
rh = st.sidebar.slider('Relative Humidity (%)', 15, 100, 45)
wind = st.sidebar.slider('Wind Speed (km/h)', 0.0, 9.5, 4.0)
rain = st.sidebar.slider('Rain (mm)', 0.0, 6.5, 0.0)
ffmc = st.sidebar.slider('FFMC', 18.0, 96.0, 90.0)
dmc = st.sidebar.slider('DMC', 1.0, 300.0, 110.0)
dc = st.sidebar.slider('DC', 7.0, 900.0, 550.0)
isi = st.sidebar.slider('ISI', 0.0, 56.0, 8.0)

# Predict button
if st.sidebar.button('Predict'):
    try:
        # Load the model
        with open('forest_fire_model.pkl', 'rb') as file:
            model = pickle.load(file)
        
        # Prepare input data
        input_data = np.array([[temp, rh, wind, rain, ffmc, dmc, dc, isi]])
        
        # Make prediction
        log_area_prediction = model.predict(input_data)[0]
        
        # Convert back to actual area (inverse log transformation)
        actual_area = np.exp(log_area_prediction) - 1
        
        # Display result
        st.write(f"The predicted burned area is: {actual_area:.2f} hectares")
        
        # Visual indicator based on area
        if actual_area > 50:
            st.error(f"⚠️ High Risk: {actual_area:.2f} hectares")
        elif actual_area > 10:
            st.warning(f"⚠️ Medium Risk: {actual_area:.2f} hectares")
        else:
            st.success(f"✅ Low Risk: {actual_area:.2f} hectares")
            
    except FileNotFoundError:
        st.error("Model file not found. Please make sure 'forest_fire_model.pkl' exists.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Add some information about the model
st.markdown("---")
st.markdown("### About this Model")
st.markdown("""
This application uses a Random Forest Regressor trained on forest fire data to predict the burned area.
The model considers the following features:
- **Temperature**: Air temperature in Celsius
- **Relative Humidity**: Percentage of moisture in the air
- **Wind Speed**: Wind speed in km/h
- **Rain**: Rainfall in mm
- **FFMC**: Fine Fuel Moisture Code
- **DMC**: Duff Moisture Code
- **DC**: Drought Code
- **ISI**: Initial Spread Index

**Risk Levels:**
- 🟢 Low Risk: ≤ 10 hectares
- 🟡 Medium Risk: 10-50 hectares
- 🔴 High Risk: > 50 hectares
""")
