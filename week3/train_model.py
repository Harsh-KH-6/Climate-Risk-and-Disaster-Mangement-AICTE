import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load the dataset
df = pd.read_csv("week1/forestfires.csv")

# Data Transformation
df['month'] = df['month'].astype('category').cat.codes
df['day'] = df['day'].astype('category').cat.codes
df['log_area'] = df['area'].apply(lambda x: np.log(x + 1))

# Feature Selection
features = ['temp', 'RH', 'wind', 'rain', 'FFMC', 'DMC', 'DC', 'ISI']
target = 'log_area'
X = df[features]
y = df[target]

# Split data and train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
with open('forest_fire_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved successfully.")

# Display some basic information about the model
print(f"\nModel Information:")
print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")
print(f"Features used: {features}")
print(f"Target variable: {target}")

# Calculate and display model performance
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print(f"\nModel Performance:")
print(f"Training R² Score: {train_score:.4f}")
print(f"Test R² Score: {test_score:.4f}")

# Feature importance
feature_importance = model.feature_importances_
print(f"\nFeature Importance:")
for feature, importance in zip(features, feature_importance):
    print(f"{feature}: {importance:.4f}")
