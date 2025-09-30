import pickle
import pandas as pd
import numpy as np
from datetime import date

print("Testing model and preprocessor...")

try:
    # Load the trained model and preprocessor
    with open('visa_model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("✅ Model loaded successfully")

    with open('preprocessor.pkl', 'rb') as f:
        preprocessor = pickle.load(f)
    print("✅ Preprocessor loaded successfully")

    # Test data
    test_data = {
        'continent': ['Asia'],
        'education_of_employee': ["Master's"],
        'has_job_experience': ['Y'],
        'requires_job_training': ['N'],
        'no_of_employees': [1000],
        'region_of_employment': ['West'],
        'prevailing_wage': [85000.0],
        'unit_of_wage': ['Year'],
        'full_time_position': ['Y'],
        'company_age': [2025 - 2010]  # Current year - establishment year
    }

    # Create DataFrame
    input_data = pd.DataFrame(test_data)
    print("✅ Test data created")

    # Preprocess the input data
    input_processed = preprocessor.transform(input_data)
    print("✅ Data preprocessed successfully")

    # Make prediction
    prediction = model.predict(input_processed)[0]
    prediction_proba = model.predict_proba(input_processed)[0]
    print("✅ Prediction made successfully")

    # Convert prediction to readable format
    if prediction == 1:
        result = "Denied"
        confidence = prediction_proba[1]
    else:
        result = "Certified"
        confidence = prediction_proba[0]

    print(f"\n🔮 Prediction Results:")
    print(f"   Status: {result}")
    print(f"   Confidence: {confidence:.4f} ({confidence*100:.2f}%)")
    print(f"   Probabilities: Certified={prediction_proba[0]:.4f}, Denied={prediction_proba[1]:.4f}")

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
