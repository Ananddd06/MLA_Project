# Visa Prediction System

This Flask web application predicts whether a visa application will be **Certified** or **Denied** based on various applicant and employer characteristics.

## Features

- **Machine Learning Model**: Uses a K-Nearest Neighbors (KNN) classifier trained on visa application data
- **Web Interface**: User-friendly form to input application details
- **REST API**: JSON API endpoint for programmatic access
- **High Accuracy**: Achieves ~96.8% accuracy on test data

## Model Details

- **Algorithm**: K-Nearest Neighbors (KNN) with optimized hyperparameters
- **Features**: Continent, education level, job experience, company details, wage information, etc.
- **Preprocessing**: Includes feature scaling, encoding, and SMOTEENN for handling class imbalance
- **Performance**: 96.8% accuracy, 97.1% F1-score

## Installation & Setup

1. **Clone/Download** the project files
2. **Create virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install pandas numpy scikit-learn imbalanced-learn flask
   ```

## Running the Application

1. **Activate virtual environment**:
   ```bash
   source venv/bin/activate
   ```
2. **Start the Flask app**:
   ```bash
   python app.py
   ```
3. **Open browser** and go to: `http://127.0.0.1:5000`

## Usage

### Web Interface
1. Fill out the form with applicant details:
   - Personal info (continent, education)
   - Job details (experience, training requirements)
   - Company info (size, establishment year, region)
   - Wage information
2. Click "Predict Visa Status"
3. View the prediction result with confidence score

### API Usage
Send POST request to `/api/predict` with JSON data:

```json
{
    "continent": "Asia",
    "education_of_employee": "Master's",
    "has_job_experience": "Y",
    "requires_job_training": "N",
    "no_of_employees": 1000,
    "yr_of_estab": 2010,
    "region_of_employment": "West",
    "prevailing_wage": 85000,
    "unit_of_wage": "Year",
    "full_time_position": "Y"
}
```

Response:
```json
{
    "prediction": "Certified",
    "confidence": 0.8542,
    "probabilities": {
        "certified": 0.8542,
        "denied": 0.1458
    }
}
```

## Input Fields

- **Continent**: Asia, Europe, North America, South America, Africa, Oceania
- **Education**: High School, Bachelor's, Master's, Doctorate
- **Job Experience**: Y/N
- **Job Training Required**: Y/N
- **Full Time Position**: Y/N
- **Number of Employees**: Integer (company size)
- **Year of Establishment**: Year (1800-2024)
- **Region**: Northeast, South, West, Midwest, Island
- **Prevailing Wage**: Numeric (salary/wage amount)
- **Unit of Wage**: Year, Hour, Week, Month

## Files Structure

```
MLA_Project/
├── app.py                 # Flask application
├── visa_model.pkl         # Trained ML model
├── preprocessor.pkl       # Data preprocessor
├── EasyVisa.csv          # Original dataset
├── Feature_Engineering.ipynb  # Model training notebook
├── templates/
│   ├── index.html        # Main form page
│   ├── result.html       # Prediction result page
│   └── error.html        # Error page
└── README.md             # This file
```

## Model Training

The model was trained using the notebook `Feature_Engineering.ipynb` which includes:
- Data preprocessing and feature engineering
- Handling class imbalance with SMOTEENN
- Hyperparameter tuning with RandomizedSearchCV
- Model evaluation and selection

## Disclaimer

This is a machine learning model for educational/demonstration purposes. Actual visa decisions involve many more factors and should not rely solely on automated predictions.
# MLA_Project
