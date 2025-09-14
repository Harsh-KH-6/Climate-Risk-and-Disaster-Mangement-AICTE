AICTE Internship Project - Climate Risk and Disaster Management
This repository contains my AICTE Internship project on Climate Risk and Disaster Management using the Forest Fire Dataset (derived from NASA’s EONET API via Kaggle). The project focuses on analyzing natural disasters such as wildfires, forestfire and there impact.

---

## Week 1 Project
In Week 1, the goal was to reach the Data Understanding stage:

Imported necessary Python libraries (pandas, numpy)
Loaded the dataset (Data.csv)
Explored dataset using:

.info() → structure of data

.describe() → summary statistics

.isnull().sum() → missing values check

Previewed disaster categories and their counts

This forms the foundation for deeper analysis and visualization in upcoming weeks.

📂 Files in Repository

Foresfire.ipynb → Notebook for Week 1

Forestfires.csv → Forest Fire Dataset

README.md → Project description


⚙️ How to Run
Clone the repository
git clone https://github.com/your-username/AICTE-ClimateRisk-Project.git


---

## Week 2 Project 

This week focused on preparing the forest fire dataset for analysis and modeling.

* **Data Transformation:** Cleaned the dataset by converting categorical columns (`month`, `day`) to numerical values. Normalized the highly skewed `area` column using a log transformation to create `log_area` for better analysis.
* **Exploratory Data Analysis (EDA):** Created several visualizations to understand the data:
    * A **correlation heatmap** revealed that temperature (`temp`), relative humidity (`RH`), and drought codes (`DMC`, `DC`) have the strongest relationships with fire occurrences.
    * **Bar charts** showed that **August and September** are the peak months for fires, and weekends (**Friday, Saturday, Sunday**) see the most incidents.
    * An interactive **geographical map** (`forest_fire_map.html`) was generated to visualize the location and size of the fires.


---

# Week 3: Forest Fire Prediction Model & Web Application

## Project Overview
This week focused on completing the final phase of our Climate Risk and Disaster Management project by developing a machine learning model to predict forest fire burned areas and creating a user-friendly web application.

## Objectives Achieved
1. **Model Development**: Trained a Random Forest Regressor to predict forest fire burned areas
2. **Web Application**: Created an interactive Streamlit application for real-time predictions
3. **Model Deployment**: Prepared the model for production use with proper serialization

## Technical Implementation

### 1. Data Preprocessing & Model Training (`train_model.py`)
- **Dataset**: Utilized the forestfires.csv dataset from Week 2
- **Data Transformation**:
  - Converted categorical variables (month, day) to numeric codes
  - Applied log transformation to the area column: `log_area = log(area + 1)`
- **Feature Selection**: Used 8 key meteorological and fire danger indices:
  - Temperature (°C)
  - Relative Humidity (%)
  - Wind Speed (km/h)
  - Rainfall (mm)
  - FFMC (Fine Fuel Moisture Code)
  - DMC (Duff Moisture Code)
  - DC (Drought Code)
  - ISI (Initial Spread Index)
- **Model**: Random Forest Regressor with 100 estimators
- **Performance**: Achieved good predictive accuracy on test data
- **Model Persistence**: Saved trained model as `forest_fire_model.pkl`

### 2. Web Application Development (`app.py`)
- **Framework**: Streamlit for interactive web interface
- **Features**:
  - User-friendly sidebar with input sliders for all 8 features
  - Real-time prediction capability
  - Risk level visualization:
    - 🟢 Low Risk: ≤ 10 hectares
    - 🟡 Medium Risk: 10-50 hectares
    - 🔴 High Risk: > 50 hectares
  - Inverse transformation to display actual burned area in hectares
  - Educational content about fire danger indices

### 3. Key Technical Features
- **Log Transformation**: Used to handle skewed area distribution
- **Model Serialization**: Pickle for model persistence
- **Error Handling**: Comprehensive exception handling in the web app
- **User Experience**: Intuitive interface with clear risk indicators

## Model Performance Insights
- **Feature Importance Analysis**:
  - Temperature: Most important predictor
  - Relative Humidity: Second most important
  - Wind Speed: Significant contributor
  - Other indices: Supporting factors
- **Training Data**: 413 samples
- **Test Data**: 104 samples
- **Cross-validation**: 80-20 train-test split

## Practical Applications
1. **Fire Risk Assessment**: Real-time evaluation of fire danger conditions
2. **Resource Planning**: Helps emergency services prepare for potential fires
3. **Public Awareness**: Educational tool for understanding fire danger factors
4. **Research**: Foundation for further climate risk analysis

## Technical Stack
- **Python**: Core programming language
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning algorithms
- **NumPy**: Numerical computations
- **Streamlit**: Web application framework
- **Pickle**: Model serialization

## Project Deliverables
1. `train_model.py` - Complete model training pipeline
2. `app.py` - Interactive web application
3. `forest_fire_model.pkl` - Trained model file
4. `requirements.txt` - Project dependencies
5. `week1/forestfires.csv` - Original dataset

## Learning Outcomes
- Applied machine learning to real-world climate data
- Developed end-to-end ML pipeline from data preprocessing to deployment
- Created user-friendly interfaces for complex predictive models
- Gained experience in model serialization and web application development
- Understood the importance of feature engineering in environmental modeling

## Future Enhancements
- Integration with real-time weather APIs
- Multi-model ensemble approaches
- Geographic visualization of fire risk
- Mobile application development
- Integration with emergency response systems

This week successfully completed the AICTE internship project, demonstrating practical application of machine learning in climate risk and disaster management.

 ⚙️ How to Run

1.  Ensure you have `pandas`, `numpy`, `seaborn`, `matplotlib`, and `folium` installed.
2.  Open the Jupyter Notebook (`Forestfire Week2.ipynb`) and run the cells.

