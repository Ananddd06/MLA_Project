# 🛂 U.S. Visa Assessment Portal

> **Navigate Your American Dream with AI-Powered Predictions**

An intelligent web application that predicts U.S. visa application outcomes using advanced machine learning and rule-based algorithms. Experience our stunning glassmorphism UI that combines beauty with functionality, offering dual prediction systems for maximum reliability.

---

## ✨ Key Features

- **🤖 Dual AI System**: KNN ML model + intelligent rule-based fallback for comprehensive analysis
- **🎨 Modern UI**: Mesmerizing glassmorphism design with custom animations and micro-interactions
- **📱 Fully Responsive**: Seamlessly optimized for all devices, from mobile to desktop
- **⚡ Lightning Fast**: Instant predictions with detailed confidence scores
- **🚀 Vercel Ready**: Optimized for serverless deployment with zero configuration
- **🔒 Secure**: No sensitive data storage - your privacy is our priority
- **🌐 Global Accessibility**: Works from anywhere in the world, anytime

---

## 🚀 Live Demo

**Experience the Application**: [Live Application](https://mla-projectusvisa.vercel.app)

[![Vercel Deploy](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/yourusername/MLA_Project)

---

## 🎯 Prediction Systems

### Primary: KNN Machine Learning Model

<div align="center">
  <img src="https://img.shields.io/badge/Algorithm-KNN-blue" alt="KNN Algorithm">
  <img src="https://img.shields.io/badge/Features-10%2B-green" alt="Features">
  <img src="https://img.shields.io/badge/Accuracy-85%25-brightgreen" alt="Accuracy">
</div>

- **Algorithm**: K-Nearest Neighbors with distance weighting
- **Features**: 10 key visa application parameters
- **Data Processing**: SMOTEENN balancing + advanced feature engineering
- **Preprocessing**: OneHot + Ordinal encoding + StandardScaler
- **Performance**: Optimized for both accuracy and speed

### Fallback: Rule-Based Intelligence

Our intelligent rule-based system provides reliable predictions through a comprehensive scoring mechanism:

| Factor         | Scoring System                               | Impact              |
| -------------- | -------------------------------------------- | ------------------- |
| **Education**  | PhD(4) → Master's(3) → Bachelor's(2) → HS(1) | Foundation Score    |
| **Experience** | +2 points for job experience                 | Professional Edge   |
| **Training**   | +1 if no training required                   | Skill Readiness     |
| **Employment** | +1 for full-time positions                   | Stability Factor    |
| **Salary**     | +2 (>$80k), +1 (>$50k)                       | Economic Value      |
| **Region**     | West/Northeast(+2), South/Midwest(+1)        | Geographic Priority |

---

## 📊 Model Performance

```mermaid
graph LR
    A[Raw Data] --> B[Feature Engineering]
    B --> C[SMOTEENN Balancing]
    C --> D[Multi-encoder Pipeline]
    D --> E[KNN Model]
    E --> F[Prediction Results]

    style A fill:#f3f9ff,stroke:#2196f3
    style B fill:#e3f2fd,stroke:#2196f3
    style C fill:#bbdefb,stroke:#2196f3
    style D fill:#90caf9,stroke:#2196f3
    style E fill:#64b5f6,stroke:#2196f3
    style F fill:#42a5f5,stroke:#2196f3
```

**Technical Specifications**:

- **Algorithm**: K-Nearest Neighbors (n_neighbors=4, weights='distance')
- **Preprocessing**: SMOTEENN + Multi-encoder pipeline
- **Features**: 10 engineered features
- **Deployment**: Rule-based system (Vercel optimized)

---

## 🛠️ Tech Stack

<div align="center">

### Backend

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0+-black?style=for-the-badge&logo=flask)

### Machine Learning

![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange?style=for-the-badge&logo=scikit-learn)
![Pandas](https://img.shields.io/badge/Pandas-1.3+-blue?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-1.21+-blue?style=for-the-badge&logo=numpy)

### Frontend

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript)

### Deployment

![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel)

</div>

---

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
  "details": "High qualification score with favorable factors",
  "factors": {
    "education": 3,
    "experience": 2,
    "training": 1,
    "employment": 1,
    "salary": 2,
    "region": 2
  }
}
```

---

## 🎯 Input Parameters

| Parameter             | Type    | Options                                                     | Icon |
| --------------------- | ------- | ----------------------------------------------------------- | ---- |
| **Continent**         | Select  | Asia, Europe, North America, South America, Africa, Oceania | 🌍   |
| **Education**         | Select  | High School, Bachelor's, Master's, Doctorate                | 🎓   |
| **Job Experience**    | Boolean | Yes/No                                                      | 💼   |
| **Training Required** | Boolean | Yes/No                                                      | 📚   |
| **Employment Type**   | Boolean | Full-Time/Part-Time                                         | ⏰   |
| **Work Region**       | Select  | Northeast, South, West, Midwest, Island                     | 🗺️   |
| **Salary Amount**     | Number  | Any positive number                                         | 💰   |
| **Pay Frequency**     | Select  | Annual, Monthly, Weekly, Hourly                             | 📅   |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.13+
- Git
- Virtual environment (recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/MLA_Project.git
cd MLA_Project

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Train ML model (optional)
python save_model.py

# Run the application
python app.py
# OR for Vercel-compatible version
python api/index.py
```

