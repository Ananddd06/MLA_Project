from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd
import numpy as np
from datetime import date

app = Flask(__name__)

# Load the trained model and preprocessor
with open('visa_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('preprocessor.pkl', 'rb') as f:
    preprocessor = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        continent = request.form['continent']
        education = request.form['education_of_employee']
        job_experience = request.form['has_job_experience']
        job_training = request.form['requires_job_training']
        region = request.form['region_of_employment']
        prevailing_wage = float(request.form['prevailing_wage'])
        unit_of_wage = request.form['unit_of_wage']
        full_time_position = request.form['full_time_position']
        
        # Set default values for removed fields
        no_of_employees = 1000  # Default company size
        company_age = 15  # Default company age
        
        # Create DataFrame with input data
        input_data = pd.DataFrame({
            'continent': [continent],
            'education_of_employee': [education],
            'has_job_experience': [job_experience],
            'requires_job_training': [job_training],
            'no_of_employees': [no_of_employees],
            'region_of_employment': [region],
            'prevailing_wage': [prevailing_wage],
            'unit_of_wage': [unit_of_wage],
            'full_time_position': [full_time_position],
            'company_age': [company_age]
        })
        
        # Preprocess the input data
        input_processed = preprocessor.transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_processed)[0]
        prediction_proba = model.predict_proba(input_processed)[0]
        
        # Convert prediction to readable format
        if prediction == 1:
            result = "Denied"
            confidence = prediction_proba[1] * 100
        else:
            result = "Certified"
            confidence = prediction_proba[0] * 100
        
        return render_template('result.html', 
                             prediction=result, 
                             confidence=round(confidence, 2))
    
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        data = request.get_json()
        
        # Set default values for removed fields
        no_of_employees = 1000  # Default company size
        company_age = 15  # Default company age
        
        # Create DataFrame with input data
        input_data = pd.DataFrame({
            'continent': [data['continent']],
            'education_of_employee': [data['education_of_employee']],
            'has_job_experience': [data['has_job_experience']],
            'requires_job_training': [data['requires_job_training']],
            'no_of_employees': [no_of_employees],
            'region_of_employment': [data['region_of_employment']],
            'prevailing_wage': [data['prevailing_wage']],
            'unit_of_wage': [data['unit_of_wage']],
            'full_time_position': [data['full_time_position']],
            'company_age': [company_age]
        })
        
        # Preprocess the input data
        input_processed = preprocessor.transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_processed)[0]
        prediction_proba = model.predict_proba(input_processed)[0]
        
        # Convert prediction to readable format
        if prediction == 1:
            result = "Denied"
            confidence = prediction_proba[1]
        else:
            result = "Certified"
            confidence = prediction_proba[0]
        
        return jsonify({
            'prediction': result,
            'confidence': round(confidence, 4),
            'probabilities': {
                'certified': round(prediction_proba[0], 4),
                'denied': round(prediction_proba[1], 4)
            }
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
