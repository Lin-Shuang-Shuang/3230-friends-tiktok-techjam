import os
import pandas as pd
from pathlib import Path
import zipfile
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

import sys
sys.path.append(str(Path(__file__).parent.parent.parent))
RAW_DATA_DIR = Path(__file__).parent.parent.parent / "data" / "raw"

def setup_kaggle_credentials():
    """
    Setup Kaggle API credentials.
    You need to:
    1. Go to https://www.kaggle.com/account
    2. Click 'Create New API Token'
    3. Download kaggle.json
    4. Place it in ~/.kaggle/ directory ('mkdir ~/.kaggle' and then 'mv ~/Downloads/kaggle.json ~/.kaggle/')
    """
    kaggle_dir = Path.home() / '.kaggle'
    kaggle_dir.mkdir(exist_ok=True)
    
    kaggle_json = kaggle_dir / 'kaggle.json'
    if not kaggle_json.exists():
        print("Kaggle credentials not found!")
        return False
    
    os.chmod(kaggle_json, 0o600)
    print("Kaggle credentials found!")
    return True

def download_kaggle_dataset():
    """Download Google Maps Restaurant Reviews dataset from Kaggle."""
    if not setup_kaggle_credentials():
        return None
    
    try:
        api = KaggleApi()
        api.authenticate()
        
        dataset_name = "denizbilginn/google-maps-restaurant-reviews"
        
        download_path = RAW_DATA_DIR / "kaggle"
        download_path.mkdir(exist_ok=True)
        
        print(f"Downloading dataset: {dataset_name}")
        print(f"Download location: {download_path}")
        
        api.dataset_download_files(
            dataset_name,
            path=download_path,
            unzip=True
        )
        
        print("Dataset downloaded successfully!")
        
        files = list(download_path.glob("*"))
        print(f"Downloaded files: {[f.name for f in files]}")
        
        return download_path
        
    except Exception as e:
        print(f"Error downloading dataset: {str(e)}")
        return None

def load_kaggle_reviews(data_path=None):
    """Load and explore the Kaggle dataset."""
    if data_path is None:
        data_path = RAW_DATA_DIR / "kaggle"
    
    csv_files = list(data_path.glob("*.csv"))
    if not csv_files:
        print("No CSV files found in the download directory")
        return None
    
    print(f"Found CSV files: {[f.name for f in csv_files]}")
    
    main_csv = csv_files[0] 
    print(f"Loading: {main_csv.name}")
    
    try:
        df = pd.read_csv(main_csv)
        
        print("\nDataset Overview:")
        print(f"Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        print("\nFirst few rows:")
        print(df.head())
        
        print("\nData types:")
        print(df.dtypes)
        
        print("\nMissing values:")
        print(df.isnull().sum())
        
        output_path = RAW_DATA_DIR / "kaggle_reviews.csv"
        df.to_csv(output_path, index=False)
        print(f"Saved to: {output_path}")
        
        return df
        
    except Exception as e:
        print(f"Error loading dataset: {str(e)}")
        return None

def main():
    """Main function to download and process Kaggle data."""
    print("Starting Kaggle data collection...")
    
    RAW_DATA_DIR.mkdir(exist_ok=True, parents=True)
    
    download_path = download_kaggle_dataset()
    
    if download_path:
        df = load_kaggle_reviews(download_path)
        if df is not None:
            print("\nKaggle data collection completed successfully!")
            return df
    
    print("\nKaggle data collection failed!")
    return None

if __name__ == "__main__":
    main()