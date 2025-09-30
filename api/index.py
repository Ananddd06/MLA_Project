from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd
import numpy as np
import os

app = Flask(__name__, template_folder='../templates')

# Load lightweight model and encoders
model_path = os.path.join(os.path.dirname(__file__), '..', 'lightweight_model.pkl')
encoders_path = os.path.join(os.path.dirname(__file__), '..', 'encoders.pkl')

model = joblib.load(model_path)
encoders = joblib.load(encoders_path)

def preprocess_input(data):
    # Create DataFrame
    df = pd.DataFrame([data])
    
    # Add company_age and no_of_employees with defaults
    df['company_age'] = 15
    df['no_of_employees'] = 1000
    
    # Encode categorical variables
    for col in ['continent', 'education_of_employee', 'has_job_experience', 
                'requires_job_training', 'region_of_employment', 'unit_of_wage', 
                'full_time_position']:
        if col in df.columns:
            try:
                df[col] = encoders[col].transform(df[col])
            except:
                df[col] = 0  # Default for unknown values
    
    # Ensure correct column order
    expected_cols = ['continent', 'education_of_employee', 'has_job_experience',
                    'requires_job_training', 'no_of_employees', 'region_of_employment',
                    'prevailing_wage', 'unit_of_wage', 'full_time_position', 'company_age']
    
    return df[expected_cols].values

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = {
            'continent': request.form['continent'],
            'education_of_employee': request.form['education_of_employee'],
            'has_job_experience': request.form['has_job_experience'],
            'requires_job_training': request.form['requires_job_training'],
            'region_of_employment': request.form['region_of_employment'],
            'prevailing_wage': float(request.form['prevailing_wage']),
            'unit_of_wage': request.form['unit_of_wage'],
            'full_time_position': request.form['full_time_position']
        }
        
        X = preprocess_input(data)
        prediction = model.predict(X)[0]
        proba = model.predict_proba(X)[0]
        
        result = "Denied" if prediction == 1 else "Certified"
        confidence = max(proba) * 100
        
        return render_template('result.html', 
                             prediction=result, 
                             confidence=round(confidence, 2))
    
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        data = request.get_json()
        X = preprocess_input(data)
        prediction = model.predict(X)[0]
        proba = model.predict_proba(X)[0]
        
        result = "Denied" if prediction == 1 else "Certified"
        confidence = max(proba)
        
        return jsonify({
            'prediction': result,
            'confidence': round(confidence, 4),
            'probabilities': {
                'certified': round(proba[0], 4),
                'denied': round(proba[1], 4)
            }
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
