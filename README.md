# TechJam 2025: Filtering the Noise - ML for Trustworthy Location Reviews

## Project Overview

**Filtering the Noise** is an innovative machine learning system designed to evaluate the quality and relevancy of Google location reviews. Our solution automatically detects and filters out:
- **Spam reviews** - Automated or promotional content
- **Advertisements** - Marketing disguised as reviews  
- **Irrelevant content** - Off-topic or unrelated comments
- **Fake rants** - Emotional outbursts without actual visit experience

This project addresses the critical challenge of maintaining review quality on location-based platforms, helping users find genuine, trustworthy feedback while reducing noise from low-quality content.

## Key Features

- **Multi-class Classification**: Distinguishes between genuine reviews, spam, irrelevant content, and rants
- **Advanced NLP Processing**: Uses state-of-the-art text preprocessing and feature extraction
- **CNN-based Model**: Implements convolutional neural networks for text classification
- **Automated Data Labeling**: Leverages Google Gemini API for efficient dataset annotation
- **Comprehensive Dataset**: Combines multiple data sources for robust training
- **Easy-to-Use Pipeline**: Simple setup and execution process

## Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Data Sources  │    │  Data Labeling  │    │  Model Training │
│                 │    │                 │    │                 │
│ • UCSD Dataset  │───▶│ • Gemini API    │───▶│ • CNN Model     │
│                 │    │ • Multi-label   │    │ • Text Features │
│ • Custom Data   │    │ • Quality Check │    │ • Classification│
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Quick Start

### Prerequisites

- Python 3.8+
- Google Gemini API key (for data labeling)
- Kaggle API credentials (optional, for additional data)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/3230-friends-tiktok-techjam.git
   cd 3230-friends-tiktok-techjam
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```


### Data Setup

1. **Download UCSD dataset**
   ```bash
   python scripts/data_collection/ucsd_data.py
   ```


## Data Labeling

Our innovative approach uses Google Gemini API for automated data labeling:

1. **Open the labeling notebook**
   ```bash
   jupyter notebook notebooks/Data_labelling.ipynb
   ```

2. **Configure your API key**
   - Replace `"YOUR_API_KEY"` with your Google Gemini API key
   - Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

3. **Update file paths**
   - Replace all `"PATH"` placeholders with your local file paths
   - Adjust `start_id` and `max_items` configurations as needed

4. **Run the cells**
   - Execute all cells to generate the labeled dataset
   - Output: `final_labeled_data_v3_3990_rows.csv`

## Model Training

Train the CNN-based classification model:

1. **Open the training notebook**
   ```bash
   jupyter notebook notebooks/Training_model.ipynb
   ```

2. **Run the training pipeline**
   - Load the labeled data `final_labeled_data_v3_3990_rows.csv` to Google Colab
   - Configures multi-class classification (genuine, spam, irrelevant, rant)
   - Trains a CNN model with text preprocessing
   - Evaluates model performance

### Model Architecture

- **Input**: Preprocessed text reviews
- **Embedding Layer**: Word embeddings for text representation
- **Convolutional Layers**: Feature extraction from text sequences
- **Global Max Pooling**: Dimensionality reduction
- **Dense Layers**: Final classification
- **Output**: Multi-class probabilities

## Project Structure

```
3230-friends-tiktok-techjam/
├── notebooks/                     # Jupyter notebooks
│   ├── Data_labelling.ipynb      # Automated data labeling
│   └── Training_model.ipynb      # Model training pipeline
├── scripts/                       # Utility scripts
│   └── data_collection/          # Data download scripts
├── README.md/                    # Documentation│
└── requirements.txt/                 


```


## Results

Our model achieves:
- **Multi-class classification** for review quality assessment
- **Automated labeling** reducing manual annotation effort
- **Scalable architecture** for large-scale review processing

## Technologies Used

- **Python**: Core programming language
- **TensorFlow/Keras**: Deep learning framework
- **Pandas/NumPy**: Data manipulation
- **NLTK**: Natural language processing
- **Google Gemini API**: Automated data labeling
- **Jupyter**: Interactive development
- **Scikit-learn**: Machine learning utilities

## Team

**Team 3230-Friends** - TikTok TechJam 2025

- **Project**: Filtering the Noise - ML for Trustworthy Location Reviews
- **Challenge**: Building reliable review quality assessment systems
- **Innovation**: Automated labeling with AI assistance

## License

This project is developed for TikTok TechJam 2025. All rights reserved.

## Acknowledgments

- **Google Gemini API** for automated data labeling capabilities
- **Kaggle** for providing restaurant review datasets
- **UCSD** for Google review datasets
- **TikTok TechJam** for the platform and challenge

---

**Ready to filter the noise and find genuine reviews! **
