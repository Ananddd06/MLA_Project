# 🛂 U.S. Visa Assessment Portal

An intelligent web application that predicts U.S. visa application outcomes using machine learning and rule-based algorithms. Features a modern glassmorphism UI with dual prediction systems for maximum reliability.

## ✨ Key Features

- **🤖 Dual AI System**: KNN ML model + intelligent rule-based fallback
- **🎨 Modern UI**: Glassmorphism design with custom animations
- **📱 Fully Responsive**: Optimized for all devices
- **⚡ Lightning Fast**: Instant predictions with confidence scores
- **🚀 Vercel Ready**: Serverless deployment optimized
- **🔒 Secure**: No sensitive data storage

## 🚀 Live Demo

**Deployed on Vercel**: [Live Application](https://your-vercel-url.vercel.app)

## 🎯 Prediction Systems

### Primary: KNN Machine Learning Model
- **Algorithm**: K-Nearest Neighbors with distance weighting
- **Features**: 10 key visa application parameters
- **Data Processing**: SMOTEENN balancing + feature engineering
- **Preprocessing**: OneHot + Ordinal encoding + StandardScaler

### Fallback: Rule-Based Intelligence
- **Education Scoring**: PhD(4) → Master's(3) → Bachelor's(2) → HS(1)
- **Experience Bonus**: +2 points for job experience
- **Training Factor**: +1 if no training required
- **Employment Type**: +1 for full-time positions
- **Salary Tiers**: +2 (>$80k), +1 (>$50k)
- **Regional Weights**: West/Northeast(+2), South/Midwest(+1)

## 📊 Model Performance

```
Algorithm: K-Nearest Neighbors
Parameters: n_neighbors=4, weights='distance'
Preprocessing: SMOTEENN + Multi-encoder pipeline
Features: 10 engineered features
Deployment: Rule-based system (Vercel optimized)
```

## 🛠️ Tech Stack

- **Backend**: Flask, Python 3.13
- **ML Pipeline**: Scikit-learn, Pandas, NumPy, Imbalanced-learn
- **Frontend**: HTML5, CSS3 (Glassmorphism), JavaScript
- **Deployment**: Vercel Serverless
- **Data**: EasyVisa dataset with feature engineering

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
    "confidence": 0.85,
    "score": 9,
    "details": "High qualification score with favorable factors"
}
```

## 🎯 Input Parameters

| Parameter | Type | Options |
|-----------|------|---------|
| Continent | Select | Asia, Europe, North America, South America, Africa, Oceania |
| Education | Select | High School, Bachelor's, Master's, Doctorate |
| Job Experience | Boolean | Yes/No |
| Training Required | Boolean | Yes/No |
| Employment Type | Boolean | Full-Time/Part-Time |
| Work Region | Select | Northeast, South, West, Midwest, Island |
| Salary Amount | Number | Any positive number |
| Pay Frequency | Select | Annual, Monthly, Weekly, Hourly |

## 🚀 Local Development

```bash
# Clone repository
git clone <your-repo-url>
cd MLA_Project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Train ML model (optional)
python save_model.py

# Run application
python app.py
# OR for Vercel-compatible version
python api/index.py
```

## 📁 Project Structure

```
MLA_Project/
├── api/
│   └── index.py              # Vercel serverless function
├── templates/
│   ├── index.html           # Main application UI
│   ├── result.html          # Prediction results page
│   └── error.html           # Error handling page
├── Notebooks/
│   ├── EDA_Visa_US.ipynb    # Exploratory data analysis
│   ├── Feature_Engineering.ipynb # Feature engineering
│   └── EasyVisa.csv         # Training dataset
├── app.py                   # Local Flask application
├── save_model.py            # ML model training script
├── test_model.py            # Model testing utilities
├── create_lightweight_model.py # Optimized model creation
├── requirements.txt         # Python dependencies
├── vercel.json             # Vercel deployment config
└── README.md               # Project documentation
```

## 🔧 Model Training

The ML pipeline includes:

1. **Data Preprocessing**:
   - Company age feature engineering
   - SMOTEENN for class balancing
   - Multi-encoder preprocessing pipeline

2. **Feature Engineering**:
   - OneHot encoding for categorical variables
   - Ordinal encoding for ordered categories
   - Standard scaling for numerical features
   - Power transformation for skewed distributions

3. **Model Selection**:
   - K-Nearest Neighbors with hyperparameter tuning
   - Distance-weighted predictions
   - Cross-validation optimization

## 🌐 Deployment

### Vercel Deployment
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel --prod
```

### Local Testing
```bash
# Test Vercel function locally
vercel dev
```

## ⚠️ Important Notes

- **Dual System**: Uses rule-based predictions for Vercel deployment (ML model available for local use)
- **Size Optimization**: Vercel version optimized to 196KB (under serverless limits)
- **Compatibility**: Handles both ML and rule-based predictions seamlessly
- **Disclaimer**: For informational purposes only - official decisions made by immigration authorities

## 📄 License

MIT License - Free for educational and commercial use.

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📞 Support

For questions or issues, please open a GitHub issue or contact the development team.

---

**Built with ❤️ for accurate visa assessment predictions**
