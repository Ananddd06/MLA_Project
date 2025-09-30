from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd
import numpy as np
import os

app = Flask(__name__, template_folder='../templates')

# Load model and preprocessor
model_path = os.path.join(os.path.dirname(__file__), '..', 'visa_model.pkl')
preprocessor_path = os.path.join(os.path.dirname(__file__), '..', 'preprocessor.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(preprocessor_path, 'rb') as f:
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
        no_of_employees = 1000
        company_age = 15
        
        # Create DataFrame
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
        
        # Preprocess and predict
        input_processed = preprocessor.transform(input_data)
        prediction = model.predict(input_processed)[0]
        prediction_proba = model.predict_proba(input_processed)[0]
        
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
        
        no_of_employees = 1000
        company_age = 15
        
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
        
        input_processed = preprocessor.transform(input_data)
        prediction = model.predict(input_processed)[0]
        prediction_proba = model.predict_proba(input_processed)[0]
        
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

# Vercel handler
def handler(request):
    return app(request.environ, lambda status, headers: None)
