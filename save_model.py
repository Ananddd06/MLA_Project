import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler, OrdinalEncoder, PowerTransformer
from sklearn.compose import ColumnTransformer 
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from imblearn.combine import SMOTEENN
from sklearn.model_selection import train_test_split

# Load and prepare data
df = pd.read_csv("/Users/anand/Desktop/MLA_Project/EasyVisa.csv")

# Drop case_id
df.drop('case_id', inplace=True, axis=1)

# Create company_age feature
from datetime import date
todays_date = date.today()
current_year = todays_date.year
df['company_age'] = current_year - df['yr_of_estab']
df.drop('yr_of_estab', inplace=True, axis=1)

# Prepare features and target
X = df.drop('case_status', axis=1)
y = np.where(df['case_status'] == 'Denied', 1, 0)

# Define column groups
or_columns = ['has_job_experience','requires_job_training','full_time_position','education_of_employee']
oh_columns = ['continent','unit_of_wage','region_of_employment']
transform_columns = ['no_of_employees','company_age']
num_features = ['no_of_employees', 'prevailing_wage', 'company_age']

# Create preprocessor
numeric_transformer = StandardScaler()
oh_transformer = OneHotEncoder()
ordinal_encoder = OrdinalEncoder()

transform_pipe = Pipeline(steps=[
    ('transformer', PowerTransformer(method='yeo-johnson'))
])

preprocessor = ColumnTransformer([
    ("OneHotEncoder", oh_transformer, oh_columns),
    ("Ordinal_Encoder", ordinal_encoder, or_columns),
    ("Transformer", transform_pipe, transform_columns),
    ("StandardScaler", numeric_transformer, num_features)
])

# Fit preprocessor and transform data
X_processed = preprocessor.fit_transform(X)

# Apply SMOTEENN
smt = SMOTEENN(random_state=42, sampling_strategy='minority')
X_res, y_res = smt.fit_resample(X_processed, y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)

# Train best model (KNN with best parameters)
best_model = KNeighborsClassifier(weights='distance', n_neighbors=4, algorithm='auto')
best_model.fit(X_train, y_train)

# Save the model and preprocessor
with open('/Users/anand/Desktop/MLA_Project/visa_model.pkl', 'wb') as f:
    pickle.dump(best_model, f)

with open('/Users/anand/Desktop/MLA_Project/preprocessor.pkl', 'wb') as f:
    pickle.dump(preprocessor, f)

print("Model and preprocessor saved successfully!")
