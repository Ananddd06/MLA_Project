import requests
import json

# Test data
test_data = {
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

try:
    # Test the API endpoint
    response = requests.post('http://127.0.0.1:5000/api/predict', 
                           json=test_data, 
                           timeout=10)
    
    if response.status_code == 200:
        result = response.json()
        print("✅ API Test Successful!")
        print(f"Prediction: {result['prediction']}")
        print(f"Confidence: {result['confidence']}")
        print(f"Probabilities: {result['probabilities']}")
    else:
        print(f"❌ API Test Failed with status code: {response.status_code}")
        print(f"Response: {response.text}")
        
except requests.exceptions.ConnectionError:
    print("❌ Connection Error: Flask app is not running")
except Exception as e:
    print(f"❌ Error: {e}")
