# 🚀 Vercel Deployment Guide

## Prerequisites
- GitHub account
- Vercel account (free)
- Git installed locally

## Step-by-Step Deployment

### 1. Initialize Git Repository
```bash
cd /Users/anand/Desktop/MLA_Project
git init
git add .
git commit -m "Initial commit: Visa Assessment Portal"
```

### 2. Create GitHub Repository
1. Go to [GitHub](https://github.com) and create a new repository
2. Name it: `visa-assessment-portal`
3. Don't initialize with README (we already have one)

### 3. Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/visa-assessment-portal.git
git branch -M main
git push -u origin main
```

### 4. Deploy to Vercel
1. Go to [Vercel](https://vercel.com)
2. Sign in with GitHub
3. Click "New Project"
4. Import your `visa-assessment-portal` repository
5. Vercel will auto-detect the configuration
6. Click "Deploy"

### 5. Environment Variables (if needed)
- No environment variables required for this project
- All dependencies are in `requirements.txt`

## File Structure for Vercel
```
MLA_Project/
├── api/
│   └── index.py          # Main Flask app for Vercel
├── templates/
│   ├── index.html        # Main form
│   ├── result.html       # Results page
│   └── error.html        # Error page
├── visa_model.pkl        # Trained ML model
├── preprocessor.pkl      # Data preprocessor
├── vercel.json          # Vercel configuration
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
└── .gitignore          # Git ignore file
```

## Vercel Configuration
The `vercel.json` file configures:
- Python runtime for the Flask app
- Route handling for all requests
- Static file serving

## Post-Deployment
1. Your app will be available at: `https://your-project-name.vercel.app`
2. Test the web interface and API endpoints
3. Update README.md with your live URL

## Troubleshooting
- Check Vercel deployment logs if issues occur
- Ensure all files are committed to Git
- Verify `requirements.txt` has correct versions

## Custom Domain (Optional)
1. In Vercel dashboard, go to your project
2. Click "Domains" tab
3. Add your custom domain
4. Follow DNS configuration instructions
