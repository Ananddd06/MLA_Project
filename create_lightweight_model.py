import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pickle
import joblib

# Load and prepare data
df = pd.read_csv("EasyVisa.csv")
df.drop('case_id', inplace=True, axis=1)

# Simple preprocessing - just label encoding
le_dict = {}
categorical_cols = ['continent', 'education_of_employee', 'has_job_experience', 
                   'requires_job_training', 'region_of_employment', 'unit_of_wage', 
                   'full_time_position', 'case_status']

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    le_dict[col] = le

# Create company_age
from datetime import date
df['company_age'] = date.today().year - df['yr_of_estab']
df.drop('yr_of_estab', inplace=True, axis=1)

# Prepare features and target
X = df.drop('case_status', axis=1)
y = df['case_status']

# Train simple model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

print(f"Model accuracy: {model.score(X_test, y_test):.3f}")

# Save lightweight model and encoders
joblib.dump(model, 'lightweight_model.pkl', compress=3)
joblib.dump(le_dict, 'encoders.pkl', compress=3)

print("Lightweight model created successfully!")