---

## 📁 Project Structure

```
MLA_Project/
├── 📂 api/
│   └── 📄 index.py              # Vercel serverless function
├── 📂 templates/
│   ├── 📄 index.html           # Main application UI
│   ├── 📄 result.html          # Prediction results page
│   └── 📄 error.html           # Error handling page
├── 📂 Notebooks/
│   ├── 📄 EDA_Visa_US.ipynb    # Exploratory data analysis
│   ├── 📄 Feature_Engineering.ipynb # Feature engineering
│   └── 📄 EasyVisa.csv         # Training dataset
├── 📄 app.py                   # Local Flask application
├── 📄 save_model.py            # ML model training script
├── 📄 test_model.py            # Model testing utilities
├── 📄 create_lightweight_model.py # Optimized model creation
├── 📄 requirements.txt         # Python dependencies
├── 📄 vercel.json             # Vercel deployment config
└── 📄 README.md               # Project documentation
```

---

## 🔧 Model Training

### Data Preprocessing Pipeline

1. **Data Collection & Cleaning**

   - Missing value imputation
   - Outlier detection and handling
   - Data type optimization

2. **Feature Engineering**

   - Company age calculation
   - Salary normalization
   - Categorical encoding strategies

3. **Class Balancing**

   - SMOTEENN for handling imbalanced classes
   - Synthetic sample generation
   - Noise reduction techniques

4. **Model Training**
   - Hyperparameter optimization
   - Cross-validation
   - Performance evaluation

---

## 🌐 Deployment

### Vercel Deployment

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy to production
vercel --prod
```

### Local Testing

```bash
# Test Vercel function locally
vercel dev
```

### Environment Variables

Create a `.env` file in the root directory:

```
FLASK_ENV=development
FLASK_DEBUG=True
```

---

## ⚠️ Important Notes

- **Dual System**: Uses rule-based predictions for Vercel deployment (ML model available for local use)
- **Size Optimization**: Vercel version optimized to 196KB (under serverless limits)
- **Compatibility**: Handles both ML and rule-based predictions seamlessly
- **Disclaimer**: For informational purposes only - official decisions made by immigration authorities

---

## 📄 License & Copyright

<div align="center">

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)
![Copyright](https://img.shields.io/badge/Copyright-2024-blue.svg?style=for-the-badge)

</div>

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. Create a **feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. Open a **Pull Request**

### Contribution Guidelines

- Follow the existing code style
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting

---

## 📞 Support & Contact

<div align="center">

**Questions? Issues? Suggestions?**

[![GitHub Issues](https://img.shields.io/github/issues/yourusername/MLA_Project?style=for-the-badge)](https://github.com/yourusername/MLA_Project/issues)
[![GitHub Stars](https://img.shields.io/github/stars/yourusername/MLA_Project?style=for-the-badge)](https://github.com/yourusername/MLA_Project)
[![GitHub Forks](https://img.shields.io/github/forks/yourusername/MLA_Project?style=for-the-badge)](https://github.com/yourusername/MLA_Project/network)

</div>

For questions or issues, please open a GitHub issue or contact the development team at [contact@example.com](mailto:contact@example.com).

---

## 🙏 Acknowledgments

- The EasyVisa dataset for providing the training data
- The open-source community for the amazing tools and libraries
- All contributors who have helped improve this project

---

<div align="center">

**Built with ❤️ for accurate visa assessment predictions**

_"Your journey to America starts here"_

</div>
