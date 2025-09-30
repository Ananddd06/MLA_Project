# 🛂 U.S. Visa Assessment Portal

An AI-powered web application that predicts visa application outcomes using machine learning. Features a modern, glassmorphism UI with 96.8% prediction accuracy.

## ✨ Features

- **🤖 AI-Powered Predictions**: KNN model with 96.8% accuracy
- **🎨 Modern UI**: Glassmorphism design with custom animations
- **📱 Responsive**: Works perfectly on all devices
- **⚡ Fast**: Instant predictions with confidence scores
- **🔒 Secure**: No sensitive data storage

## 🚀 Live Demo

**Deployed on Vercel**: [Your Vercel URL will be here]

## 📋 API Usage

### Endpoint: `/api/predict`
```json
POST /api/predict
{
    "continent": "Asia",
    "education_of_employee": "Master's",
    "has_job_experience": "Y",
    "requires_job_training": "N",
    "region_of_employment": "West",
    "prevailing_wage": 85000,
    "unit_of_wage": "Year",
    "full_time_position": "Y"
}
```

### Response:
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

## 🛠️ Local Development

```bash
# Clone repository
git clone <your-repo-url>
cd MLA_Project

# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py
```

## 📊 Model Performance

- **Accuracy**: 96.8%
- **F1-Score**: 97.1%
- **Algorithm**: K-Nearest Neighbors (KNN)
- **Features**: 10 key visa application parameters

## 🎯 Input Parameters

| Field | Type | Options |
|-------|------|---------|
| Continent | Select | Asia, Europe, North America, South America, Africa, Oceania |
| Education | Select | High School, Bachelor's, Master's, Doctorate |
| Job Experience | Select | Yes/No |
| Training Required | Select | Yes/No |
| Employment Type | Select | Full-Time/Part-Time |
| Work Region | Select | Northeast, South, West, Midwest, Island |
| Salary Amount | Number | Any positive number |
| Pay Frequency | Select | Annual, Monthly, Weekly, Hourly |

## 🔧 Tech Stack

- **Backend**: Flask, Python
- **ML**: Scikit-learn, Pandas, NumPy
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: Vercel
- **Model**: K-Nearest Neighbors

## ⚠️ Disclaimer

This AI assessment tool is for informational purposes only. Official visa decisions are made exclusively by authorized immigration authorities.

## 📄 License

MIT License - feel free to use for educational purposes.
# MLA_Project
