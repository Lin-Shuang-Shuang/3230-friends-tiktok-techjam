# TechJam 2025: Filtering the Noise - ML for Trustworthy Location Reviews

## 🎯 Project Overview
An ML-based system to evaluate the quality and relevancy of Google location reviews, automatically detecting spam, advertisements, irrelevant content, and fake rants.

## 🚀 Quick Start
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/3230-friends-tiktok-techjam.git
cd 3230-friends-tiktok-techjam

# Install dependencies
pip install -r requirements.txt

# Download required NLTK data
python -c "import nltk; nltk.download('vader_lexicon'); nltk.download('stopwords')"
```

## Download kaggle dataset
1. Sign up for a new account in Kaggle
2. Click on settings
2. Click 'Create New API Token'
3. Download kaggle.json
4. Place it in ~/.kaggle/ directory (`mkdir ~/.kaggle` and then `mv ~/Downloads/kaggle.json ~/.kaggle/`)
5. Run this: `
python3 scripts/data_collection/kaggle_data.py
`