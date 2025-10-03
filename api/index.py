from flask import Flask, request, render_template, jsonify
import json
import os

app = Flask(__name__, template_folder='../templates')

# Simple rule-based prediction (no ML dependencies)
def predict_visa(data):
    score = 0
    
    # Education scoring
    education_scores = {
        "Doctorate": 4, "Master's": 3, "Bachelor's": 2, "High School": 1
    }
    score += education_scores.get(data.get('education_of_employee', ''), 1)
    
    # Experience scoring
    if data.get('has_job_experience') == 'Y':
        score += 2
    
    # Training requirement (inverse scoring)
    if data.get('requires_job_training') == 'N':
        score += 1
    
    # Full-time position
    if data.get('full_time_position') == 'Y':
        score += 1
    
    # Wage scoring with unit conversion
    wage = float(data.get('prevailing_wage', 0))
    unit = data.get('unit_of_wage', 'Year')
    
    # Convert to annual salary
    if unit == 'Month':
        annual_wage = wage * 12
    elif unit == 'Week':
        annual_wage = wage * 52
    elif unit == 'Hour':
        annual_wage = wage * 2080  # 40 hours/week * 52 weeks
    else:  # Year
        annual_wage = wage
    
    if annual_wage > 80000:
        score += 2
    elif annual_wage > 50000:
        score += 1
    
    # Region scoring (some regions have higher approval rates)
    region_scores = {
        "West": 2, "Northeast": 2, "South": 1, "Midwest": 1, "Island": 0
    }
    score += region_scores.get(data.get('region_of_employment', ''), 0)
    
    # Continent scoring
    continent_scores = {
        "Asia": 1, "Europe": 2, "North America": 2, 
        "South America": 1, "Africa": 1, "Oceania": 1
    }
    score += continent_scores.get(data.get('continent', ''), 0)
    
    # Determine prediction based on score
    max_score = 13
    confidence = min(score / max_score, 1.0)
    
    if score >= 8:
        return "Certified", confidence * 100
    else:
        return "Denied", (1 - confidence) * 100

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
        
        result, confidence = predict_visa(data)
        
        return render_template('result.html', 
                             prediction=result, 
                             confidence=round(confidence, 2))
    
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        data = request.get_json()
        result, confidence = predict_visa(data)
        
        conf_decimal = confidence / 100
        
        return jsonify({
            'prediction': result,
            'confidence': round(conf_decimal, 4),
            'probabilities': {
                'certified': round(conf_decimal if result == "Certified" else 1-conf_decimal, 4),
                'denied': round(1-conf_decimal if result == "Certified" else conf_decimal, 4)
            }
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
